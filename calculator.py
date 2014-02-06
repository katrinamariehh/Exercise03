# take the input from the user
# tokenize the string
# evaluate the second and third tokens based on the first

from arithmetic import *

user_tired = raw_input("> ")

command = user_tired.split()

print command

if command[0] == "+":
    print add(int(command[1]), int(command[2]))
