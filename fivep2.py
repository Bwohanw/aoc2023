f = open("five.txt", "r")

info = f.read()

splitgroups = info.split("\n\n")

seeds = splitgroups[0]

groupmaps = splitgroups[1:]


listofranges = []
#each map has key: (starting, ending) -> (startingdest)
#(get length by startingdest + idx-starting)

for grouping in groupmaps:
    splitgroup = grouping.split('\n')[1:]
    currentmap = []
    for mapping in splitgroup:
        splitmapping = mapping.split()
        if (len(splitmapping) == 0):
            break
        dest = int(splitmapping[0])
        src = int(splitmapping[1])
        length = int(splitmapping[2])
        endingsrc = src + length - 1
        currentmap.append((src, endingsrc,dest))
    listofranges.append(sorted(currentmap))
#missing the range from (max, infinity)
#print(listofranges)

#populate the list of ranges with the missing ranges (just map to themselves)
for j in range(len(listofranges)):
    rangelist = listofranges[j]
    start = 0
    for i in range(len(rangelist)):
        startpt,endpt,mappingpt = rangelist[i]
        if (start < startpt):
            listofranges[j].insert(i,(start, startpt-1, start))
            i += 1
        start = endpt + 1

#print(listofranges)

#listofranges is a list of all the seed transformations
#each list in listofranges represents one transformation
#they are stored in the format (x,y,z) where x,y are the endpoints of the source range
#and z is the startpoint of the destination interval

seedlist = []

seedstr = seeds[6:].split()

for i in seedstr:
    seedlist.append(int(i.strip()))

#print(seedlist)

seedpoints = []
for i in range(0,len(seedlist), 2):
    seedpoints.append((seedlist[i],seedlist[i] + seedlist[i+1] - 1))
#puts the seeds in a list in the format (startpoint, endpoint) of the interval, both sides inclusive.

#startpoints and endpoints of each thing
#print(seedpoints)

#this function takes in a startpoint and endpoint of an interval, along with a mapping of interval->interval
    #returns a list of the intervals that the input interval is transformed into.
def newpoints(startpoint, endpoint, lst):
    startrangeidx = -1
    endrangeidx = -1
    
    for i in range(len(lst)):
        startpt, endpt, dest = lst[i]
        if (startpoint >= startpt and startpoint <= endpt):
            startrangeidx = i
        if (endpoint >= startpt and endpoint <= endpt):
            endrangeidx = i
    if (startrangeidx == -1): #in range (, infty), maps to self
        return [(startpoint, endpoint)]
    if (startrangeidx == endrangeidx):
        startpt, endpt, dest = lst[startrangeidx]
        return [(dest + startpoint - startpt, dest + endpoint - startpt)]
    if (endrangeidx == -1): #start is in a range but end isn't
        startpt, endpt, dest = lst[startrangeidx]
        toret = []
        toret.append((dest + startpoint - startpt,endpt - startpt + dest))
        for i in range(startrangeidx + 1, len(lst)):
            elem = lst[i]
            toret.append((elem[2],elem[2] + elem[1]-elem[0]))
        toret = sorted(toret)
        toret.append((lst[-1][1] + 1, endpoint))#maximum destionation mapped to + 1
        return sorted(toret)
    #otherwise everything is inside an interval
    startpt, endpt, dest = lst[startrangeidx]
    toret = []
    toret.append((dest + startpoint - startpt,endpt - startpt + dest))
    for i in range(startrangeidx + 1, endrangeidx):
        elem = lst[i]
        toret.append((elem[2],elem[2] + elem[1]-elem[0]))
    startpt, endpt, dest = lst[endrangeidx]
    toret.append((dest,dest + endpoint - startpt))
    return toret

# print(listofranges[4])
# print(newpoints(74,87,listofranges[4]))

#applies each successive transformation to the seeds
for seedmap in listofranges:
    # print(seedpoints)
    newlst = []
    for i in range(0,len(seedpoints)):
        newpts = newpoints(seedpoints[i][0],seedpoints[i][1], seedmap)
        for point in newpts:
            newlst.append(point)
    seedpoints = newlst

# print(seedpoints)

minimum = 100000000000000000
for elem in seedpoints:
    if elem[0] < minimum:
        minimum = elem[0]
print(minimum)