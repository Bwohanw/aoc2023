f = open('sixteen.txt', 'r')

info = f.read().splitlines()
grid = []

visited = []

for line in info:
    row = []
    visit = [False] * len(line)
    for char in line:
        row.append(char)
    grid.append(row)
    visited.append(visit)

# print(grid)

def resetvisit():
    global visited
    visited = []
    for line in info:
        visit = [False] * len(line)
        visited.append(visit)



numrows = len(grid)
numcols = len(grid[0])

#direction: (0,1) = right, (1,0) = down, (0,-1) = left, (-1,0) = up
#this one doesnt work for some reason (fixed: had some issues with negative indices)
#still stack overflows (with good reason)
def move(row=0, col=0, dir = (0,1)):
    if (row >= numrows or col >= numcols or row < 0 or col < 0):
        return
    if ((grid[row][col] == '|' or grid[row][col] == '-') and visited[row][col]):
        return
    visited[row][col] = True
    c = grid[row][col]
    if (c == '.'):
        move(row + dir[0], col + dir[1], dir)
        return
    if (c == '/'):
        move(row - dir[1], col - dir[0], (-dir[1],-dir[0]))
        return
    if (c == '\\'):
        move(row + dir[1], col + dir[0], (dir[1],dir[0]))
        return
    if (c == '-'):
        if (dir[0] == 0):
            move(row, col + dir[1], dir)
            return
        move(row, col + 1, (0,1))
        move(row, col-1, (0,-1))
        return
    if (c == '|'):
        if (dir[1] == 0):
            move(row + dir[0], col, dir)
            return
        move(row + 1, col, (1,0))
        move(row-1, col, (-1,0))
        return
    print('fuck')


def move2(startrow = 0, startcol = 0, dir = (0,1)):
    if (startrow >= numrows or startcol >= numcols or startrow < 0 or startcol < 0):
        return
    while True:
        if (startrow >= numrows or startcol >= numcols or startrow < 0 or startcol < 0):
            return
        if ((grid[startrow][startcol] == '|' or grid[startrow][startcol] == '-') and visited[startrow][startcol]):
                break
        visited[startrow][startcol] = True
        c = grid[startrow][startcol]
        if (c == '.'):
            startrow += dir[0]
            startcol += dir[1]
            continue
        if (c == '/'):
            startrow -= dir[1]
            startcol -= dir[0]
            dir = (-dir[1],-dir[0])
            continue
        if (c == '\\'):
            startrow += dir[1]
            startcol += dir[0]
            dir = (dir[1],dir[0])
            continue
        if (c == '-'):
            if (dir[0] == 0):
                startcol += dir[1]
                continue
            move2(startrow, startcol + 1, (0,1))
            move2(startrow, startcol-1, (0,-1))
            return
        if (c == '|'):
            if (dir[1] == 0):
                startrow += dir[0]
                continue
            move2(startrow + 1, startcol, (1,0))
            move2(startrow-1, startcol, (-1,0))
            return

def moveiter(startrow = 0, startcol = 0, dir = (0,1)):
    threads = [(startrow,startcol,dir)]
    while (len(threads) != 0):
        startrow, startcol, dir = threads.pop(0)
        while True:
            if (startrow >= numrows or startcol >= numcols or startrow < 0 or startcol < 0):
                break
            if ((grid[startrow][startcol] == '|' or grid[startrow][startcol] == '-') and visited[startrow][startcol]):
                break
            visited[startrow][startcol] = True
            c = grid[startrow][startcol]
            if (c == '.'):
                startrow += dir[0]
                startcol += dir[1]
                continue
            elif (c == '/'):
                startrow -= dir[1]
                startcol -= dir[0]
                dir = (-dir[1],-dir[0])
                continue
            elif (c == '\\'):
                startrow += dir[1]
                startcol += dir[0]
                dir = (dir[1],dir[0])
                continue
            elif (c == '-'):
                if (dir[0] == 0):
                    startcol += dir[1]
                    continue
                else:
                    threads.append((startrow, startcol + 1, (0,1)))
                    threads.append((startrow, startcol-1, (0,-1)))
                    break
            elif (c == '|'):
                if (dir[1] == 0):
                    startrow += dir[0]
                    continue
                else:
                    threads.append((startrow + 1, startcol, (1,0)))
                    threads.append((startrow-1, startcol, (-1,0)))
                    break

moveiter()

count = 0
for row in visited:
    print(row)
    for elem in row:
        if elem:
            count += 1
print(count)

    


