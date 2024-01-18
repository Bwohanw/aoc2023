f = open("three.txt", "r")

lines = f.readlines()



digits = '0123456789'

digitlocs = set()
digtoint = {}

for k in range(len(lines)):
    line = lines[k]
    i = 0
    while i < len(line):
        if (line[i] not in digits):
            i += 1
            continue

        endidx = i
        for j in range(i, len(line)):
            if (line[j] in digits):
                endidx = j + 1
            else:
                break
        
        num = int(line[i:j])
        
        digitlocs.add(tuple((i,k)))
        digitlocs.add(tuple((j-1,k)))

        digtoint[tuple((i,k))] = num
        digtoint[tuple((j-1,k))] = num



        #print(num)

        i = j

tempsum = 0

for k in range(len(lines)):
    line = lines[k]
    for m in range(len(line)):
        if line[m] != '*':
            continue
        c12 = set()

        for i in range(max(0, k-1), min(len(lines), k+2)):
            for j in range(max(0, m-1), min(len(line), m+2)):
                key = tuple((j, i))
                if key in digitlocs:
                    c12.add(digtoint[key])
        if (len(c12) == 2):
            print(c12)
            temp = 1
            for elem in c12:
                temp *= elem
            tempsum += temp

print(tempsum)
