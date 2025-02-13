#! /usr/bin/env python

INPUT='data/rosalind_gc.txt'


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

                header = line[1:]  # Remove ">"
                sequence_lines = []
            elif line:
                sequence_lines.append(line)
        if header:
             sequences.append((header, "".join(sequence_lines))) # Add the last sequence

    return sequences


def calculate_gc(fasta_list):
    """
     Goes through the list of (header, sequence) tuples, calculates GC content, 
     and prints the header corresponding to the sequence with the highest GC content

    """

    top_header = None
    top_gc = 0.0
    for header, sequence in fasta_list:
        gc_content = (sequence.count("G") + sequence.count("C"))/len(sequence) * 100
        if gc_content > top_gc:
            top_gc = gc_content
            top_header = header

    print(f"{top_header}")
    print(f"{top_gc:.6f}")


def main(INPUT):
    calculate_gc(parse_fasta(INPUT))


if __name__ == "__main__":
    main(INPUT)



