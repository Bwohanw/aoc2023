f = open("eighteen.txt", 'r')

commands = f.readlines()


coords = []

cx = 1
cy = 1

directions = {'R': (1,0), 'L': (-1,0), 'D': (0,1), 'U' : (0,-1)}

blocks = 0

for command in commands:
    s = command.split()
    multiplier = int(s[1])
    blocks += multiplier
    dir = s[0]
    cx += directions[dir][0] * multiplier
    cy += directions[dir][1] * multiplier
    coords.append((cx,cy))

coords.insert(0, (1,1))
def shoelace(coor):
    csum = 0
    for i in range(len(coor)-1):
        csum += (coor[i][0] - coor[i+1][0]) * (coor[i][1] + coor[i+1][1])
    return int(csum/2  - 0.5*blocks + 1)+ blocks #picks theorem for finding the area + the perimeter

print(shoelace(coords))