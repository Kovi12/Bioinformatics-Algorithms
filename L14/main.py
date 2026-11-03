import numpy as np
import math


def trans_mat(seq):
    letters = []

    for i in seq:
        if not i in letters:
            letters.append(i)
    mat = np.full((int(len(letters)), int(len(letters))), 0.00000001)
    for i in range(len(seq) - 1):
        if mat[letters.index(seq[i])][letters.index(seq[i + 1])] == 0.00000001:
            first = seq[:-1].count(seq[i])
            second = seq.count(''.join(seq[i:i + 2]))
            res = second / first
            mat[letters.index(seq[i])][letters.index(seq[i + 1])] = res
    return mat, letters


S1 = "ATCGATTCGATATCATACACGTAT"
S2 = "CTCGACTAGTATGAAGTCCACGCTTG"

M1, letters1 = trans_mat(S1)
M2, letters2 = trans_mat(S2)
print(M1)
print(M2)
log_l = np.zeros((len(M1), len(M1[0])))

for i in range(len(M1)):
    for j in range(len(M1[0])):
        log_l[i][j] = math.log2(M1[i][j] / M2[i][j])

print(log_l)

S = "CAGGTTGGAAACGTAA"


def isCpG(seq, l_l, letters, sliding_size):
    score = 0
    for i in range(0, len(seq) - sliding_size):
        window_score = 0
        window = seq[i:sliding_size + i]
        for j in range(len(window) - 1):
            window_score += l_l[letters.index(window[j])][letters.index(window[j + 1])]
        print(f"Sliding window {i}: {window_score}")
        score += window_score
    return score


print(f"Total score is: {isCpG(S, log_l, letters1, 5)}")
