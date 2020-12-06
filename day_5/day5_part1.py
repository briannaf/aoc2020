# AOC 2020, 
# Day 5, Part 1

# Objective: Examine list of boarding passes, find seat highest seat ID 
#   (row * 8 + column) in list. 
# Boarding passes are in binary format
#   FBFBBFFRLR
# F means go to first half, B means go to back half
# Then L and R mean left and right half of the row (for determining column)
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Basically will treat these like binary numbers, because that's what they are.
# And for this part, we just need to find the highest number.

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

def process_pass(pass_string):
    # going to replace F and B with 0 and 1, and L and R with 0 and 1,
    # respectively. This gives us an equivalent binary string
    raw_binary = pass_string.replace('F', '0')
    raw_binary = raw_binary.replace('B', '1')
    raw_binary = raw_binary.replace('L', '0')
    raw_binary = raw_binary.replace('R', '1')

    return int(raw_binary, 2)

passes = parse_input('day_5/input/day5_part1_input.txt')

highest_pass = 0
for item in passes:
    pass_number = process_pass(item)
    if pass_number > highest_pass:
        highest_pass = pass_number

print(highest_pass)