f = open('eight.txt', 'r')

info = f.readlines()
steps = info[0].strip()
print(steps)

stepmapping = {'R':1,'L':0}

paths = {}
for i in range(2,len(info)):
    maps = info[i]
    src = maps[0:3]
    dest1 = maps[7:10]
    dest2 = maps[12:15]
    paths[src] = (dest1,dest2)

current = 'AAA'
numsteps = 0
stepindex = 0
while (current != 'ZZZ'):
    currentstep = steps[stepindex]
    direction = stepmapping[currentstep]
    current = paths[current][direction]
    numsteps += 1
    stepindex = stepindex + 1 if stepindex < len(steps) - 1 else 0

print(numsteps)
