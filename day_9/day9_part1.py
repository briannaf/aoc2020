# AOC 2020, 
# Day 9, Part 1

# Objective: Input is list of numbers. Find first number that is not a sum of 2 of the 25 preceding numbers

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
        return None

sequence = parse_input('day_9/input/day9_part1_input.txt')

for i in range(25, len(sequence) - 1):
    sum_exists = False
    subset = sequence[i - 25:i]
    desired_sum = sequence[i]
    for number in subset:
        if desired_sum - number in subset:
            sum_exists = True
    if sum_exists == False:
        print('%s is not the sum of 2 of its 25 preceding numbers.' % sequence[i])