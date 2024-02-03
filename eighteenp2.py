f = open("eighteen.txt", 'r')

commands = f.readlines()


coords = []

cx = 1
cy = 1


digtodir = {0:'R', 1: 'D', 2 : 'L', 3 : 'U'}
directions = {'R': (1,0), 'L': (-1,0), 'D': (0,1), 'U' : (0,-1)}

blocks = 0

hex = {}
for i in range(6):
    hex[chr(ord('a') + i)] = 10 + i
for i in range(10):
    hex[str(i)] = i
print(hex)

for command in commands:
    s = command.split()[-1]
    s = s[1:-1]
    dir = digtodir[int(s[-1])]
    s = s[1:-1]
    mult = 0
    sixteenpow = 4
    for x in s:
        mult += hex[x] * (16 ** sixteenpow)
        sixteenpow -= 1
    blocks += mult
    cx += directions[dir][0] * mult
    cy += directions[dir][1] * mult
    coords.append((cx,cy))



coords.insert(0, (1,1))
def shoelace(coor):
    csum = 0
    for i in range(len(coor)-1):
        csum += (coor[i][0] - coor[i+1][0]) * (coor[i][1] + coor[i+1][1])
    return int(csum/2  - 0.5*blocks + 1)+ blocks #picks theorem for finding the area + the perimeter

print(shoelace(coords))