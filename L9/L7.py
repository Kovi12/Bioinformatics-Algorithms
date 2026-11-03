import random
import matplotlib.pyplot as plt

size = 2000
with open("sequence.fasta") as file:
    sequence = file.read()[:size]

sequence = sequence.replace("\n", "")

samples = []
for i in range(0, 10):
    r1 = random.randint(100, size)
    r2 = random.randint(0, size - r1 - 1)
    samples.append(sequence[r2:r2 + r1])

def transform(length):
    return 3000 / length

lengths = [len(x) for x in samples]
distances = [transform(x) for x in lengths]

fig, ax = plt.subplots()

ax.plot([0, 0], [0, max(distances)], color='blue', linestyle='-', linewidth=10)

dot_size = 50
for distance, length in zip(distances, lengths):
    ax.plot([0, 1], [distance, distance], color='red', linewidth=2)
    ax.text(0.02, distance, length, fontsize=12, color='black', va='center')

ax.set_ylim(0, max(distances))

ax.set_ylabel("Distance")
ax.set_title("Electrophoresis")
ax.legend()

ax.set_xticks([])

plt.show()
