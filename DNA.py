#! /usr/bin/env python

INPUT = "data/rosalind_dna.txt"
def main(text):
    with open(text, "r") as data:
        s = data.read()

    A = s.count("A")
    C = s.count("C")
    G = s.count("G")
    T = s.count("T")

    print(f"{A} {C} {G} {T}")


if __name__ == "__main__":
    main(INPUT)