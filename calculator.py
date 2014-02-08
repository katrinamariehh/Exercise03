# take the input from the user
# tokenize the string
# evaluate the second and third tokens based on the first

from arithmetic import *

while True:
    user_input = raw_input("> ")

    command = user_input.split()

# need to deal with if command has more than two items
# need to deal with if command other than command[0] includes invalid input

     
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
        total = command[1]
        for i in range(2, len(command)):
            total = divide(int(total), int(command[i]))
        print total
    elif command[0] == "square":
        if len(command) > 2:
            print "The square function takes only one argument; please try again."
        else:
            print square(int(command[1]))
    elif command[0] == "cube":
        if len(command) > 2:
            print "The cube function takes only one argument; please try again."
        else:
            print cube(int(command[1]))
    elif command[0] == "pow":
        total = command[1]
        for i in range(2, len(command)):
            total = power(int(total), int(command[i]))
        print total
    elif command[0] == "mod":
        if len(command) > 3:
            print "The modulo function takes only two arguments; please try again."
        else:
            print mod(int(command[1]), int(command[2]))
    elif command[0] == 'q':
        break
    else:
        print "That is not a valid command"