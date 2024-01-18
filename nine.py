f = open("nine.txt", "r")

numberlines = f.readlines()


def calculatedistances(numlist):
    differences = []
    for i in range(1, len(numlist)):
        differences.append(numlist[i] - numlist[i-1])
    if (differences.count(0) == len(differences)):
        return numlist[-1]
    return numlist[-1] + calculatedistances(differences)

csum = 0

for line in numberlines:
    numbers = line.split()
    numlist = []
    for num in numbers:
        numlist.append(int(num))
    csum += calculatedistances(numlist)

print(csum)