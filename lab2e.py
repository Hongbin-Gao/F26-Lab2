# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin Gao
# Date: 2026/09/25
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file

# import "sys" module
import sys

list = len(sys.argv[1:])
# print out how many arguments provideed after script name


if list == 0:
#if the user not provide arguments
    print("This script requires exactly two arguments. No arguments were provided!")
elif list < 2 or list > 2 :
    print("This script requires exactly two arguments. You provided three arguments.")
else:
    print("Hello user, good job, your provided two arguments!")