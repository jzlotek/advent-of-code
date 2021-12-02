#!/usr/bin/env python3

import itertools
import math
import os
import sys
sys.path.append('../..')

from util.parsing import parse_list, parse_as_str_list, parse_as_str, parse_list2d


if __name__ == "__main__":
    lines = parse_as_str_list()

    mapping = {}
    stripped_lines = []
    for line in lines:
        split = line.split('(')
        ingred, allergens = split[0].strip().split(), split[1].strip(')').strip().split()[1:]
        for allergen in allergens:
            mapping.setdefault(allergen.strip(', '), []).append(set(ingred))
        stripped_lines.append(set(ingred))


    allergen_map = {}

    for allergen, ingredients in mapping.items():
        ingred = set()
        for idx, ingred_list in enumerate(ingredients):
            if idx == 0:
                ingred = ingred_list
            ingred = ingred & ingred_list

        allergen_map[allergen] = ingred



    # part 1
    inert = set()
    s = 0
    for line in stripped_lines:
        l = line
        for allergens in allergen_map.values():
            l -= allergens
        s += len(l)
        inert = inert.union(l)


    # part 2
    for allergen in sorted(allergen_map.keys()):
        allergen_map[allergen] -= inert

    changes = True
    while changes:
        # strip out the ones that match
        # assume that the allergen: ingredients
        # where len(ingred) == 1 is a match so strip them out for every other allergen
        changes = False
        for allergen in sorted(allergen_map.keys()):
            allergens = allergen_map[allergen]
            if len(allergens) != 1:
                continue
            for other, ingreds in allergen_map.items():
                if other == allergen:
                    continue

                new_ingred = ingreds - allergens
                if len(new_ingred) != len(ingreds):
                    changes = True
                allergen_map[other] = new_ingred

    dangerous = []
    for allergen in sorted(allergen_map.keys()):
        dangerous.extend(allergen_map[allergen])

    print(s)
    print(','.join(dangerous))


