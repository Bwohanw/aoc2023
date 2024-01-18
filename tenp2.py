f = open('ten.txt', 'r')

info = f.read()
lines = info.split()
COL_LEN = len(lines[0])#its a square LOL
ROW_LEN = len(lines)


distances = []
visited = []
pipes = []

for i in range(ROW_LEN):
    one = [0] * COL_LEN
    two = [False] * COL_LEN
    three = ['.'] * COL_LEN
    distances.append(one)
    visited.append(two)
    pipes.append(three)


starting = (-1,-1)

for i in range(ROW_LEN):
    for j in range(COL_LEN):
        pipes[i][j] = lines[i][j]
        if (lines[i][j] == 'S'):
            starting = (i,j)
pipes[starting[0]][starting[1]] = 'L'#change S to what it actually is

def inbounds(w):
    x,y = w
    return x < ROW_LEN and x >= 0 and y < COL_LEN and y >= 0

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

def bfs(w):
    count = 1
    global distances
    global visited
    q = []
    x,y = w
    visited[x][y] = True
    q.append(w)
    while (len(q) != 0):
        w = q.pop(0)
        neighbors = findneighbors(w)
        for neighbor in neighbors:
            x,y = neighbor
            if (not visited[x][y]):
                count += 1
                distances[x][y] = distances[w[0]][w[1]] + 1
                visited[x][y] = True
                q.append(neighbor)
    return count

def bfsperiod(w):
    global visited
    global pipes
    q = []
    x,y = w
    visited[x][y] = True
    q.append(w)
    while (len(q) != 0):
        w = q.pop(0)
        x,y = w
        above = (x-1,y)
        below = (x+1,y)
        right = (x,y+1)
        left = (x,y-1)
        neighbors = []
        if (inbounds(above) and not visited[above[0]][above[1]] and pipes[above[0]][above[1]] == '.'):
            neighbors.append(above)
        if (inbounds(below) and not visited[below[0]][below[1]] and pipes[below[0]][below[1]] == '.'):
            neighbors.append(below)
        if (inbounds(left) and not visited[left[0]][left[1]] and pipes[left[0]][left[1]] == '.'):
            neighbors.append(left)
        if (inbounds(right) and not visited[right[0]][right[1]] and pipes[right[0]][right[1]] == '.'):
            neighbors.append(right)
        for neighbor in neighbors:
            visited[neighbor[0]][neighbor[1]] = True
            q.append(neighbor)
    


bfs(starting)

counter = 0



symbols = 'FLJ7'

for i in range(ROW_LEN):
    inBorder = False
    prevshape = ''
    for j in range(COL_LEN):
        if (visited[i][j]):
            if (pipes[i][j] in symbols):
                if (prevshape == ''):
                    prevshape = pipes[i][j]
                    continue
                elif ((prevshape == 'F' and pipes[i][j] == 'J') or (prevshape == 'J' and pipes[i][j] == 'F')):
                    prevshape = ''
                    inBorder = not inBorder
                elif ((prevshape == 'L' and pipes[i][j] == '7') or (prevshape == '7' and pipes[i][j] == 'L')):
                    prevshape = ''
                    inBorder = not inBorder
                else:
                    prevshape = ''
            if (pipes[i][j] == '|'):
                inBorder = not inBorder
        else:
            if inBorder:
                counter += 1

print(counter)


# # bfsperiod((0,19))
# # print(visited)

# count = 0
# for i in range(ROW_LEN):
#     if pipes[i][0] == '.':
#         bfsperiod((i,0))
#     if pipes[i][COL_LEN-1] == '.':
#         bfsperiod((i,COL_LEN-1))

# for j in range(COL_LEN):
#     if (pipes[0][j] == '.'):
#         bfsperiod((0,j))
#     if (pipes[ROW_LEN-1][j] == '.'):
#         bfsperiod((ROW_LEN-1,j))

# print(visited)

# for i in range(ROW_LEN):
#     for j in range(COL_LEN):
#         if not visited[i][j]:
#             if (pipes[i][j] != '.'):
#                 count += bfs((i,j))
#             else:
#                 count += 1
# print(count)

