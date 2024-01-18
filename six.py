import math

f = open("six.txt", "r")

info = f.readlines()
timelist = info[0].split(':')[1]
distancelist = info[1].split(':')[1]

timelist = timelist.split()
distancelist = distancelist.split()

times = [int(x) for x in timelist]
distances = [int(x) for x in distancelist]


def solvequadratic(t, d):
    #equation: x(t-x) > d, solve for the first int x that satisfies
    #-x^2 + tx - d > 0
    a = -1
    b = t
    c = -d
    disc = b**2 - 4*a*c
    root1 = -b + math.sqrt(disc)
    root2 = -b - math.sqrt(disc)
    root1 /= -2
    root2 /= -2
    maxroot = max(root1, root2)
    minroot = min(root1, root2)
    lowerbound = math.floor(minroot + 1)
    print(minroot)
    print(maxroot)
    print(lowerbound)
    return math.ceil(maxroot-lowerbound)

csum = 1

for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    root = solvequadratic(time, distance)
    csum *= root

print(csum)
