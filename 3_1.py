import re
import fileinput

acc = 0
mulre = re.compile(r"mul\(([1-9][0-9]{,2}),([1-9][0-9]{,2})\)")
for line in fileinput.input():
    mat = mulre.finditer(line)
    for m in mat:
        acc += int(m.group(1)) * int(m.group(2))

print(acc)
