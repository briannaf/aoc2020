# AOC 2020
# Day 1, Part 2

# Objective: Find product of three numbers from input list that sum to 2020
# Notes: Maybe find a more optimized way later

from day1_part1 import parse_input

input = parse_input('input/day1_part1_input.txt')
print('Successfully parsed input')

for number in input:
    for second_number in input:
        if (number + second_number) < 2020:
            for third_number in input:
                if number + second_number + third_number == 2020:
                    number_a = number
                    number_b = second_number
                    number_c = third_number
                    break

print(number_a, number_b, number_c, '\n', number_a*number_b*number_c)