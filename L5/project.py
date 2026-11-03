# minimum 8
# le iei din doua parti, prima oara verific daca se suprapune din partea stanga si a doua din partea dreapta
import random

size = 2000
with open("sequence.fasta") as file:
    sequence = file.read()[:size]

sequence = sequence.replace("\n", "")

samples = []
for i in range(0, size):
    r1 = random.randint(100, 150)
    r2 = random.randint(0, size - r1 - 1)
    samples.append(sequence[r2:r2 + r1])

new_sequence = samples[0]
minimum = 8


def check1(org, right):
    res = 0
    change = False
    for i in range(minimum, min(len(org), len(right))):
        if org[len(org) - i:] == right[:i]: ## ab,cdef cdef,abc
            res = i
            change = True
            break
    if res == 0:
        return org, change

    return org + right[res:], change


def check2(left, org):
    res = 0
    for i in range(minimum, min(len(left), len(org))):
        if left[len(left) - i:] == org[:i]:
            res = i
            break
    if res == 0:
        return org
    return left + org[res:]


def update(new):
    for s in samples:
        if new is s or s in new:
            continue
        if len(new) > size:
            break
        aux, change = check1(new, s)
        if not change:
            aux = check2(s, new)
        new = aux
    return new


while len(new_sequence) < size:
    print(new_sequence,0)
    new_sequence = update(new_sequence)

percentage = 0
i = 0
while i < min(len(new_sequence), len(sequence)):
    if new_sequence[i] == sequence[i]:
        percentage += 1
    i += 1
print(percentage / size * 100)
print(new_sequence)
print(sequence)
