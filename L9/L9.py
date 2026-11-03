from matplotlib import pyplot as plt

with open("sequence.fasta") as file:
    sequence = file.read()

sequence = sequence.replace("\n", "")

enzymes_dic = {('G', 'AATTC'): 0, ('G', 'GATCC'): 0, ('A', 'AGCTT'): 0,
               ('T', 'CGA'): 0, ('GG', 'CC'): 0}

pos = []


def func(seq, key):
    for s in seq:
        begin = None
        for i in range(len(s)):
            if list(key[0]) == list(s[i]) and begin is None:
                begin = i
            if key[1] == s[i:i + len(key[1])] and begin is not None:
                end = i + len(key[1])
                enzymes_dic[key] += 1
                pos.append((begin, end))
                seq.remove(s)
                print(s[:begin], len(s[:begin]))
                print("____")
                print(s[end:], len(s[end:]))
                seq.append(s[:begin])
                seq.append(s[end:])
                break
    return seq


seqs = [sequence]
for k in enzymes_dic.keys():
    seqs = func(seqs, k)


def transform(length):
    return 3000 / length


lengths = [y - x for x, y in pos]
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
print(enzymes_dic)
print(pos)
plt.show()
