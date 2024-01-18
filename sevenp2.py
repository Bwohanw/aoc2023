f = open("seven.txt", "r")

lines = f.readlines()
cards = []
bets = []

mapping = {'2' : 2, '3':3,'4':4, '5': 5, '6' : 6, '7': 7, '8': 8, '9':9, 'T': 10, 'J':1, 'Q': 12, 'K':13, 'A':14}

for x in range(len(lines)):
    line = lines[x]
    info = line.split()
    card = info[0]
    bet = info[1]
    c = []
    for i in card:
        c.append(mapping[i])
    cards.append(c)
    bets.append(int(bet))




def getgrouping(card):
    counters = [0]*15
    for num in card:
        counters[num] += 1
    if (5 in counters):
        return 7 #five of a kind
    if 4 in counters:
        return 6
    if 3 in counters and 2 in counters:
        return 5
    if 3 in counters:
        return 4
    if counters.count(2) == 2:
        return 3
    if counters.count(2) == 1:
        return 2
    if counters.count(1) == 5:
        return 1
    return 0


def getmaxgrouping(card):
    jidxs = []
    for i in range(5):
        if card[i] == 1:
            jidxs.append(i)
    maxgrouping = getgrouping(card)
    if (len(jidxs) == 0):
        return maxgrouping
    for i in range(2, 15):
        ccopy = card.copy()
        for idx in jidxs:
            ccopy[idx] = i
        grouping = getgrouping(ccopy)
        if (grouping > maxgrouping):
            maxgrouping = grouping
    return maxgrouping

sortedcards = []
for card in cards:
    inserted = False
    for i in range(len(sortedcards)):
        currentcard = sortedcards[i]
        cardgroup = getmaxgrouping(card)
        ccardgroup = getmaxgrouping(currentcard)
        if (cardgroup > ccardgroup):
            sortedcards.insert(i,card)
            inserted = True
            break
        if (cardgroup == ccardgroup):
            shouldinsert = False
            for j in range(6):
                if (j == 5):
                    shouldinsert = True
                    break
                if (card[j] > currentcard[j]):
                    shouldinsert = True
                    break
                if (card[j] < currentcard[j]):
                    break
            if (shouldinsert):
                sortedcards.insert(i,card)
                inserted = True
                break
    if (not inserted):
        sortedcards.append(card)


totalwinnings = 0
for i in range(len(sortedcards)):
    card = sortedcards[i]
    idx = cards.index(card)
    betsize = bets[idx]
    rank = len(sortedcards) - i
    totalwinnings += betsize*rank

print(totalwinnings)
                