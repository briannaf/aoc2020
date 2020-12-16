# AOC 2020, 
# Day 9, Part 2

# Objective: Find a contiguous set of at least two numbers from the list that 
# sum the the invalid number from part 1 (in the case for my dataset, this is 
# 144381670). The answer to the puzzle is the sum of the lowest and highest 
# number in this set.

from day9_part1 import parse_input

sequence = parse_input('day_9/input/day9_part1_input.txt')

for i in range(len(sequence)):
    for j in range(i+1, len(sequence)):
        if sum(sequence[i:j]) == 144381670:
            print(sequence[i:j])
            result = min(sequence[i:j]) + max(sequence[i:j])
            print(result)