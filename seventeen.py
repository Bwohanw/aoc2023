import heapq


'''
day 17 part 1 (dijkstras using graph layering to track horizontal vs vertical distances,
 2 blocks had an edge btw them if they were in between minsteps and maxsteps in a straight line away from each other,
   and we had to keep alternating horizontal and vertical)'''

f = open('seventeen.txt','r')
lines = f.read().split()

grid = []
visitedh = []
visitedv = []
#distance to get to (row,col) by a horiz step
distancesh = []
#distance to get to (row,col) by a vertical step
distancesv = []

for line in lines:
    row = []
    tf = [False] * len(line)
    tf2 = [False] * len(line)
    dist = [10000000] * len(line)
    dist2 = [10000000] * len(line)
    for char in line:
        row.append(int(char))
    grid.append(row)
    visitedh.append(tf)
    visitedv.append(tf2)
    distancesh.append(dist)
    distancesv.append(dist2)

numrow = len(grid)
numcol = len(grid[0])

def dijkstras(minstep, maxstep):
    #0 for previous step horizontal
    #1 for previous step vertical
    pq = []
    #(row, col, direction)
    heapq.heappush(pq, (0,(0,0,0)))
    heapq.heappush(pq, (0,(0,0,1)))
    distancesh[0][0] = 0
    distancesv[0][0] = 0
    while len(pq) != 0:
        elem = heapq.heappop(pq)
        dist = elem[0]
        row, col, dir = elem[1]
        if (visitedh[row][col] and dir == 0):
            continue
        if (visitedv[row][col] and dir == 1):
            continue
        if (dir == 0):
            visitedh[row][col] = True
        else:
            visitedv[row][col] = True
        if dir == 0:
            for i in [-1,1]:
                currdist = 0
                if (row + i*minstep < 0 or row + i*minstep >= numrow):
                    continue
                currdist = 0
                for j in range(1, maxstep + 1):
                    if (row + i*j < 0 or row + i*j >= numrow):
                        break
                    currdist += grid[row + i*j][col]
                    if (j < minstep):
                        continue
                    if (not visitedv[row+i*j][col]):
                        if (dist + currdist < distancesv[row+i*j][col]):
                            distancesv[row+i*j][col] = dist + currdist
                            heapq.heappush(pq, (dist + currdist, (row+i*j,col,1)))
        else:
            for i in [-1,1]:
                currdist = 0
                for j in range(1, maxstep + 1):
                    if (col + i*j < 0 or col + i*j >= numcol):
                        break
                    currdist += grid[row][col+i*j]
                    if (j < minstep):
                        continue
                    if (not visitedh[row][col+i*j]):
                        if (dist + currdist < distancesh[row][col+i*j]):
                            distancesh[row][col + i*j] = dist+currdist
                            heapq.heappush(pq, (dist+currdist, (row, col+i*j, 0)))
        

dijkstras(1,3)
# print(distancesh)
# print(distancesv)
# print(distancesh == distancesv)

# for row in distancesh:
#     print(row)

print(min(distancesh[numrow-1][numcol-1],distancesv[numrow-1][numcol-1]))