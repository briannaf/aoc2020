# AOC 2020, 
# Day 2, Part 2

# Objective: Validate passwords using different scheme-- upper bound and 
# lower bound are now indices (not zero-indexed), and exactly one of these indices must 
# contain letter.

import re

def parse_input(file_name):
    data_left = True
    input_array = []
    try:
        f = open(file_name, 'r')

        while data_left == True:
            temp = f.readline()
            if temp == '':
                data_left = False
                break
            input_array.append(temp)

        return input_array
    except Exception as e:
        print(e)
        return None

def process_input(input_array):
    # This takes the string that represents each password and its 
    # policy and breaks it into a tuple of the following format:
    #     (lower_bound, upper_bound, letter, password_string)

    new_array = []
    password_regex = re.compile('(\d+)-(\d+) (\w): (\w+)')

    for item in input_array:
        result = password_regex.match(item)
        new_array.append((result[1], result[2], result[3], result[4]))

    return new_array

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