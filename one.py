
digits = "1234567890"

f = open("one.txt", "r")

inputs = f.readlines()

csum = 0

for line in inputs:
    num = ""
    for c in line:
        if c in digits:
            num += c
            break
    for idx in range(len(line)-1, -1, -1):
        if line[idx] in digits:
            num += line[idx]
            break
    csum += int(num)

print(csum)
