# AOC 2020, 
# Day 6, Part 1

# Objective: Input is lists of question letters each group member has answered 'yes' to. Need to get count of how many questions have at least one 'yes' answer for each group and sum that.

import string

def parse_input(file_name):
    # The input will be processed to be a string for each group, with each members' answers separated by a space
    data_left = True
    input_array = []
    try:
        f = open(file_name, 'r')

        current_entry = ''
        while data_left == True:
            temp = f.readline()
            if temp == '':
                data_left = False
                input_array.append(current_entry)
                break
            elif temp == '\n':
                input_array.append(current_entry.lstrip())
                current_entry = ''
            else:
                current_entry = current_entry + ' ' + temp.rstrip('\n')
        return input_array
    except Exception as e:
        print(e)

input_strings = parse_input('day_6/input/day6_part1_input.txt')

count = 0

for group in input_strings:
    for char in string.ascii_lowercase:
        # if any char a-z appears in the group's collective answers, count it
        if char in group:
            count += 1

print(count)