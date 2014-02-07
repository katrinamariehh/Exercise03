# take the input from the user
# tokenize the string
# evaluate the second and third tokens based on the first

from arithmetic import *

user_input = raw_input("> ")

command = user_input.split()

methods = {
    "+": add,
    "-": subtract,
    "*": multiply
}

if command[0] == "+":
    print add(int(command[1]), int(command[2]))
if command[0] == "-":
    print subtract(int(command[1]), int(command[2]))
