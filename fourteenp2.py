f = open("fourteen.txt", 'r')

lines = f.read().split()

formation = []
for line in lines:
    row = []
    for rock in line:
        row.append(rock)
    formation.append(row)

#print(formation)

lookuptable = {}
#finds the 4 closest '#' marks to the current space in the 4 directions, -1 if it's the edge
# 0 = north, 1 = west, 2 = south, 3 = east

numrow = len(formation)
numcol = len(formation[0])

#setup lookup table for the '#' positions in their respective directions
#the place a stone ends up will be '#' position +- (dep on direction) number of stones in that dir (before the first #) (including that stone)
for row in range(len(formation)):
    for col in range(len(formation[row])):
        ntup = (row, col, 0)
        for i in range(row, -2, -1):
            if (i == -1):
                lookuptable[ntup] = -1
                break
            if (formation[i][col]) == '#':
                lookuptable[ntup] = i
                break
        wtup = (row,col,1)
        for j in range(col, -2, -1):
            if (j == -1):
                lookuptable[wtup] = -1
                break
            if (formation[row][j] == '#'):
                lookuptable[wtup] = j
                break
        stup = (row, col, 2)
        for i in range(row, numrow+1):
            if (i == numrow):
                lookuptable[stup] = numrow
                break
            if (formation[i][col] == '#'):
                lookuptable[stup] = i
                break
        etup = (row, col, 3)
        for j in range(col, numcol + 1):
            if (j == numcol):
                lookuptable[etup] = numcol
                break
            if (formation[row][j] == '#'):
                lookuptable[etup] = j
                break


#track the stone positions, need to change the board afterwards tho 
#this ended up being pretty useless lmao (wanted to use for cycle detection but didn't work for some reason)
stonepositions = []

for row in range(numrow):
    for col in range(numcol):
        if formation[row][col] == 'O':
            stonepositions.append([row,col])

def updateBoard():
    global formation
    global stonepositions
    for row in range(numrow):
        for col in range(numcol):
            if (formation[row][col] == 'O'):
                formation[row][col] = '.'
    for position in stonepositions:
        formation[position[0]][position[1]] = 'O'

#returns number of stones in all 4 directions before a # as a tuple of 4
def countstones(row, col, dir):
    #assumes the row, col is already a valid stone position
    #north
    if (dir == 0):
        count = 0
        rowcount = row
        while (rowcount > -1 and rowcount > lookuptable[(row,col,0)]):
            if (formation[rowcount][col] == 'O'):
                count += 1
            rowcount -= 1
        return count
    #west
    if (dir == 1):
        count = 0
        colcount = col
        while (colcount > -1 and colcount > lookuptable[(row,col,1)]):
            if (formation[row][colcount] == 'O'):
                count += 1
            colcount -= 1
        return count

    #south
    if (dir == 2):
        count = 0
        rowcount = row
        while (rowcount < numrow and rowcount < lookuptable[(row,col,2)]):
            if (formation[rowcount][col] == 'O'):
                count += 1
            rowcount += 1
        return count

    #east
    if (dir == 3):
        count = 0
        colcount = col
        while (colcount < numcol and colcount < lookuptable[(row, col, 3)]):
            if (formation[row][colcount] == 'O'):
                count += 1
            colcount += 1
        return count

    return 0

def cycle():
    global stonepositions
    global formation

    for dir in range(4):
        for i in range(len(stonepositions)):
            startposition = stonepositions[i]
            surroundingstones = countstones(startposition[0],startposition[1], dir)
            if (dir == 0):
                startposition[0] = lookuptable[(startposition[0],startposition[1], 0)] + surroundingstones
            if (dir == 1):
                startposition[1] = lookuptable[(startposition[0],startposition[1], 1)] + surroundingstones
            if (dir == 2):
                startposition[0] = lookuptable[(startposition[0],startposition[1], 2)] - surroundingstones
            if (dir == 3):
                startposition[1] = lookuptable[(startposition[0],startposition[1],3)] -  surroundingstones
        stonepositions[i][0] = startposition[0]
        stonepositions[i][1] = startposition[1]
        updateBoard()





def calcweight():
    weight = 0

    numrows = len(formation)

    for rowctr in range(len(formation)):
        for item in formation[rowctr]:
            if (item == 'O'):
                weight += numrows - rowctr

    return weight

# cycle()
# for i in range(100 - 1):
#     prev = stonepositions
#     cycle()
#     print(calcweight())
#     if (stonepositions == prev):
#         break

#remnants from part 1
def movenorth(startingx, startingy):
    global formation
    if (formation[startingx][startingy] != 'O'):
        return
    while (startingx != 0 and formation[startingx-1][startingy] == '.'):
        formation[startingx][startingy] = '.'
        formation[startingx-1][startingy] = 'O'
        startingx -= 1

def moveallnorth():
    for i in range(numrow):
        for j in range(numcol):
            movenorth(i,j)

# cycle()
# print(formation)
# moveallnorth()
# print(calcweight())
# print(calcweight())

# for i in range(101):
#     prev = [x[:] for x in stonepositions]
#     cycle()
#     if (stonepositions == prev):
#         print(i)
#         calcweight()
#     print(calcweight())

# print(calcweight())

#next implement cycle detection maybe

#for now, manually see what the cycle is ig

def transformtuple():
    toret = ''
    for row in formation:
        for col in row:
            toret += col
    return toret

seen = {}


numcycles = 1000000000

seen[transformtuple()] = numcycles

while numcycles > 0:
    cycle()
    numcycles -= 1
    t = transformtuple()
    if t in seen.keys():
        print("here")
        print(numcycles)
        print(seen[t] - numcycles)
        numcycles %= seen[t] - numcycles
        print(numcycles)
        break
    seen[t] = numcycles

for i in range(numcycles):
    cycle()

print(calcweight())

# while numcycles > 0:
#     cycle()
#     numcycles -= 1
#     t = transformtuple()
#     if t in seen:
#         cyclelen = 0
#         print("seen")
#         # print(numcycles)
#         x = (-1,)* (2*len(stonepositions))
#         while x != t:
#             cycle()
#             numcycles -= 1
#             x = transformtuple()
#             cyclelen += 1
#         print(cyclelen)
#         numcycles %= cyclelen
#         break
#         # print("here")
#         continue
#     else:
#         seen.add(t)

# for i in range(numcycles):
#     cycle()

print(calcweight())

# for numleft in range(numcycles, 0, -1):
#     cycle()
#     t = transformtuple()
#     cyclelen = 0
#     if t in seen:
#         x = (-1,)* (2*len(stonepositions))
#         while x != t:
#             cycle()
#             x = transformtuple()
#             cyclelen += 1
#         numleft = numleft % cyclelen
#     else:
#         seen.add(t)

