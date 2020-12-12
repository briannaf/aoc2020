# AOC 2020, 
# Day 10, Part 1

# Objective: Each entry in the input list is the "joltage" of a power adapter you posess. Each adapter can take 1, 2, or 3 jolts lower than its rating and still work (and of course the same rating works). Treat the carging outlet as 0 jolts and your device to charfe as being rated for 3 volts higher than the highest-rated adapter in your bag. If you use every adapter at once, what is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

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

joltages = parse_input('day_10/input/day10_part1_input.txt')
joltages.sort()

current_joltage = 0
differences = []

for i in joltages:
    differences.append(i - current_joltage)
    current_joltage = i

print(differences.count(1) * (differences.count(3) + 1))