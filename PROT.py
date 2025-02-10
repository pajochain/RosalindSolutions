#! /usr/bin/env python

INPUT="data/rosalind_prot.txt"
def main(INPUT):
    with open(INPUT, "r") as data:
        sequence = data.read()

    codon_table = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G', 
    }

    print(f'Sequence length is: {len(sequence)}')

    input = sequence
    n = 3 #for number of nucleotides
    codons = [input[i:i+n] for i in range(0, len(input), n)]
    protein = ""
    for codon in codons:
        if codon in codon_table:
            if codon_table[codon] == 'Stop':
                break
            else:
                    protein += codon_table[codon]
    print(protein)


if __name__ == "__main__":
    main(INPUT)
