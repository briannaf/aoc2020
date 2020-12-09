# AOC 2020, 
# Day 8, Part 1

# Objective: Find value of accumulator value right before infinite loop in input
# Opcodes: 
#   acc: add argument to accumulator
#   nop: do nothing
#   jmp: jump specified amt of commands

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

def process_commands(command_list):
    command_regex = re.compile('(\w{3}) ([0-9\+\-]+)')
    output_list = []

    for command in command_list:
        result = command_regex.search(command)
        opcode = result[1]
        argument = int(result[2])
        output_list.append((opcode, argument))
    return output_list

input_array = parse_input('day_8/input/day8_part1_input.txt')
commands = process_commands(input_array)

accumulator = 0
visited = []

i = 0
while i not in visited:
    command = commands[i]
    print(str(i) + ': ' + command[0] + ' ' + str(command[1]) + ', ' + str(accumulator))
    visited.append(i)
    if command[0] == 'nop':
        i += 1
    if command[0] == 'acc':
        accumulator += command[1]
        i += 1
    if command[0] == 'jmp':
        i += command[1]

print(accumulator)