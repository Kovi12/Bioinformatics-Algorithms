import numpy as np
import math

str_mat = [list("GAGGTAAAC"),
           list("TCCGTAAGT"),
           list("CAGGTTGGA"),
           list("ACAGTCAGT"),
           list("TAGGTCATT"),
           list("TAGGTACTG"),
           list("ATGGTAACT"),
           list("CAGGTATAC"),
           list("TGTGTGAGT"),
           list("AAGGTAAGT")]

rows = len(str_mat)
cols = len(str_mat[0])

print(str_mat)

count_mat = {'A': np.zeros(cols),
             'C': np.zeros(cols),
             'G': np.zeros(cols),
             'T': np.zeros(cols)}

for y in range(cols):
    for x in range(len(str_mat)):
        count_mat[str_mat[x][y]][y] += 1

print(count_mat)

relative_freq_mat = {k: [x / rows for x in v] for k, v in count_mat.items()}

print(relative_freq_mat)
log_likelihood = {}
try:
    log_likelihood = {k: [math.log(x / 0.25) if x != 0 else 0 for x in v] for k, v in relative_freq_mat.items()}
except:
    pass
print(log_likelihood)

S = "CAGGTTGGAAACGTAATCAGCGATTACGCATGACGTAA"


def score(window, ll):
    res = 0
    for i, let in enumerate(window):
        res += ll[let][i]
    return res


scores = []
for i in range(len(S) - cols):
    scores.append(score(S[i:i + cols], log_likelihood))

print(scores)
