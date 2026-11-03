import matplotlib.pyplot as plt
S = 'CGGACTGATCTATCTAAAAAAAAAAAAAAAAAAAAAAAAAAACGTAGCATCTATCGATCTATCTAGCGATCTATCTACTACG'
l = 30


def CpG(seq):
    percentage = 0
    for base in seq:
        if base == 'C' or base == 'G':
            percentage += 1
    return round(percentage * 100 / len(seq), 2)


print(CpG(S))


def f(x, y):
    if x == y:
        return 1
    else:
        return 0


def KIC(A):
    T = 0
    M = 0
    L = len(A)
    for u in range(1, L):
        for i in range(L - u):
            M += f(A[i], A[u + i])
        T += M / (L - u) * 100
        M = 0
    return round((T / (L - 1)), 2)


print(KIC(S))

x_val = [(CpG(S[i:i + l + 1])) for i in range(len(S) - l)]
y_val = [(KIC(S[i:i + l + 1])) for i in range(len(S) - l)]

plt.scatter(x_val,y_val)
plt.show()

def CoW(x,y):
    return sum(x) / len(x) , sum(y) / len(y)

print(CoW(x_val,y_val))
cow_x, cow_y = CoW(x_val,y_val)
plt.scatter([cow_x],[cow_y])
plt.show()
