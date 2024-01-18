import math

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

currents  = []
for point in paths.keys():
    if (point[-1] == 'A'):
        currents.append(point)
print(currents)
numsteps = []
stepindex = 0


for current in currents:
    stepindex = 0
    stepcounter = 0
    while (current[-1] != 'Z'):
        currentstep = steps[stepindex]
        direction = stepmapping[currentstep]
        current = paths[current][direction]
        stepcounter += 1
        stepindex = stepindex + 1 if stepindex < len(steps) - 1 else 0
    numsteps.append(stepcounter)


print(numsteps)#11567,21251,12643,16409,19099,14257

print(math.lcm(11567,21251,12643,16409,19099,14257))