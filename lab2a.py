# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/09/21
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file

# creat a variable "x" and get the value from user
x = input("Enter a integer: ")
# print out the type of "x"
print(type(x))

# convert "x" to integer and assign it again
x = int(x)

# create if-statement
# the condition is x need greater than or equal to 6
if x >= 6:
    ## while the condition is "TRUE" print out "x is greater then 6!"
    print("x is greater then 6!")

# the condition is x greater than or equal to 4 and x is less than 12
elif x >=4 and x < 12:
    # while the condition is "TRUE" print out appropriate message
    print("TRUE")
