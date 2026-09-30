# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin Gao
# Date: 2026/09/28
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

import sys

argument_count = len(sys.argv) - 1
if argument_count < 2:
    print("The script requires at least 2 arguments.")
elif argument_count >= 2:
    name = sys.argv[1]
    age = sys.argv[2]
    print(f"Hi {name}, you are {age} years old and the script received {argument_count} arguments.")
