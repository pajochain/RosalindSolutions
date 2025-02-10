#! /usr/bin/env python

INPUT="data/rosalind_revc.txt"


def main(INPUT):
    with open(INPUT) as data:
        s = data.read()
        
    sc = ""
    for nt in s:
        if nt == "A":
            sc += "T"
        elif nt == "T":
            sc += "A"
        elif nt == "C":
            sc += "G"
        elif nt == "G":
            sc += "C"
    print(sc[::-1])

if __name__ == "__main__":
    main(INPUT)


