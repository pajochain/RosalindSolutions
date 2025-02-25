#! /usr/bin/env python


INPUT="data/rosalind_tran.txt"


def parse_fasta(INPUT):
    """
    
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


def transitions_transversions(string1, string2):
    transitions = 0
    transversions = 0
    for x, y, in zip(string1, string2):
        if x != y: 
            if (x == "A" and y == "G") or (x == "G" and y == "A") or (x == "C" and y == "T") or (x == "T" and y == "C"):
                transitions += 1
            else:
                transversions += 1
    ratio = transitions/transversions

    return ratio

def main():
    sequences = parse_fasta(INPUT)
    seq1 = sequences[0][1]
    seq2 = sequences[1][1]

    return transitions_transversions(seq1,seq2)


if __name__ == "__main__":
    print(main())