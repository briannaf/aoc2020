# AOC 2020, 
# Day 6, Part 2

# Objective: Same input list and same objective as part one, but instead of the sum including each question at least one group member has answered 'yes' to, it must include how many questions every group member answered 'yes' to.

import string
from day6_part1 import parse_input

def count_common_answers(group):
    group = group.split()
    
    if len(group) == 1:
        return len(group[0])

    # make a set out of lowercase a-z
    result = set(string.ascii_lowercase)

    # find the intersection of that set against each group member's answer set, all in a row.
    # if a group member doesn't have it in their answers, it'll get knocked out of the result set
    for i in group:
        i = set(i)
        result = i.intersection(result)

    return len(result)

input_strings = parse_input('day_6/input/day6_part1_input.txt')

count = 0
for group in input_strings:
    count += count_common_answers(group)

print(count)