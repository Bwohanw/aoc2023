f = open('fifteen.txt','r')

info = f.read()

steps = info.split(',')


total = 0
for step in steps:
    hash = 0
    for char in step:
        hash += ord(char)
        hash *= 17
        hash %= 256
    total += hash

print(total)