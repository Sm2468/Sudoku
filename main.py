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


def main():
    # Open a file named numbers.txt
    sudoku_file = open('sudoku-example.txt','r')

    # read the numbers on the file
    file_contents = sudoku_file.read()

    numbers_filled_in = file_contents.split(" 0\n")

    # Close the the numbers file
    sudoku_file.close()

    # Print the data that was inside the file
    #print(file_contents)
    print(numbers_filled_in)
    for number in numbers_filled_in:

        row = number[0]
        column = number[1]
        getal = number[2]

        # if a number is filled in, set all other numbers on that position to negative
        if number != "":
            statements.append(number)
            #print(number+ " number ")
            #print(getal)
            for i in range(1, size+1):
                new_number = row + column
                if str(i) != getal:
                    new_number = new_number+str(i)
                    #print(new_number + " new")
                    numbers_not_possible.append(new_number)
                    statements.append("-" + new_number)
        # if a number is filled in, set every position in the same column, row and box negative for that number.
        else:
            for i in range(1, size+1):
                if i != row:
                    new_number = i+column+getal
                    numbers_not_possible.append(new_number)
                    statements.append("-" + new_number)
                if j != column:
                    new_number = row+j+getal
                    numbers_not_possible.append(new_number)
                    statements.append("-" + new_number)



    print(numbers_not_possible)
    print(statements)
# Call the main function
main()
