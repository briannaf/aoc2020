# AOC 2020, 
# Day 10, Part 1

# Objective: 

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