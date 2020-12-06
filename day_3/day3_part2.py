# AOC 2020, 
# Day 3, Part 2

# Objective: Same as part 1, calculate tree count for R1D1, R3D1, R5D1, R7D1, 
#   and R1D2. Then multiply all results

from day3_part1 import parse_input

tree_map = parse_input('day_3/input/day3_part1_input.txt')
width = len(tree_map[0])

def get_tree_count(right_num, down_num):
    global width
    global tree_map

    tree_count = 0
    horiz_pos = 0

    # use down_num here to control how many vertical lines we move each loop
    for i in range(0, len(tree_map), down_num):
        position_character = tree_map[i][horiz_pos]
        if position_character == '#':
            tree_count += 1

        # and use right_num here to control how many we move to the right 
        #   each loop
        horiz_pos += right_num 
        horiz_pos = horiz_pos % width

    print('Going %s right and %s down collides with %s trees.' % (right_num, down_num, tree_count))
    return tree_count

# slopes are tuples in form (right_num, down_num)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = 1

for item in slopes:
    trees = trees * get_tree_count(item[0], item[1])

print(trees)