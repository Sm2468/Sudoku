from read import readin
from Difference import pure_check
from unitcheck import unit_check
from purelit import get_not_assigned_literals
from split import random_choice
from updateclauses import update
from update_literal import updatelit

numbers_filled_in = []
numbers_not_possible = []
statements = []
row = ""
column = ""
getal = ""
# Size moet uit het grote document met meerdere oplossingen gehaald worden.
# de sudokus uit dit document gaan we veranderen naar de vorm van sudoku-example,
# zodat we onderstaande code daarvoor kunnen gebruiken.
size = 9
truthvalues = {}
decisions = []

def main():
    # inlezen van sudokus, maar voor nu gebruiken we nog het simpele voorbeeld.
    sudoku_file = open('sudoku-example.txt', 'r')
    file_contents = sudoku_file.readlines()
    sudoku_unsolved = readin(file_contents)

    sudoku_rules = open('sudoku-rules.txt', 'r')
    rules = sudoku_rules.readlines()
    sudoku_rules.close()
    #clauses = readin(rules)
    #for filled_in in sudoku_unsolved:
    #    clauses.insert(0, filled_in)
    #print(clauses)

    # voorbeeld om te debuggen
    clauses = [[2, -4], [4, 3], [1, -1], [-3, -2], [-5], [6, -5]]

    # make list to keep track of negative and positive literals that have no truth-value yet
    negative_literals = []
    positive_literals = []
    all_literals = []
    positive_literals, negative_literals, all_literals = get_not_assigned_literals(clauses, positive_literals, negative_literals)

    stuck = 0
    solution_still_possible = 1
    # zolang er nog clauses zijn om opgelost te worden, gaan we door met keuzes maken
    while clauses != [[]]:

        while solution_still_possible:

            # zolang er nog een simpele keuze te maken is, gaan we dat doen
            if not stuck:
                stuck = 1

                # kijk per clause of er een tautologie in zit of het unit variable is
                for clause in clauses:
                    if clause:
                        print(clauses)
                        print(clause)

                        # check for tautology
                        for literal in clause:
                            if -literal in clause:

                                print("tautology")
                                clauses.remove(clause)
                                print(clauses)

                                # stuck veranderen zodat we nogmaals voor simpele oplossing gaan zoeken
                                # (kan nu weer wat verandert zijn waardoor dit opnieuw kan)
                                stuck = 0
                                break

                        # check for unit clause
                        if len(clause) == 1:
                            print("unit")

                            # unit_check(clause, positive_literals, negative_literals, all_literals, truthvalues)
                            unit_clause = clause[0]
                            truthvalues[unit_clause] = 1
                            truthvalues[-unit_clause] = 0

                            # truth value assigned, so literals can be removed from lists
                            # (trying to find a better way to do this)

                            # updatelit(unit_clause, negative_literals, positive_literals, all_literals)

                            all_literals.remove(unit_clause)
                            if unit_clause in negative_literals:
                                negative_literals.remove(unit_clause)
                            if -unit_clause in negative_literals:
                                negative_literals.remove(-unit_clause)
                            if unit_clause in positive_literals:
                                positive_literals.remove(unit_clause)
                            if -unit_clause in positive_literals:
                                positive_literals.remove(-unit_clause)

                            clauses.remove(clause)
                            stuck = 0


                # gets difference of negative and positive literals, so gives the pure literals
                list_of_pure_literals = pure_check(positive_literals, negative_literals)
                print("list of pure literals")
                print(list_of_pure_literals)

                for literal in list_of_pure_literals:
                    truthvalues[literal] = 1
                    truthvalues[-literal] = 0
                    print(truthvalues)

                    updatelit(literal, negative_literals, positive_literals, all_literals)

                    if list_of_pure_literals:
                        list_of_pure_literals = []
                        stuck = 0

                clauses = update(clauses, truthvalues)
                print(clauses)
                print("stuck")
                print(stuck)

                        # denk niet dat deze hier hoeft, maar laat hem voor zekerheid nog even staan
                        # pure(clauses, positive_literals, negative_literals)
            else:
                # als er nog niets is gekozen, dan kiezen we een random literal die we waarde true geven
                # en zetten deze in de lijst met decisions.
                split_bool = 1
                while split_bool:

                    if not decisions:
                        choice = random_choice(all_literals)
                        decisions.append([choice, "opposite not tried"])

                        # als het inverse van de laatste decision nog niet is geprobeerd, probeer dat dan
                    elif decisions[-1][1] == "opposite not tried":
                        decisions.append([-decisions[-1][0], "opposite tried"])
                        decisions.pop(-2)

                    else:
                        split_bool = 0

                #else:
                    # kijk naar de twee-na-laatste decision

        else:
            old_decision = decisions.keys()[-1]
            new_decision = - decisions.keys()[-1]

    print(truthvalues)



# Call the main function
main()
