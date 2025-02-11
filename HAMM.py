#! /usr/bin/env python

INPUT="data/rosalind_hamm.txt"

with open(INPUT, 'r') as file:
    lines = file.readlines()
s = lines[0]
t = lines[1]

# Test inputs
# s = "GAGCCTACTAACGGGAT"
# t = "CATCGTAATGACGGCCT"

def hamming_distance(string1, string2):
    distance = 0
    for x, y, in zip(string1, string2):
        if x != y:
            distance += 1
    print(distance)


hamming_distance(s, t)


