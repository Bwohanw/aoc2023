f = open("three.txt", "r")

lines = f.readlines()



digits = '0123456789'

tempsum = 0

def checksurroundings(idx,rownum, leftmost):
    symbols = digits + '.' + '\n'
    for i in range(max(0, rownum - 1), min(len(lines), rownum+2)):
        for j in range(max(0, idx-1), min(len(lines[rownum]),idx+2)):
            if (lines[i][j] not in symbols):
                return True
    return False

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
        print(num, end=" ")
        print(i, end=" ")
        print(j)
        if (checksurroundings(i, k, True) or checksurroundings(j-1,k, False)):
            tempsum += num



        #print(num)

        i = j
    
print(tempsum)


