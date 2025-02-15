#! /usr/bin/env python

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# Sample data

# t = 'GATATATGCATATACTT'
# s = 'ATAT'


ANSWER = input("Paste name of dataset (example.txt) in C:\\Users\\tanic\\MLProjects\\RosalindSolutions\\data:")
INPUT = f'C:\\Users\\tanic\\MLProjects\\RosalindSolutions\\data\\{ANSWER}'

def slice_and_check(string, substring):
    """
    Slices string to same lengths as substring. 
    Checks each slice to see if it matches substring.
    If match, checks and saves where the slice started.
    """
    if INPUT: print(f"{ANSWER} found")
    else: print(f"{ANSWER} not found.")
    s_length = len(substring.strip())
    locations = []
    for i in range(len(string)-s_length):
        if string[i:i+s_length].strip() == substring.strip():
            # printed position/idex should not start from 0
            locations.append(str(i+1)) 
    return " ".join(locations)    


def main(text):
    """
    Assigns which is string and substring based on length
    """
    with open(INPUT, 'r') as file:
        lines = file.readlines()
    if lines[0] > lines[1]:
        string = lines[0]
        substring = lines[1]
    else:
        string = lines[1]
        substring = lines[0]

    return slice_and_check(string, substring)


if __name__ == "__main__":
    output = main(INPUT)
    print(output)



