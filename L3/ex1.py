#Na+ = 0.0001
#make a function that makes sequences with increasing percentages of C and G
import random as rd
import numpy as np
import matplotlib.pyplot as plt
def temp(seq):
    C = seq.count('C')
    G = seq.count('G')
    A = seq.count('A')
    T = seq.count('T')
    return 4*(G + C) + 2*(A + T)
def seq_maker(seq):
    result = []
    arr = ['G','C']
    while not(seq.count('A') == 0 and seq.count('T') == 0):
        result.append([ letter for letter in seq])
        for i in range(len(seq)):
            if seq[i] == 'A' or seq[i] == 'T':
                seq[i] = arr[rd.randint(0,1)]
                break
    return result

def percentage(seq):
    res = 0
    for letter in seq:
        if letter == "G" or letter == "C":
            res += 1
    return res * len(seq) / 100

sequence = input("Give sequence:")
print(list(sequence))
seqs = seq_maker(list(sequence))
print(seqs)
percentages = [percentage(i) for i in seqs]
temps = [temp(i) for i in seqs]
print(percentages,temps)
percentages = np.array(percentages)
temps = np.array(temps)

plt.plot(temps,percentages)
plt.show()
