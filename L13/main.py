import random

import numpy as np

mat = [[0.1, 0.3, 0.6], [0.8, 0.1, 0.1], [0.3, 0.3, 0.4]]

initial_vector = [1, 0, 0]


def func(i_vec, m):
    tmp = np.array([[i_vec[0]], [i_vec[1]], [i_vec[2]]])
    for i in range(5):
        tmp = np.matmul(m, tmp)
        print("[", end=" ")
        for e in tmp:
            print(e[0], end=" ")
        print("]")
        print("\n")
    return tmp


def trans_mat(seq):
    letters = []

    for i in seq:
        if not i in letters:
            letters.append(i)
    mat = np.zeros((int(len(letters)), int(len(letters))))
    for i in range(len(seq) - 1):
        if mat[letters.index(seq[i])][letters.index(seq[i + 1])] == 0:
            first = seq[:-1].count(seq[i])
            second = seq.count(''.join(seq[i:i + 2]))
            mat[letters.index(seq[i])][letters.index(seq[i + 1])] = second / first
    return mat, letters


S1 = "AT GC CATG"


def simulate(seq, size):
    m, letters = trans_mat(seq)
    print(m)
    print(letters)
    output = "" + random.choice(letters)
    for _ in range(size):
        index = letters.index(output[-1])
        borcan = []
        for i in range(len(m[index])):
            number = int(m[index][i] * 100)
            if number != 0:
                borcan += list(number * str(letters[i]))
        output += random.choice(borcan)
    return output


print(simulate(S1, 100))
