# Let us modify a text S.
# 2. Randomly mutate sequence S such that 1000 variants are generated.These 1000 versions are called children and the original the parent.
# 3 Make a fitness fucntion that is able to check each child for particular desired proprieties such that a maximization is searched for among the 1000
# versions. Thus the function will provide the best fit child for the particular requirements of the medium.
# 4.The best fit child is then used as a parent and the cycle repeats until in the next generations a child is found that meets the fitness requirements.
# The requirements: -the secodn half of the child must contain 80% of letter A; -The first 6 letters of the child must be ABCDAB
import random as rd
from copy import deepcopy

S = "ABDDAACBACDABCAAADBA"
S = list(S)
alphabet = ['A', 'B', 'C', 'D']


def mutate(mutation_rate, sequence):
    mutated_sequence = deepcopy(sequence)
    for i in range(mutation_rate):
        index = rd.randint(0, len(mutated_sequence) - 1)
        mutated_sequence[index] = rd.choice(alphabet)
    return mutated_sequence


def generate_children(parent):
    children = [parent]
    for i in range(1000):
        children.append(mutate(3, parent))
    return children


def fitness_score(sequence):
    score = 0
    if sequence[0:6] == list("ABCDAB"):
        score += 40

    count = 0
    for i in range(int(len(sequence) / 2), len(sequence)):
        if sequence[i] == 'A':
            count += 1
    score += count * 10
    return score


def to_string(s):
    return "".join([str(element) for element in s])


def main_loop(best_child, score):
    if score > 120:
        return best_child, score
    s = "".join([str(element) for element in best_child])
    children_score = {to_string(child): fitness_score(child) for child in generate_children(best_child)}
    children_score[s] = score
    maximum = 0
    new_child = []
    for key, value in children_score.items():
        if value >= maximum:
            maximum = value
            new_child = list(key)

    return main_loop(new_child, maximum)


result_child, result_score = main_loop(S, fitness_score(S))
print("Best child:", result_child)
print("Best score:", result_score)
