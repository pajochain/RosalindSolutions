
def parse_fasta(INPUT):
    """
    Expects a filepath to fasta file.
    Parses a FASTA file and returns a list of tuples, 
    where each tuple contains the header and sequence as strings.
    """
    sequences = []
    with open(INPUT, 'r') as file:
        header = None
        sequence_lines = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # Checks to make sure header is not a sequence and it is not an empty string
                if header is not None and header != "":
                    # Saves the previous sequence before starting a new one
                    sequences.append((header, "".join(sequence_lines)))

                header = line[1:]  # Removes ">"
                sequence_lines = []
            elif line:
                sequence_lines.append(line)
        if header:
             sequences.append((header, "".join(sequence_lines))) # Adds the last sequence

    return sequences


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



def find_seqs(sequences):
    """Finds the main string and saves substrings into a list. 
    Requires a list of tuples where each tuple has a fasta header and sequence. """
    main_seq = ""
    sub_seqs = []
    for header, sequence in sequences:
        if len(sequence) > len(main_seq):
            main_seq = sequence 

    for header, sequence in sequences:
        if len(sequence) < len(main_seq):
            sub_seqs.append(sequence)

    return main_seq, sub_seqs

def to_exon(main_seq, introns):
    """
    Removes introns from a sequence
    Requires a Main Sequence as a string, and a list of strings of introns.
    Returns exonic sequence
    """
    for intron in introns:
        main_seq = main_seq.replace(intron, "")
    return main_seq