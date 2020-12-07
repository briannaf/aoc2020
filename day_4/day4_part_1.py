# AOC 2020, 
# Day 4, Part 1

# Objective: Validate passports/ids. Valid ids contain these fields:
# byr
# iyr
# eyr
# hgt
# hcl
# ecl
# pid
# And they do not have to contain cid.
# Formatting can be different, but a newline will be between each id

import re

# Compiling regexes up here for efficiency, and so they can be global
fields = [re.compile('byr'), re.compile('iyr'), re.compile('eyr'), re.compile('hgt'), re.compile('hcl'), re.compile('ecl'), re.compile('pid')]

def parse_input(file_name):
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
                input_array.append(current_entry)
                current_entry = ''
            else:
                current_entry = current_entry + temp.rstrip('\n') + ' '

        return input_array
    except Exception as e:
        print(e)

def check_id(identification):
    global fields

    valid = True

    for item in fields:
        if item.search(identification) == None:
            valid = False
            break

    return valid

ids = parse_input('day_4/input/day4_part1_input.txt')
count = 0

for item in ids:
    if check_id(str(item)) == True:
        count += 1

print(count)