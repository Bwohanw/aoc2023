f = open('fifteen.txt','r')

info = f.read()

steps = info.split(',')

'''
takes advantage of the insertion order of python dicts being preserved'''
boxes = {}
for i in range(256):
    boxes[i] = {}


def hash(s):
    h = 0
    for char in s:
        h += ord(char)
        h *= 17
        h %=256
    return h

for step in steps:
    if '-' in step:
        boxname = step[:-1]
        boxnum = hash(boxname)
        if boxname in boxes[boxnum].keys():
            d = boxes[boxnum]
            del d[boxname]
            boxes[boxnum] = d
    else:
        parts = step.split('=')
        boxnum = hash(parts[0])
        boxes[boxnum][parts[0]] = parts[0] + parts[1]

#print(boxes)


total = 0
for i in range(256):
    const = i+1
    counter = 1
    for key in boxes[i].keys():
        leng = int(boxes[i][key][-1])
        total += const * counter * leng
        counter += 1

print(total)