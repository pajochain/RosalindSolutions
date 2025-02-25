# #! /usr/bin/env python

ANSWER = input("Open Reading Frames.\nPaste name of dataset (example.txt) in data folder:")
INPUT = f'data\\{ANSWER}'



def parse_fasta(path):
    with open(path, 'r') as file: 
        sequence = ""
        for line in file:
            if ">" not in line: 
                sequence += line
        return sequence.strip()

def to_rna(sequence):
    """
    Converts DNA sequence to RNA
    """
    return sequence.replace("T", "U")

def show_proteins(sequence):
    """
    Requires to_rna(). Given an DNA sequence, returns all possible proteins accounting for start and stop codons. 
    """
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

    proteins = []
    input_rna = to_rna(sequence)
    n = 3 #for number of nucleotides per codon
    for i in range(len(input_rna)):

        if input_rna[i:i+n] == "AUG": # Finds start codon
            # Only keeps codons with length of n declared
            codons = [input_rna[j:j+n] for j in range(i, len(input_rna), n) if len(input_rna[j:j+n]) == n]
            protein = ""

            for codon in codons:  
                    if codon in codon_table:
                        if codon_table[codon] == 'Stop':
                            break
                        else:
                                protein += codon_table[codon]

            # Final check to make sure the last codon is a Stop codon and not just the end of the string
            if codon_table[codon] == "Stop": 
                proteins.append(protein) 
    return proteins

def reverse_complement(sequence):
    """
    Given a DNA sequence, returns its reverse complement.
    """
    sc = ""
    for nt in sequence:
        if nt == "A":
            sc += "T"
        elif nt == "T":
            sc += "A"
        elif nt == "C":
            sc += "G"
        elif nt == "G":
            sc += "C"
    return sc[::-1]

def main():
    sequence = parse_fasta(INPUT)
    fwd = show_proteins(sequence)
    rev = show_proteins(reverse_complement(sequence))
    final_protein_list = fwd + rev
    print("#######  OUTPUT  ######")

    # Only prints unique sequences
    for protein in set(final_protein_list):
        print(protein)


if __name__ == "__main__":
    main()