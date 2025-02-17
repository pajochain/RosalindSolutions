#! /usr/bin/env python

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns.
# All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. 
# (Note: Only one solution will exist for the dataset provided.)

from modules_by_paulo import parse_fasta, show_proteins, find_seqs, to_exon

ANSWER = input("RNA Splicing.\nPaste name of dataset (example.txt) in data folder:")
INPUT = f'data\\{ANSWER}'

def main():
    sequences = parse_fasta(INPUT) 
    main_seq, introns = find_seqs(sequences)
    exon = to_exon(main_seq, introns)
    protein = show_proteins(exon)
    # Problem only requires the first protein translated
    print(protein[0])


if __name__ == "__main__":
    main()