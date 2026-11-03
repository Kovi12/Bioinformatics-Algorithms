import random

seq = []
bases = ['A', 'C', 'G', 'T']
for _ in range(400):
    seq.append(random.choice(bases))

transposons = []
for _ in range(3):
    trs = []
    for _ in range(8):
        trs.append(random.choice(bases))
    transposons.append(trs)


def insert(beg, end, s, t):
    for i in range(8):
        s[beg + i] = t[i]
        s[end - i - 1] = t[i]


insert(4, 350, seq, transposons[0])
insert(100, 200, seq, transposons[1])
insert(250, 380, seq, transposons[2])

def find_transp_elems(sequence, transps):
    pos = []
    for t in transps:
        begin = -1
        for i in range(len(sequence)):
            if sequence[i:i + 8] == t[::-1] and begin != -1:
                end = i
                pos.append((begin, end))
                break
            if sequence[i:i + 8] == t:
                begin = i + 8
                i += 8
    return pos


positions = find_transp_elems(seq, transposons)
for p in positions:
    print("Begin: {b}, End: {e}, Transposon {t}".format(b=p[0], e=p[1], t=seq[p[0]:p[1]]))
