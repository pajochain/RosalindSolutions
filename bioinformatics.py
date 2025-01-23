
# This function will calculate the GC content of a string. 
sequence = 'ATGCGGGCGAGCGTTTCGGAGGGTATTTATTATCTTTCTATCATTTTTTAGGGGAGGATTTTAGGGGATTATCTCTCGATCGATTATCGATC'

def calc(sequence):
    total = len(sequence)
    print(f'The GC content of the sequence is {( sequence.count("G") + sequence.count("C") ) / total * 100 :.2f} %')

calc(sequence)