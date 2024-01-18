f = open("four.txt", "r")

lines = f.readlines()

information = []

for line in lines:
    information.append(line[9:])

print(information[0])

csum = 0

for cards in information:
    splitdata = cards.split("|")
    winningcards = splitdata[0].split()
    yourcards = splitdata[1].split()
    number = 0
    for card in yourcards:
        if card in winningcards:
            number += 1
    if (number != 0):
        csum += 2**(number-1)

print(csum)