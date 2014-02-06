# take the input from the user
# tokenize the string
# evaluate the second and third tokens based on the first

from arithmetic.py import *

command = raw_input.split(" ")

if command[0] == "+":
    add(command[1], command[2])
elif command[0] == "-":
    subtract(command[1], command[2])
elif command[0] == "*":
    multiply(command[1], command[2])