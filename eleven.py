f = open("eleven.txt",'r')

info = f.readlines()

galaxies = []
galaxy_rows = set()
galaxy_cols = set()

rownums = len(info)
colnums = len(info[0])

#gets positions of all galaxies, and also puts rows/cols that have galaxies into their sets
for rownum in range(len(info)):
    for colnum in range(len(info[rownum])):
        if info[rownum][colnum] == '#':
            galaxies.append((rownum,colnum))
            galaxy_rows.add(rownum)
            galaxy_cols.add(colnum)


empty_rows = []
empty_cols = []

for i in range(rownums):
    if i not in galaxy_rows:
        empty_rows.append(i)

for i in range(colnums):
    if i not in galaxy_cols:
        empty_cols.append(i)


def countemptyrows(startrow, endrow):
    global empty_rows
    counter = 0
    for row in empty_rows:
        if (row > startrow and row < endrow or row > endrow and row < startrow):
            counter += 1
    return counter

def countemptycols(startcol, endcol):
    global empty_cols
    counter = 0
    for col in empty_cols:
        if (col > startcol and col < endcol or col > endcol and col < startcol):
            counter += 1
    return counter


totaldist = 0
for i in range(len(galaxies)):
    galaxy1 = galaxies[i]
    for j in range(i+1, len(galaxies)):
        galaxy2 = galaxies[j]
        totaldist += abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1]) + countemptyrows(galaxy1[0],galaxy2[0]) + countemptycols(galaxy1[1],galaxy2[1])

print(totaldist)