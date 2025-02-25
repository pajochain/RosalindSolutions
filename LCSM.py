#! /usr/bin/env python

from modules_by_paulo import parse_fasta

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

INPUT = 'data/rosalind_lcsm.txt'

def longest_common_substring(strings):
    # Finds the shortest sequence and starts finding substrings from there
    shortest_string = min(strings, key=len)
    
    # Gradually reduces the length of the shortest sequence
    for length in range(len(shortest_string), 0, -1):
        for i in range(len(shortest_string) - length + 1):
            substring = shortest_string[i:i + length]
            # Checks if every string  in strings contains the substring
            if all(substring in string for string in strings): # returns True if substring is in each string in strings list. 
                return substring

### Testing it
# shortest_string = 'ABABABBA'
# for length in range(len(shortest_string), 0, -1):
#     for i in range(len(shortest_string) - length + 1):
#         print(i, length)
#         substring = shortest_string[i:i + length]
#         print(substring)

def main():
    headers_w_sequences = parse_fasta(INPUT)
    sequences_only = []
    for header, sequence in headers_w_sequences:
        sequences_only.append(sequence)

    print(longest_common_substring(sequences_only))

if __name__ == "__main__":
    main()