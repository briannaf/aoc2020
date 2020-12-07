# AOC 2020, 
# Day 4, Part 2

# Objective: Validate ids more thoroughly.
#   byr - dddd, 1920-2002 (inclusive)
#   iyr - dddd, 2010-2020
#   eyr - dddd, 2020-2030
#   hgt - d+cm (150-193) OR d+in (59-76)
#   hcl - #[6 chars 0-9 or a-f]
#   ecl - one of following list: amb blu brn gry grn hzl oth
#   pid - ddddddddd (9 digits)
#   cid - ignored

import re
from day4_part_1 import parse_input

birthyear_reg = re.compile('(byr):(\d\d\d\d) ')
issueyear_reg = re.compile('(iyr):(\d\d\d\d) ')
expireyr_reg = re.compile('(eyr):(\d\d\d\d) ')
height_reg = re.compile('(hgt):(\d+)(cm|in) ')
# these 3 don't need further validation
haircolor_reg = re.compile('(hcl):(#[0-9a-f]{6}) ')
eyecolor_reg = re.compile('(ecl):(amb|blu|brn|gry|grn|hzl|oth) ')
pass_id_reg = re.compile('(pid):(\d{9}) ')

regexes = [birthyear_reg, issueyear_reg, expireyr_reg, height_reg, haircolor_reg, eyecolor_reg, pass_id_reg]

def check_id(identification):
    global regexes
    # print(identification)
    for regex in regexes:
        result = regex.search(identification)
        if result == None:
            return False
        elif result[1] == 'byr':
            if int(result[2]) < 1920 or int(result[2]) > 2002:
                return False
        elif result[1] == 'iyr':
            if int(result[2]) < 2010 or int(result[2]) > 2020:
                return False
        elif result[1] == 'eyr':
            if int(result[2]) < 2020 or int(result[2]) > 2030:
                return False
        elif result[1] == 'hgt':
            if result[3] == 'cm':
                if int(result[2]) < 150 or int(result[2]) > 193:
                    return False
            elif result[3] == 'in':
                if int(result[2]) < 59 or int(result[2]) > 76:
                    return False
            else:
                return False
        elif result[1] in ['hcl', 'ecl', 'pid']:
            pass
        else:
            return False

    return True


ids = parse_input('day_4/input/day4_part1_input.txt')
print(len(ids))
count = 0

for item in ids:
    if check_id(str(item)) == True:
        count += 1

print(count)