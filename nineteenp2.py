import copy


f = open("nineteen.txt")
info = f.read().split('\n\n')


workflows = info[0].split()
parts = info[1].split()

workflowdict = {}

for workflow in workflows:
    sp = workflow[:-1].split('{')
    workflowdict[sp[0]]=sp[1]


#print(workflowdict)


# def processworkflow(currbounds, flowname, )


# nametobounds = {} #dict with keys=flowname, values are a list of dict with keys x,m,a,s values a list of length 2 with the upper/lower bounds
# #assuming you start from that flowname (list bc theres multiple paths u can take)
# def getBounds(flowname):
#     global workflowdict
#     global nametobounds


#     #checks if its already been processed
#     if (flowname in nametobounds.keys()):
#         return nametobounds[flowname]

#     options = workflowdict[flowname].split(',')
#     currbounds = {}
#     lst = ['x','m','a','s']
#     for elem in lst:
#         currbounds[elem] = [1,4000] #inclusive of both bounds
#     acceptbounds = []#list of all possible accepted bounds from the listed options for the flowname

#     for option in options:
#         if ':' not in option:
        




def countPossible(bounds):
    csum = 1
    for key in bounds.keys():
        diff = bounds[key][1] - bounds[key][0] + 1
        if (diff < 0):
            return 0
        csum *= diff
    return csum


#checking that there are no loops (though idk how that would be possible?)
#but there are none lol so we're good
seen = set()


#cbounds is a dict of keys x,m,a,s with values a list of length 2 like [lowerbound, upperbound] (inclusive both ends)
#for whatever your current bounds look like following your current workflow
def processworkflow(cbounds, flowname):
    if (flowname == 'A'):
        return countPossible(cbounds)
    if (flowname == 'R'):
        return 0
    

    global seen
    if (flowname in seen):
        print("seen 2x:")
        print(flowname)
    seen.add(flowname)

    global workflowdict

    options = workflowdict[flowname].split(',')

    boundspossible = []
    resflows = []
    for i in range(len(options)):
        boundspossible.append(copy.deepcopy(cbounds))
        #creates copies of the current bounds so we have an individual range for each possible path we can take
        #in the current workflow

    for i in range(len(options)):
        option = options[i]
        if ':' not in option:
            resflows.append(option)#else option, the option is just the resulting path
            break

        steps = option.split(':')
        resultflow = steps[1]
        rule = steps[0]
        var = rule[0]
        number = int(rule[2:])
        resflows.append(resultflow)
        if '<' in option:#change the upper bound at index i, the lower bound at index i+1 (for the else condition)
            boundspossible[i][var][1] = min(boundspossible[i][var][1], number - 1)#strictly less or greater than
            #change ALL FUTURE BOUNDS into the ELSE condition
            for j in range(i+1, len(boundspossible)):
                boundspossible[j][var][0] = max(boundspossible[i+1][var][0], number)#change the next bound into the 'else' condition
                #but we need to change ALL the future bounds to incorporate the else condition
        else:# > case
            boundspossible[i][var][0] = max(boundspossible[i][var][0], number+1)#max for changing lower bound
            for j in range(i+1, len(boundspossible)):
                boundspossible[j][var][1] = min(boundspossible[i+1][var][1], number)#min for changing upper bound

    csum = 0
    for i in range(len(boundspossible)):
        resflow = resflows[i]
        csum += processworkflow(boundspossible[i],resflow)#recursively sums all possible combinations of the accepting bounds
        #starting from the current workflow name
    return csum
            

startcount = {'x':[1,4000],'m':[1,4000], 'a':[1,4000], 's': [1,4000]}

total = processworkflow(startcount, 'in')

print(total)
