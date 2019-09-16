from read import readin
from Difference import pure_check
from unitcheck import unit_check
from purelit import pure
from split import split

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
truthvalues={}


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
    clauses = [[2, -4], [4, 3], [-5], [-3, -2], [1, -1], [6, -5]]

    # make list to keep track of negative and positive literals that have no truth-value yet
    negative_literals = []
    positive_literals = []
    all_literals = []
    positive_literals, negative_literals, all_literals = pure(clauses, positive_literals, negative_literals)

    stuck = 0
    # zolang er nog clauseszijn om opgelost te worden, gaan we door met keuzes maken
    while clauses != [[]]:

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

                            # remove -literal zodat we geen probleem met for loop krijgen
                            clause.remove(-literal)
                            clauses.remove(clause)

                            # stuck veranderen zodat we nogmaals voor simpele oplossing gaan zoeken
                            # (kan nu weer wat verandert zijn waardoor dit opnieuw kan)
                            stuck = 0

                    # check for unit clause
                    if len(clause) == 1:
                        print("unit")

                        # unit_check(clause, positive_literals, negative_literals, all_literals, truthvalues)
                        unit_clause = clause[0]
                        truthvalues[unit_clause] = 1
                        truthvalues[-unit_clause] = 0

                        # truth value assigned, so literals can be removed from lists
                        # (trying to find a better way to do this)
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
                print("list of literals")
                print(list_of_pure_literals)
                for literal in list_of_pure_literals:
                    truthvalues[literal] = 1
                    truthvalues[-literal] = 0

                    # denk dat hier iets fout gaat
                    all_literals.remove(literal)
                    all_literals.remove(-literal)

                # als de lijst niet leeg is, verwijder de lijst,
                # zodat we de volgende keer weer dezelfde naam kunnen gebruiken voor de lijst.
                if list_of_pure_literals:
                    del list_of_pure_literals
                    stuck = 0

                    # update list of clauses
                    for clause in clauses:
                        for truthvalue in truthvalues:
                            if truthvalue in clause:

                                # extra if loop omdat ik tussendoor clauses remove, doet anders raar...
                                if clause in clauses:

                                    # verwijder de clause waarin een waarde staat die al waar is.
                                    if truthvalues[truthvalue]:
                                        clauses.remove(clause)

                                    # verwijder een literal uit een clause waarvan je weet dat die niet waar is.
                                    else:
                                        clause.remove(truthvalue)

                    # denk niet dat deze hier hoeft, maar laat hem voor zekerheid nog even staan
                    # pure(clauses, positive_literals, negative_literals)
        else:
            decisions = []
            split(all_literals, decisions)
        # print(truthvalues)

    print(truthvalues)



# Call the main function
main()
