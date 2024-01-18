f = open('ten.txt', 'r')

info = f.read()
lines = info.split()
ROW_LEN = len(lines[0])#its a square LOL


distances = []
visited = []
pipes = []

for i in range(ROW_LEN):
    one = [0] * ROW_LEN
    two = [False] * ROW_LEN
    three = ['.'] * ROW_LEN
    distances.append(one)
    visited.append(two)
    pipes.append(three)


starting = (-1,-1)

for i in range(ROW_LEN):
    for j in range(ROW_LEN):
        pipes[i][j] = lines[i][j]
        if (lines[i][j] == 'S'):
            starting = (i,j)

def inbounds(w):
    x,y = w
    return x < ROW_LEN and x >= 0 and y < ROW_LEN and y >= 0

def findneighbors(w):
    x,y = w
    global pipes
    global visited
    toret = []
    above = (x-1,y)
    below = (x+1,y)
    right = (x,y+1)
    left = (x,y-1)
    if (pipes[x][y] == 'S'):
        if (pipes[x-1][y] == '|' or pipes[x-1][y] == '7' or pipes[x-1][y] == 'F'):
            toret.append(above)
        if (pipes[x+1][y] == '|' or pipes[x+1][y] == 'L' or pipes[x+1][y] == 'J'):
            toret.append(below)
        if (pipes[x][y+1] == '-' or pipes[x][y+1] == 'J' or pipes[x][y+1] == '7'):
            toret.append(right)
        if (pipes[x][y-1] == '-' or pipes[x][y-1] == 'L' or pipes[x][y-1] == 'F'):
            toret.append(left)
        return toret

    if (pipes[x][y] == '|'):
        if (inbounds(above)):
            toret.append(above)
        if (inbounds(below)):
            toret.append(below)
        return toret
    if (pipes[x][y] == '-'):
        if (inbounds(right)):
            toret.append(right)
        if (inbounds(left)):
            toret.append(left)
        return toret
    if (pipes[x][y] == 'L'):
        if (inbounds(above)):
            toret.append(above)
        if (inbounds(right)):
            toret.append(right)
        return toret
    if (pipes[x][y] == 'J'):
        if (inbounds(above)):
            toret.append(above)
        if (inbounds(left)):
            toret.append(left)
        return toret
    if (pipes[x][y] == '7'):
        if (inbounds(left)):
            toret.append(left)
        if (inbounds(below)):
            toret.append(below)
        return toret
    if (pipes[x][y] ==  'F'):
        if (inbounds(below)):
            toret.append(below)
        if (inbounds(right)):
            toret.append(right)
        return toret
    if (pipes[x][y] == '.'):
        return toret

def bfs():
    global starting
    global distances
    global visited
    q = []
    x,y = starting
    visited[x][y] = True
    q.append(starting)
    while (len(q) != 0):
        w = q.pop(0)
        neighbors = findneighbors(w)
        for neighbor in neighbors:
            x,y = neighbor
            if (not visited[x][y]):
                distances[x][y] = distances[w[0]][w[1]] + 1
                visited[x][y] = True
                q.append(neighbor)


bfs()



maximum = 0
for row in distances:
    for col in row:
        if col > maximum:
            maximum = col

print(maximum)

