# take the input from the user
# tokenize the string
# evaluate the second and third tokens based on the first

from arithmetic import *

while True:
    user_input = raw_input("> ")

    command = user_input.split()

# need to deal with if command has more than two items
# need to deal with if command other than comman[0] includes invalid input

    if command[0] == "+":
        total = 0
        for i in range(1, len(command)):
            total = add(int(total), int(command[i]))
        print total
    elif command[0] == "-":
        total = command[1]
        for i in range(2, len(command)):
            total = subtract(int(total), int(command[i]))
        print total
    elif command[0] == "*":
        total = 1
        for i in range(1, len(command)):
            total = multiply(int(total), int(command[i]))
        print total
    elif command[0] == "/":
        print divide(int(command[1]), int(command[2]))
    elif command[0] == "square":
        print square(int(command[1]))
    elif command[0] == "cube":
        print cube(int(command[1]))
    elif command[0] == "pow":
        print power(int(command[1]), int(command[2]))
    elif command[0] == "mod":
        print mod(int(command[1]), int(command[2]))
    elif command[0] == 'q':
        break
    else:
        print "That is not a valid command"