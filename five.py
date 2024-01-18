f = open("five.txt", "r")

info = f.read()

splitgroups = info.split("\n\n")

seeds = splitgroups[0]

groupmaps = splitgroups[1:]


listofmaps = []
#each map has key: (starting, ending) -> (startingdest)
#(get length by startingdest + idx-starting)

for grouping in groupmaps:
    splitgroup = grouping.split('\n')[1:]
    currentmap = {}
    for mapping in splitgroup:
        splitmapping = mapping.split()
        if (len(splitmapping) == 0):
            break
        dest = int(splitmapping[0])
        src = int(splitmapping[1])
        length = int(splitmapping[2])
        endingsrc = src + length - 1
        currentmap[(src, endingsrc)] = dest
    listofmaps.append(currentmap)



seedlist = []

seedstr = seeds[6:].split()

for i in seedstr:
    seedlist.append(int(i.strip()))


cmin = -1

for seed in seedlist:
    current = seed
    for mapping in listofmaps:
        for key in mapping.keys():
            if current >= key[0] and current <= key[1]:
               current = mapping[key] + current-key[0]
               break
    if (current < cmin or cmin < 0):
        cmin = current

print(cmin)