# AOC 2020, 
# Day 11, Part 2

# Objective: Now instead of counting adjacent seats, count first visible seat in each direction

from day11_part1 import parse_input

seating_chart = []

def find_visible_seats(base_y, base_x):
    global seating_chart

    occupied = 0

    # increments for directions (y, x):
    # up             1  0
    # up-right       1  1
    # right          0  1
    # down-right    -1  1
    # down          -1  0
    # down-left     -1 -1
    # left           0 -1
    # up-left        1 -1
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for direction in directions:
        inc_y = direction[0]
        inc_x = direction[1]
        y = base_y
        x = base_x

        seat_found = False 

        while seat_found == False:
            y += inc_y
            x += inc_x

            if y >= 0 and x >= 0 and y < len(seating_chart) and x < len(seating_chart[0]):
                if seating_chart[y][x] == '#':
                    occupied += 1
                    seat_found = True
                if seating_chart[y][x] == 'L':
                    seat_found = True
            else:
                seat_found = True

    return occupied

def check_seat(y, x):
    global seating_chart

    if seating_chart[y][x] == '.':
        return '.'
    
    occupied = find_visible_seats(y, x)

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
# for i in range(len(seating_chart)):
#     print(''.join(seating_chart[i]))