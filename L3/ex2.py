# TAA TAG TGA // ATG
sequence = input("Enter sequence:")


def groups(seq):
    s = False
    result = []
    i = 0
    while i < len(seq):
        if s:
            result.append(seq[i:i + 3])
            i = i + 3
        if seq[i: i + 3] == "TAA" or seq[i: i + 3] == "TAG" or seq[i: i + 3] == "TGA":
            result.append(seq[i:i + 3])
            break
        if seq[i:i + 3] == "ATG" and not s and i + 3 < len(seq) - 1:
            result.append(seq[i:i + 3])
            i = i + 3
            s = True
    return result

#nu stiu cerinta
print(groups(sequence))
