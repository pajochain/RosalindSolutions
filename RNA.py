#! /usr/bin/env python

INPUT = "data/rosalind_rna.txt"

def main(text):
    with open(text, "r") as data:
        t = data.read()

    u = t.replace("T", "U")
    print(u)


if __name__ == "__main__":
    main(INPUT)