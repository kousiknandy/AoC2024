import re
import fileinput

acc, enabled = 0, True
mulre = re.compile(r"mul\(([1-9][0-9]{,2}),([1-9][0-9]{,2})\)|do\(\)|don't\(\)")
for line in fileinput.input():
    mat = mulre.finditer(line)
    for m in mat:
        if m.group(0) == "do()":
            enabled = True
            continue
        if m.group(0) == "don't()":
            enabled = False
            continue
        if enabled:
            acc += int(m.group(1)) * int(m.group(2))

print(acc)
