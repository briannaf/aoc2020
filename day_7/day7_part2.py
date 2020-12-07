# AOC 2020, 
# Day 7, Part 2

# Objective: How many individual bags does a shiny gold bag ultimately contain?

from day7_part1 import parse_input
import re

def sum_contained_bags(color, bag_rules):
    total = 0

    if color not in bag_rules:
        return 1

    for sub_bag in bag_rules[color]:
        # total += number of bags + (number of bags * the number of bags inside that color)
        total += int(sub_bag[0]) + (int(sub_bag[0]) * int(sum_contained_bags(sub_bag[1], bag_rules)))

    return total

bag_rules_raw = parse_input('input/day7_part1_input.txt')

base_color_regex = re.compile('^(\w+ \w+)')
sub_color_regex = re.compile('(\d+) (\w+ \w+)')

# This dict is dict[bag color] = [list of bag colors it can directly contain, in format (number, color)]
bag_rules = {}

for rule in bag_rules_raw:
    base_color = base_color_regex.search(rule)[0]
    sub_colors = sub_color_regex.findall(rule)

    bag_rules[base_color] = sub_colors

print(bag_rules)

print(sum_contained_bags('shiny gold', bag_rules))