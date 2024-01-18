
digits = {"one" : 1, "two" : 2, "three" :3 , "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "zero" : 0}

otherdigits = "1234567890"

f = open("one.txt", "r")

inputs = f.readlines()

csum = 0

for line in inputs:
    num = 0
    flag = False
    for idx in range(0, len(line)):
        if (line[idx] in otherdigits):
            num += int(line[idx])*10
            flag = True
            break
        for diff in range(2, 6):
            endidx = idx + diff
            if (endidx >= len(line)):
                endidx = len(line)
            if (line[idx:endidx] in digits.keys()):
                num += digits[line[idx:endidx]] * 10
                flag = True
                break
        if (flag):
            break
    flag = False
    for idx in range(len(line) - 1, -1, -1):
        if (line[idx] in otherdigits):
            num += int(line[idx])
            flag = True
            break
        for diff in range(2, 6):
            endidx = idx + diff
            if (endidx >= len(line)):
                endidx = len(line)
            if (line[idx:endidx] in digits.keys()):
                num += digits[line[idx:endidx]]
                flag = True
                break
        if (flag):
            break
    csum += num

print(csum)
