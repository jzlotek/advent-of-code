#!/usr/bin/env python3

import itertools
import math
import os
import sys
import re
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d

def isvalid(user):
    if len(user.keys()) == 8 or (len(user.keys()) == 7  and 'cid' not in user):
        return True
    return False

def isvalid2(user):
    if not isvalid(user):
        return False

    byr = int(user['byr'])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(user['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(user['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False

    hgt = user['hgt']
    r = re.compile("[1-9][0-9]+(cm|in)")
    if not r.fullmatch(hgt):
        return False
    if 'cm' in hgt:
        a = int(hgt.strip('cm'))
        if a < 150 or a > 193:
            return False
    elif 'in' in hgt:
        a = int(hgt.strip('in'))
        if a < 59 or a > 76:
            return False

    hcl = user['hcl']
    r = re.compile("#[0-9a-f]{6}")
    if not r.fullmatch(hcl):
        return False

    r = re.compile("(amb|blu|brn|gry|grn|hzl|oth)")
    ecl = user['ecl']
    if not r.fullmatch(ecl):
        return False

    pid = user['pid']
    r = re.compile("[0-9]{9}")
    if not r.fullmatch(pid):
        return False

    return True


if __name__ == "__main__":
    lines = parse_as_str_list()

    users = []
    i = 0
    while i < len(lines):
        user = {}

        while i < len(lines) and lines[i] != "":
            fields = lines[i].split(" ")
            for field in fields:
                a, b = field.split(':')
                user[a] = b
            i += 1
        i += 1
        users.append(user)

    print(len(list(filter(isvalid, users))))
    print(len(list(filter(isvalid2, users))))








