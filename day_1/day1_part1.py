# AOC 2020
# Day 1, Part 1

# Objective: get 2 numbers from input that sum to 2020; return the result of multiplying them

import time

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
            input_array.append(int(temp))

        return input_array
    except Exception as e:
        print(e)

input = parse_input('./input/day1_part1_input.txt')
print('Successfully parsed input')

for number in input:
    for second_number in input:
        if (number + second_number) == 2020:
            number_a = number
            number_b = second_number
            break

print(number_a, number_b, '\n', number_a*number_b)