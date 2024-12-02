import fileinput
from collections import Counter

left, right = [], []

for line in fileinput.input():
    l, r, *_ = line.split()
    left.append(int(l))
    right.append(int(r))

counter = Counter(right)
similarity = 0

for l in left:
    similarity += counter[l] * l

print(similarity)
