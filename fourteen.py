f = open("fourteen.txt", 'r')

lines = f.read().split()

formation = []
for line in lines:
    row = []
    for rock in line:
        row.append(rock)
    formation.append(row)

#print(formation)

def movenorth(startingx, startingy):
    global formation
    if (formation[startingx][startingy] != 'O'):
        return
    while (startingx != 0 and formation[startingx-1][startingy] == '.'):
        formation[startingx][startingy] = '.'
        formation[startingx-1][startingy] = 'O'
        startingx -= 1
    

for rowctr in range(len(formation)):
    for colctr in range(len(formation[rowctr])):
        movenorth(rowctr, colctr)

#print(formation)

weight = 0

numrows = len(formation)

for rowctr in range(len(formation)):
    for item in formation[rowctr]:
        if (item == 'O'):
            weight += numrows - rowctr

print(weight)