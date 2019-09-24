import random
import sys
from copy import deepcopy

from heuristics1 import heuristic1
from read import readin
from Difference import get_pure_literals
from keep_track_of_lit import get_not_yet_assigned_literals
from updates import update_clauses
from updates import update_literals

numbers_filled_in = []
numbers_not_possible = []
statements = []
# Size moet uit het grote document met meerdere oplossingen gehaald worden.
# de sudokus uit dit document gaan we veranderen naar de vorm van sudoku-example,
# zodat we onderstaande code daarvoor kunnen gebruiken.
size = 9
# new_truthvalues gives the literal and bool 1 if it is positive and bool 0 if it is negative
# new_truthvalues = {}

# to keep track of all the truthvalues
truthvalues = {}
decisions = []
number_of_splits = 0
solved = False


def random_choice(literals):
    # random choice for literal
    new_choice = random.choice(literals)
    print("new")
    print(new_choice)
    return new_choice


def split_with_copy(clauses, all_literals, truthvalues, negative_literals, positive_literals, number_of_splits):
    clauses_before_splitting = deepcopy(clauses)
    literal_before_splitting = deepcopy(all_literals)
    truthvalues_before_splitting = deepcopy(truthvalues)
    negative_literals_bef_spl = deepcopy(negative_literals)
    positive_literals_bef_spl = deepcopy(positive_literals)

    clauses_before_splitting2 = deepcopy(clauses)
    literal_before_splitting2 = deepcopy(all_literals)
    truthvalues_before_splitting2 = deepcopy(truthvalues)
    negative_literals_bef_spl2 = deepcopy(negative_literals)
    positive_literals_bef_spl2 = deepcopy(positive_literals)

    choice = random_choice(literal_before_splitting)
    # choice1 = heuristic1(clauses_before_splitting)
    print("choice")
    print(truthvalues_before_splitting)
    print(clauses_before_splitting)

    decisions.append(choice)
    truthvalues_before_splitting[choice] = True
    truthvalues_before_splitting[-choice] = False
    update_literals(choice, negative_literals_bef_spl, positive_literals_bef_spl, literal_before_splitting)
    update_clauses(clauses_before_splitting, truthvalues_before_splitting)

    decisions.append(choice)
    number_of_splits += 1

    solv = dp(clauses_before_splitting, truthvalues_before_splitting, negative_literals_bef_spl,
              positive_literals_bef_spl,
              literal_before_splitting)
    dp(clauses_before_splitting, truthvalues_before_splitting, negative_literals_bef_spl, positive_literals_bef_spl,
       literal_before_splitting)

    if solv == "solved":
        print("problem solved")
        return

    elif [] in clauses_before_splitting:
        decisions.append(-choice)
        truthvalues_before_splitting2[-choice] = True
        truthvalues_before_splitting2[choice] = False
        update_literals(-choice, negative_literals_bef_spl2, positive_literals_bef_spl2, literal_before_splitting2)
        update_clauses(clauses_before_splitting2, truthvalues_before_splitting2)

        decisions.append(-choice)

        dp(clauses_before_splitting2, truthvalues_before_splitting2, negative_literals_bef_spl2,
           positive_literals_bef_spl2,
           literal_before_splitting2)
        if [] in clauses_before_splitting2:
            return split_with_copy(clauses, all_literals, truthvalues, negative_literals, positive_literals,
                                   number_of_splits)

        else:
            return split_with_copy(clauses_before_splitting2, literal_before_splitting2, truthvalues_before_splitting2,
                                   negative_literals_bef_spl2, positive_literals_bef_spl2, number_of_splits)

    else:
        return split_with_copy(clauses_before_splitting, literal_before_splitting, truthvalues_before_splitting,
                               negative_literals_bef_spl, positive_literals_bef_spl, number_of_splits)


def dp(clauses, truthvalues, negative_literals, positive_literals, all_literals):
    print(clauses)
    # print(clause)
    for clause in clauses:
        if not clause:
            solution_still_possible = False

    stuck = True

    # kijk per clause of er een tautologie in zit of het unit variable is
    for clause in [*clauses]:
        # print(clauses)
        # print(clause)

        # check for unit clause
        if len(clause) == 1:
            print("unit")
            print(clause)

            # unit_check(clause[0], positive_literals, negative_literals, all_literals, truthvalues)
            unit_clause = clause[0]
            truthvalues[unit_clause] = True
            truthvalues[-unit_clause] = False

            # truth value assigned, so literals can be removed from lists
            # (trying to find a better way to do this)

            update_literals(unit_clause, negative_literals, positive_literals, all_literals)

            update_clauses(clauses, truthvalues)
            stuck = False

    # gets difference of negative and positive literals, so gives the pure literals
    list_of_pure_literals = get_pure_literals(positive_literals, negative_literals)
    # print("list of pure literals")
    # print(list_of_pure_literals)

    for literal in list_of_pure_literals:
        truthvalues[literal] = True
        truthvalues[-literal] = False
        # print(truthvalues)

        update_literals(literal, negative_literals, positive_literals, all_literals)

        if list_of_pure_literals:
            list_of_pure_literals = []
            stuck = False

    update_clauses(clauses, truthvalues)
    # print(clauses)
    if not clauses:
        print(truthvalues)
        return "solved"

    if not stuck:
        dp(clauses, truthvalues, negative_literals, positive_literals, all_literals)

    return clauses, truthvalues, negative_literals, positive_literals, all_literals


def main():
    print("Which heuristic would you like to use?\n Type 1 for the DPLL, type 2 for the other one")

    # read in sudoku file, for now we have just one sudoku.
    sudoku_file = open('sudoku-example.txt', 'r')
    file_contents = sudoku_file.readlines()
    sudoku_unsolved = readin(file_contents)

    sudoku_rules = open('sudoku-rules.txt', 'r')
    rules = sudoku_rules.readlines()
    sudoku_rules.close()

    # uncomment to get sudoku to be tested
    # clauses = readin(rules)

    # for filled_in in sudoku_unsolved:
    #    clauses.insert(0, filled_in)
    #    print(clauses)

    # voorbeeld om te debuggen
    clauses = [[2, -4], [4, 3], [1, -1], [-3, -2], [-5], [6, -5]]

    # make list to keep track of negative and positive literals that have no truth-value yet
    negative_literals = []
    positive_literals = []
    all_literals = []
    positive_literals, negative_literals, all_literals = get_not_yet_assigned_literals(clauses,
                                                                                       positive_literals,
                                                                                       negative_literals)

    # check for tautology (only need to do this once)
    for clause in [*clauses]:

        # check for tautology
        for literal in clause:
            if -literal in clause:
                print("tautology")
                clauses.remove(clause)
                # print(clauses)
                break

    # stuck = False
    solution_still_possible = True

    # run DP algorithm (unit, tautology and pure literal check)
    dp(clauses, truthvalues, negative_literals, positive_literals, all_literals)

    if [] in clauses:
        solution_still_possible = False

    while solution_still_possible:
        # zolang er nog een simpele keuze te maken is, gaan we dat doen

        if dp(clauses, truthvalues, negative_literals, positive_literals, all_literals) == "solved":
            print("solved")
            break

        else:
            split_with_copy(clauses, all_literals, truthvalues, negative_literals, positive_literals, number_of_splits)


# Call the main function
main()
