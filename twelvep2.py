from functools import cache

f = open("twelve.txt", 'r')

lines = f.readlines()

puzzles = []
numbers = []

for line in lines:
    split = line.split()
    puzzles.append(split[0])
    #nums = split[1].split(',')
    # for i in range(len(nums)):
    #     nums[i] = int(nums[i])
    numbers.append(eval(split[1]))

# print(puzzles)
# print(numbers)

newpuzzles = []
newnumbers = []
for i in range(len(lines)):
    unfolded = ''
    for j in range(4):
        unfolded =unfolded + puzzles[i] + '?'
    unfolded += puzzles[i]
    newpuzzles.append(unfolded)
    # unfoldednum = []
    # for j in range(5):
    #     for elem in numbers[i]:
    #         unfoldednum.append(elem)
    unfoldednum = numbers[i] * 5
    newnumbers.append(unfoldednum)

# print(newpuzzles)
# print(newnumbers)

puzzles = newpuzzles
numbers = newnumbers

#let numsols(i,j) be the number of solutions from A[i,...,n-1] where you need to make numbers [j,...m-1] from the numbers
'''recurrence: numsols(i,j) = 
1 if j == m
0 if i == n
numsols(i+1,j) if A[i] == .
0 if A[i] == # but the line of ? is not size numbers[j] (or can't create one, or even too big)
numsols(i+1,j) if A[i] == ? but can't make line of # of size numbers[j] with a period at the end
numsols(i+numbers[j] + 1,j+1) if A[i] == ? or # and you can make line of # of size numbers[j] with period at the end
'''

@cache
def numsols(puzzle, numlist):
    if len(numlist) == 0:
        return 0 if '#' in puzzle else 1
    if len(puzzle) == 0:
        return 0 if len(numlist) != 0 else 1
    
    totalcount = 0

    if puzzle[0] == '.' or puzzle[0] == '?':
        totalcount += numsols(puzzle[1 : ], numlist)
    if puzzle[0] == '#' or puzzle[0] == '?':
        run = numlist[0]
        if (run <= len(puzzle) and '.' not in puzzle[:run] and (len(puzzle) == run or puzzle[run] != '#')):
            totalcount += numsols(puzzle[run + 1 : ], numlist[1 : ])
    return totalcount

total = 0
for i in range(len(lines)):
    total += numsols(puzzles[i],numbers[i])

print(total)

#let numsols[i][j] be the number of ways to satisfy puzzles[i,...,n-1] using numlist[j,...,m-1]
#numsols[n][j] = 0 unless j == m then it's 1
#numsols[i][m] = 1 if # not in puzzles[i:] else 0
def numsolsdp(puzzle, numlist):
    n = len(puzzle)
    m = len(numlist)
    numsols = []
    for i in range(len(puzzle) + 1):
        numsols.append([0] * (len(numlist) + 1))
    for i in range(len(numlist)):
        numsols[n][i] = 0
    for i in range(len(puzzle)):
        numsols[i][m] = 0 if '#' in puzzle[i:] else 1
    numsols[n][m] = 1

    # print(numsols)

    #eval order right to left, bottom to top
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if puzzle[i] == '.' or puzzle[i] == '?':
                numsols[i][j] += numsols[i+1][j]
            if (puzzle[i] == '?' or puzzle[i] == '#') and (i == 0 or puzzle[i-1] == '.' or puzzle[i-1] == '?'):
                run = numlist[j]
                if (run <= len(puzzle[i:]) and ('.' not in puzzle[i:i+run]) and (len(puzzle[i:]) == run or puzzle[i+run] != '#')):
                    # print(i)
                    # print(j)
                    # print(run)
                    if (i+run+1 <= n):
                        numsols[i][j] += numsols[i+run+1][j+1]
                    else:
                        numsols[i][j] += 1 if j+1 >= m else 0
    
    #print(numsols)
    return numsols[0][0]


total = 0
for i in range(len(lines)):
    total += numsolsdp(puzzles[i],numbers[i])

print(total)