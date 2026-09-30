# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin Gao
# Date: 2026/09/28
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
#for fruit in fruits:
#    print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.

# creat a variable
total = 0
# iterate from 1 to 100
for number in range(1, 101):
    # Check if it is an even number.
    if number % 2 == 0:
        total = total + number
print(total)
