#! /usr/bin/env python
INPUT = 'data/rosalind_revp.txt'
# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
# You may return these pairs in any order.
from modules_by_paulo import reverse_complement, parse_fasta


def main(input):
    sequence = parse_fasta(input)[0][1]# Pulls first item in list and second item in tuple

    longest_length = 12
    for length in range(longest_length, 3, -2):
        for i in range(len(sequence) - length + 1):
            if len(sequence[i:i+length]) == length and sequence[i:i+length] == reverse_complement(sequence[i:i+length]): # Checks correct length and reverse complement
                codon = sequence[i:i+length]
                print(i+1, length)

if __name__ == "__main__":
    main(INPUT)