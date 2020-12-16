# AOC 2020, 
# Day 13, Part 1

# Objective: Input is 2 lines -- line one is the timestamp you will be at the 
#   port and ready to board any available buses. Line 2 is the bus schedules. 
# The ID # of the bus is the interval in minutes that it arrives back at the 
#   port (so ID 5 means the bus will be there at 0, 5, 10, so on). An x for
#   the id # means the bus is out of service.

# What is the ID of the earliest bus you can catch multiplied by the number of 
#   minutes you'll need to wait?

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

temp = parse_input('day_13/input/day13_part1_input.txt')

timestamp = int(temp[0])

buses = temp[1].split(',')
buses = [int(x) for x in buses if x != 'x']

min_time = timestamp * 2
min_bus_id = 0

for i in buses:
    bus_arrival_time = (timestamp // i + 1) * i

    if bus_arrival_time < min_time:
        min_time = bus_arrival_time
        min_bus_id = i

print(min_bus_id, min_time - timestamp, min_bus_id * (min_time - timestamp))