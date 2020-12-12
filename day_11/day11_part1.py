# AOC 2020, 
# Day 11, Part 1

# Objective: This puzzle seems to be like Conway's game of life, but with different rules.
    # The input is a seating chart. '.' represents floor, 'L' represents empty seats, and '#' represents an occupied seat. 
    # Rules:
    #     - An empty seat with no occupied seats adjacent to it becomes occupied
    #     - An occupied seat with four or more adjacent occupied seats, it becomes empty
    #     - No change otherwise.
    # The pattern will reach equilibrium at some point. How many seats are occupied when that happens?

seating_chart = []

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
            input_array.append(temp.rstrip())

        return input_array
    except Exception as e:
        print(e)
        return None

def check_seat(y, x):
    global seating_chart

    if seating_chart[y][x] == '.':
        return '.'
    
    occupied = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if seating_chart[y + i][x + j] == '#' and y + i >= 0 and x + j >= 0:
                    occupied += 1
            except IndexError:
                pass
            except Exception as e:
                print(e)

    if seating_chart[y][x] == 'L' and occupied == 0:
        return '#'
    if seating_chart[y][x] == '#' and occupied >= 5: #we count the occupied seat itself, has to be >= 5, not 4
        return 'L'
    
    return seating_chart[y][x]

seating_chart = parse_input('day_11/input/day11_part1_input.txt')
# seating_chart = parse_input('day_11/input/day11_sample_input.txt')

# Going to model seating chart with 2d array, and check each seat. The resulting symbol for the seat's new state will be strored in a temp list, then copied over after all is calculating, since modifying in place will mess up the results
# 2d list addressing: list[y][x] / list[vert][horiz]
rows = len(seating_chart[0])
cols = len(seating_chart)

temp_list = [['.' for i in range(rows)] for j in range(cols)]

count = 0

while True:
    for y in range(cols):
        for x in range(rows):
            temp_list[y][x] = check_seat(y,x)
    if temp_list == seating_chart:
        break
    else:
        # can't just use = operator, that just sets the reference
        seating_chart = [row[:] for row in temp_list]


result = 0

for i in range(cols):
    result += seating_chart[i].count('#')


print(result)