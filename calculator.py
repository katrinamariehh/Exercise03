# take the input from the user
# tokenize the string
# evaluate the second and third tokens based on the first

from arithmetic import *

user_input = raw_input("> ")

command = user_input.split()

# need to deal with if command has more than two items
# need to deal with if command other than comman[0] includes invalid input

if command[0] == "+":
    print add(int(command[1]), int(command[2]))
elif command[0] == "-":
    print subtract(int(command[1]), int(command[2]))
elif command[0] == "*":
    print multiply(int(command[1]), int(command[2]))
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
else:
    print "That is not a valid command"