f = open("twentyone.txt", "r")

info = f.read().split()

numrows = len(info)
numcols = len(info[0])


NUM_STEPS = 64

grid = []
for line in info:
    row = []
    for c in line:
        row.append(c)
    grid.append(row)

def printgrid(grid):
    for line in grid:
        print(line)

printgrid(grid)

startingrow = numrows//2
startingcol = numcols//2

print(grid[startingrow][startingcol])

queue = [(startingrow, startingcol, 0)]

counter = 0

seen = set()

while (len(queue) != 0):
    elem = queue.pop(0)
    rownum = elem[0]
    colnum = elem[1]
    numsteps = elem[2]
    if elem in seen:
        continue
    else:
        seen.add(elem)
    if (numsteps > NUM_STEPS):
        break
    if (numsteps == NUM_STEPS):
        if ((rownum, colnum) not in seen):
            counter += 1
    for i in [-1,1]:
        potenrow = rownum + i
        potencol = colnum
        if potenrow >= 0 and potenrow < numrows and potencol >= 0 and potencol < numcols:
            if grid[potenrow][potencol] == '.' or grid[potenrow][potencol] == 'S':
                queue.append((potenrow, potencol, numsteps + 1))
        potenrow = rownum
        potencol = colnum + i
        if potenrow >= 0 and potenrow < numrows and potencol >= 0 and potencol < numcols:
            if grid[potenrow][potencol] == '.' or grid[potenrow][potencol] == 'S':
                queue.append((potenrow, potencol, numsteps + 1))

print(counter)



