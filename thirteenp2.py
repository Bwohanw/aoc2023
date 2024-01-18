import numpy as np

f = open("thirteen.txt",'r')

puzzles = f.read().split("\n\n")


for x in range(len(puzzles)):
    lines = puzzles[x].split()
    A = np.zeros((len(lines),len(lines[0])), dtype=np.int64)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            A[i][j] = 1 if lines[i][j] == '#' else 0
    puzzles[x] = A

print(puzzles[0])


def arrdiff(num1, num2, shiftcount):
    count = 0
    for i in range(shiftcount+2):
        # print(num1)
        # print(num2)
        if (num1%2 != num2%2):
            count += 1
        num1 = num1 >> 1
        num2 = num2 >> 1
    return count

#finds any horizontal lines of mirroring
#we look left->right and then right->left
#because one of the endpoints must match with a corresponding line on the other side of the mirror
#or be off by one in part 2
#use transpose to look at the vertical lines of mirroring
def findhorizreflection(array):
    columns = []
    shiftcount = 0
    for col in range(np.shape(array)[1]):
        cnum = 0
        counter = 0
        for row in range(np.shape(array)[0]):
            cnum = cnum << 1
            counter += 1
            cnum += array[row][col]
        shiftcount = counter
        columns.append(cnum)
    print(columns)
    toret = -1 #the number of columns to the left of the line
    n = len(columns)
    for i in range(n):
        if (arrdiff(columns[i],columns[-1], shiftcount) <= 1 and ((n-i) % 2 == 0)):
            if (i == n-1):
                break
            midptsteps = (n-i) // 2
            diffcounter = 0
            for j in range(midptsteps):
                diffcounter += arrdiff(columns[i + j],columns[n-1-j],shiftcount)
            if (diffcounter != 1):
                continue
            else:
                toret = i + midptsteps

    for i in range(n-1,-1,-1):
        if (arrdiff(columns[i],columns[0], shiftcount) <= 1 and ((i) % 2 == 1)):
            if (i == 0):
                break
            midptsteps = (i+1)//2
            diffcounter = 0
            for j in range(midptsteps):
                diffcounter += arrdiff(columns[i-j],columns[j],shiftcount)
            if (diffcounter != 1):
                continue
            else:
                toret = midptsteps
    return toret



print(findhorizreflection(puzzles[0].T))
#print(findhorizreflection(puzzles[1].T))

total = 0
for puzzle in puzzles:
    horizres = findhorizreflection(puzzle)
    colres = findhorizreflection(puzzle.T)
    if (horizres != -1 and colres != -1):
        print("fuck")
    if (horizres == -1 and colres == -1):
        print("extra fuck")
    if (horizres == -1):
        total += 100*colres
    else:
        total += horizres

print(total)

