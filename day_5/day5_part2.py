# AOC 2020, 
# Day 5, Part 2

# Objective: Find your seat number-- it will be the 'missing' seat number. 
#   However, some of the seats at the very front and back aren't on the flight,
#   so that must be taken into account.

from day5_part1 import parse_input, process_pass

temp_passes = parse_input('day_5/input/day5_part1_input.txt')
# print(temp_passes)
passes = []

lowest_num = 1500

for item in temp_passes:
    temp_pass_num = process_pass(item)
    passes.append(temp_pass_num)
    if temp_pass_num < lowest_num:
        lowest_num = temp_pass_num

for i in range(lowest_num, 1500):
    if i not in passes:
        print(i)
        break