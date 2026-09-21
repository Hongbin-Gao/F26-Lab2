
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Hongbin
# Date:2026/09/21
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user

# create variables "str1", "str2"
# get the value from user  
# use len() to get the figure
str1 = input("Enter something: ")
str2 = input("Enter something: ")

str1_len = len(str1)
str2_len = len(str2)

# create if-statement
# print "str1 longer then str2", when str1 > str2
if str1_len > str2_len:
    print(f"'{str1}' is longer then '{str2}'!")

# print "str2 longer then str1", when str2 > str1
elif str2_len > str1_len:
    print(f"'{str2}' is longer then '{str1}'!")

# print "str1 and str2 are of equal length", when str1 = str2
else:
    print(f"'{str1}' and '{str2}' are of equal length")