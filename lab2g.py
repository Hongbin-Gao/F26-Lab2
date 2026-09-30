# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin Gao
# Date: 2026/09/29
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.


# Get the taxable income and marital status from the user.
income = float(input("Enter your taxable income: "))
status = input("Enter your status (single or married): ").lower()

# Calculate tax using the tax table from the lab instructions.
# user is single
if status == "single":
    # income at most 32000
    if income <= 32000:
        tax = income * 0.10    
    # income over 32000    
    else:
        tax = 3200 + (income - 32000) * 0.25
    print(f"Your tax is ${tax:.2f}")
# user married
elif status == "married":
    # income at most 64000
    if income <= 64000:
        tax = income * 0.10
    # income over 64000
    else:
        tax = 6400 + (income - 64000) * 0.25
    print(f"Your tax is ${tax:.2f}")
# user enter status without single or married
else:
    print("Invalid status. Please enter single or married.")



