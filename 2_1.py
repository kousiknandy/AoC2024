import fileinput

safe = 0
for line in fileinput.input():
    levels = [int(l) for l in line.split()]
    if len(levels) == 1:
        safe += 1
        continue

    i = 0
    p, c = levels[i], levels[i+1]
    inc = c > p

    while True:
        if inc and not p+1<=c<=p+3: break
        if not inc and not p-3<=c<=p-1: break
        p = c
        if i >= len(levels)-2:
            safe += 1
            break
        i += 1
        c = levels[i+1]

print(safe)
