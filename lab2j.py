# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin 
# Date: 2026/09/29
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO 1: 
# Import the `math` module.
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.

# TO DO 2: 
# Create an infinite loop using while True. Inside the loop:
# Check if num is negative:
# If it is, print "Invalid number." and continue to the next iteration of the loop.

# TO DO 3: 
# Check if num is zero:
# If it is, print "Exiting..." and break out of the loop.

# TO DO 4: 
#Calculate the square root of num using the math.sqrt function.


# import module
import math

# infinite loop
while True:
    num = float(input("Please type in a number: "))
    # if the number is negative
    if num < 0:
        print("Invalid number.")
        # restart loop
        continue
    # if the number is 0
    if num == 0:
        print("Exiting...")
        # exit loop
        break
    # it is Non-Negative Number
    print(math.sqrt(num))
