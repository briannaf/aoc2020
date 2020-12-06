# AOC 2020, 
# Day 2, Part 2

# Objective: Validate passwords using different scheme-- upper bound and 
#   lower bound are now indices (not zero-indexed), and exactly one of 
#   these indices must contain letter.

import re
from day2_part1 import parse_input, process_input

def check_password_validity(password_tuple):
    lower_bound = int(password_tuple[0])
    upper_bound = int(password_tuple[1])
    letter = password_tuple[2]
    password_string = password_tuple[3]

    valid = False
    if password_string[lower_bound - 1] == letter:
        valid = not valid
    if password_string[upper_bound - 1] == letter:
        valid = not valid

    return valid

input = parse_input('./day_2/input/day2_part1_input.txt')
input = process_input(input)

count = 0

for item in input:
    if check_password_validity(item) == True:
        count += 1

print(count)