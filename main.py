from read import readin
from Difference import Diff
from unitcheck import unit_check
from purelit import pure

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

    clauses = [[2, -4], [4, 3], [-3, -2]]
    # make list to keep track of pure literals
    negative_literals = []
    positive_literals = []
    positive_literals = pure(clauses, positive_literals, negative_literals)[0]
    negative_literals = pure(clauses, positive_literals, negative_literals)[1]

    print(clauses)
    print(positive_literals)
    print(negative_literals)

    stuck = 0
    #clauses.insert(0, [122, -122])
    while clauses:
        if not stuck:
            for clause in clauses:
                print(clause)

                # check for tautology
                for variable in clause:
                    if -variable in clause:
                        print("tautology")
                        clause.remove(-variable)
                        clauses.remove(clause)

                # check for pure literal
                list_of_literals = Diff(truthvalues, positive_literals, negative_literals)


                # check for unit clause
                if len(clause) == 1:
                    unit_check(clause, positive_literals, negative_literals, truthvalues)
                    clauses.remove(clause)

                # update list of clauses
                for truthvalue in truthvalues:
                    if truthvalue in clause:
                        if clause in clauses:
                            if truthvalues[truthvalue]:
                                clauses.remove(clause)
                            else:
                                clause.remove(truthvalue)

                pure(clauses, positive_literals, negative_literals)


    #else:
    #    print("split")


        #for value in truthvalues:
         #   if value in clause:




    #print(truthvalues)


    #Open a file named numbers.txt
    #sudoku_file = open('sudoku-example.txt','r')

    # read the numbers on the file
    #file_contents = sudoku_file.read()

    #numbers_filled_in = file_contents.split(" 0\n")
    #numbers_filled_in.remove("")

    # Close the the numbers file
    #sudoku_file.close()

    # Print the data that was inside the file
    #print(file_contents)
    #print(numbers_filled_in)
    #first_line = numbers_filled_in[0]
    #variables = first_line.split(" ")[2]
    #number_of_clauses = first_line.split(" ")[3]
    #numbers_filled_in.pop(0)
    #for number in numbers_filled_in:

        # if a number is filled in, set all other numbers on that position to negative
        #if number != "":

            #row = number[0]
            #column = number[1]
            #getal = number[2]

            #statements.append(number)
            #print(number+ " number ")
            #print(getal)
            #for i in range(1, size+1):
                #new_number = row + column
                #if str(i) != getal:
                    #new_number = new_number+str(i)
                    #print(new_number + " new")
                    #numbers_not_possible.append(new_number)
                    #statements.append("-" + new_number)
                    # if a number is filled in, set every position in the same column, row and box negative for that number.
                #else:
                    #if i != row:
                        #new_number = str(i) + column + getal
                        #numbers_not_possible.append(new_number)
                        #statements.append("-" + new_number)
                    #if i != column:
                        #new_number = row + str(i) + getal
                        #numbers_not_possible.append(new_number)
                        #statements.append("-" + new_number)



    #print(numbers_not_possible)
    #print(statements)

    # Open a file named numbers.txt
    #clauses = open('sudoku-rules.txt', 'r')

    # read the numbers on the file
    #


    #numbers_filled_in = file_contents.split(" 0\n").ToList()
    #numbers_filled_in.pop(0)

    # Close the the numbers file
    #clauses.close()

    # Print the data that was inside the file
    # print(file_contents)
    #print(numbers_filled_in)

# Call the main function
main()
