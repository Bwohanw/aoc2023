f = open("four.txt", "r")

lines = f.readlines()

information = []

for line in lines:
    information.append(line[9:])

print(information[len(information)-1])

numcopiesperrow = [1]*len(information)

for i in range(len(information)):
    cards = information[i]
    splitdata = cards.split("|")
    winningcards = splitdata[0].split()
    yourcards = splitdata[1].split()
    number = 0
    for card in yourcards:
        if card in winningcards:
            number += 1
    for j in range(i+1, min(len(information),i+number+1)):
        numcopiesperrow[j] += numcopiesperrow[i]
    
csum = 0
for copies in numcopiesperrow:
    csum += copies

print(csum)