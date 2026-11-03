import numpy as np
from matplotlib import pyplot as plt

GAP = -2
MATCH = 2
MISMATCH = -1
col = list("ACCGTGAAGCCAATAC")
row = list("AGCGTGCAGCCAATAC")
matrix = np.zeros((len(col) + 1, len(row) + 1))
trace = np.zeros((len(col) + 1, len(row) + 1))

for x in range(len(row) + 1):
    matrix[0][x] = GAP * x

for x in range(len(col) + 1):
    matrix[x][0] = GAP * x


def s_func(i, j, c, r):
    if c[i - 1] == r[j - 1]:
        return MATCH
    return MISMATCH


def D_max(a, b, c):
    max_number = max(a, b, c)

    if max_number == a:
        return a

    elif max_number == b:
        return b

    else:
        return c


def get_score_mat(mat, c, r):
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            s = s_func(i, j, c, r)
            a = mat[i - 1][j - 1] + s
            b = mat[i - 1][j] + GAP
            y = mat[i][j - 1] + GAP
            mat[i][j] = D_max(a, b, y)
    return mat


get_score_mat(matrix, col, row)


def best_alignment(mat, tr, c, r):
    alignment_A = ""
    alignment_B = ""
    i = len(mat) - 1
    j = len(mat[0]) - 1
    while i >= 1 or j >= 1:

        if i >= 1 and j >= 1 and mat[i][j] == mat[i - 1][j - 1] + s_func(i, j, c, r):
            tr[i][j] = mat[i][j]
            alignment_A += c[i - 1]
            alignment_B += r[j - 1]
            i -= 1
            j -= 1
        elif i >= 1 and mat[i][j] == mat[i - 1][j] + GAP:
            tr[i][j] = mat[i][j]
            alignment_A += c[i - 1]
            alignment_B += '_'
            i -= 1
        elif j >= 1 and mat[i][j] == mat[i][j - 1] + GAP:
            tr[i][j] = mat[i][j]
            alignment_A += '_'
            alignment_B += r[j - 1]
            j -= 1
    tr[0][0] = 1
    return alignment_A[::-1], alignment_B[::-1]


A, B = best_alignment(matrix, trace, col, row)
print(f"AlignmentA = {A}")
print(f"AlignmentB = {B}")

plt.figure(figsize=(10, 6))
plt.imshow(matrix, cmap='viridis', aspect='auto')
plt.colorbar(label='Score')
plt.title('Scoring Matrix Heatmap')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()

trace_binary = np.where(trace != 0, 1, 0)

plt.figure(figsize=(10, 6))
plt.imshow(trace_binary, cmap='viridis', aspect='auto', vmin=0, vmax=1)
plt.title('Trace Matrix Heatmap')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()
