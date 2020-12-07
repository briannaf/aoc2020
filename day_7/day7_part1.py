# AOC 2020, 
# Day 7, Part 1

# Objective: Input is list of rules on what different colored bags must contain. How many bag colors are there that can ultimately (so directly or indirectly though chaining) contain a shiny gold bag?

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

def get_containing_bags_recursive(bag_color, bag_rules_reverse):
    containing_bags = bag_rules_reverse[bag_color]
    indirect_containers = bag_rules_reverse[bag_color]

    if containing_bags == []:
        return []

    for color in containing_bags:
        indirect_containers = indirect_containers + get_containing_bags_recursive(color, bag_rules_reverse)

    return indirect_containers


bag_rules_raw = parse_input('input/day7_part1_input.txt')

color_finding_regex = re.compile('(\w+ \w+) bag')

# This dict is dict[bag color] = [list of bag colors it can directly contain]
bag_rules = {}
# This dict is dict[bag color] = [list of bag colors that can directly contain it]
bag_rules_reverse = {}

for rule in bag_rules_raw:
    matches = color_finding_regex.findall(rule)
    bag_rules[matches[0]] = matches[1:]
    for color in matches[1:]:
        # don't have to have this if-statement in the previous array because each bag only has 1 list of allowed contents, but it's not 1:1 when it's reversed
        if color in bag_rules_reverse:
            bag_rules_reverse[color].append(matches[0])
        else:
            bag_rules_reverse[color] = [matches[0]]
        if matches[0] not in bag_rules_reverse:
            bag_rules_reverse[matches[0]] = []

result = get_containing_bags_recursive('shiny gold', bag_rules_reverse)
# get rid of duplicates
result = set(result)
print(len(result))