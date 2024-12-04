import collections
import fileinput
import itertools


def classify(a, b):
    inc = b > a
    if inc:
        bump = a+1<=b<=a+3
    else:
        bump = a-3<=b<=a-1
    return inc,bump

def safe_series(levels, dampner=False):
    cl = [classify(a,b) for a,b in itertools.pairwise(levels)]
    if (all([c[0] for c in cl]) or all([not c[0] for c in cl])) and all([c[1] for c in cl]): return True
    if not dampner: return False
    counter = collections.Counter([c[0] for c in cl])
    if counter[True] >= 2 and counter[False] >= 2: return False
    bumps = [c[1] for c in cl if not c[1]]
    if len(bumps) >= 2: return False
    if counter[True] <= 1:
        for i, c in enumerate(cl):
            if c[0] or not c[1]:
                if safe_series(levels[:i]+levels[i+1:]) or safe_series(levels[:i+1]+levels[i+2:]): return True
    if counter[False] <= 1:
        for i, c in enumerate(cl):
            if not c[0] or not c[1]:
                if safe_series(levels[:i]+levels[i+1:]) or safe_series(levels[:i+1]+levels[i+2:]): return True
    return False

safe = 0
for line in fileinput.input():
    levels = [int(l) for l in line.split()]
    if safe_series(levels, True): safe += 1

print(safe)
