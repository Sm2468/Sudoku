from TruthValue import TruthValue
#from readin import readin

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
maxvar = 0


def readin(file):
    cnf = list()
    cnf.append(list())
    for line in file:
        tokens = line.split()
        if len(tokens) != 0 and tokens[0] not in ("p", "c"):
            for tok in tokens:
                lit = int(tok)
                maxvar = max(maxvar, abs(lit))
                if lit == 0:
                    cnf.append(list())
                else:
                    cnf[-1].append(lit)

    assert len(cnf[-1]) == 0
    cnf.pop()

    return cnf

def main():
    sudoku_file = open('sudoku-example.txt', 'r')
    file_contents = sudoku_file.readlines()

    sudoku_rules = open('sudoku-rules.txt', 'r')
    rules = sudoku_rules.readlines()
    sudoku_rules.close()

    Truths = []

    sudoku_unsolved = readin(file_contents)
    clauses = readin(rules)
    for number in sudoku_unsolved:

        Truths.append(TruthValue(number, 1))
        for clause in clauses:
            if len(clause) == 1:
                if int(clause[0]) > 0:
                    Truths.append(TruthValue(clause[0], 1))
                else:
                    Truths.append(TruthValue(-clause[0], 0))
                


            if str(number) in clause:
                clause.pop(number)





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
