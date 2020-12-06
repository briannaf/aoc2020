# AOC 2020, 
# Day 3, Part 1

# Objective: Trees follow a map like this:
#    ..##.......
#    #...#...#..
#    .#....#..#.
#    ..#.#...#.#
#    .#...##..#.
#    ..#.##.....
#    .#.#.#....#
#    .#........#
#    #.##...#...
#    #...##....#
#    .#..#...#.#

# And this map repeats to the right infinitely
# Starting at the top-left, how many trees would you hit if you went at a slope of right 3 down 1?

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
            # remove trailing newline
            input_array.append(temp.rstrip())

        return input_array
    except Exception as e:
        print(e)
        return None

tree_map = parse_input('day_3/input/day3_part1_input.txt')

width = len(tree_map[0])
horiz_pos = 0
tree_count = 0

for i in tree_map:
    position_character = i[horiz_pos]
    if position_character == '#':
        tree_count += 1
    
    #before next iteration, update horizontal position. Deal with how it wraps when the map repeats by doing modulus width of map
    horiz_pos += 3
    horiz_pos = horiz_pos % width

print(tree_count)