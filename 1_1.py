import heapq
import fileinput

left, right = [], []

for line in fileinput.input():
    l, r, *_ = line.split()
    left.append(int(l))
    right.append(int(r))

heapq.heapify(left)
heapq.heapify(right)
dist = 0

while True:
    try:
        l, r = heapq.heappop(left), heapq.heappop(right)
    except IndexError:
        print(dist)
        break
    dist += abs(l-r)
