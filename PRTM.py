#! /usr/bin/env python

# Given: A protein string P
# Return: Total weight of P using monoisotopic mass table

# Sample Data:
# Input: SKADYEK
# Output: 821.392

ANSWER = input("Protein string to weight.\nPaste name of dataset (example.txt) in data folder:")
INPUT = f'data\\{ANSWER}'
MASS_TABLE = "data/mass_table.txt"

def load_mass_table(file_path):
    """Reads a mass table file and returns a dictionary with amino acid masses."""
    mass_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:  # Ensure the line contains two values
                amino_acid, mass = parts
                mass_dict[amino_acid] = float(mass)
    file.close()
    return mass_dict

def calculate_mass(protein_str):
    aa_mass_table = load_mass_table(MASS_TABLE)
    total_mass = 0.0
    for aa in protein_str:
        total_mass += aa_mass_table[aa]
    print(f"{total_mass:.3f}")

def main():
    with open(INPUT, 'r') as file:
        line = file.readline().strip()
    file.close()
    calculate_mass(line)

if __name__ == "__main__":
    main()  








