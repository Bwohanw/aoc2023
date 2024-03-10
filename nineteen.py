f = open("nineteen.txt")
info = f.read().split('\n\n')


workflows = info[0].split()
parts = info[1].split()

workflowdict = {}

for workflow in workflows:
    sp = workflow[:-1].split('{')
    workflowdict[sp[0]]=sp[1]


#print(workflowdict)


def processworkflow(flowname, nametovar):
    global workflowdict

    options = workflowdict[flowname].split(',')
    #nametovar = {'x': x, 'm' : m, 'a' : a, 's' : s}
    for option in options:
        if (':' not in option):
            return option
        
        steps = option.split(':')
        resflow = steps[1]
        if ('<' in option):
            if (nametovar[steps[0][0]] < int(steps[0][2:])):
                return resflow
        else:
            if (nametovar[steps[0][0]] > int(steps[0][2:])):
                return resflow
    

csum = 0
for part in parts:
    values = part[1:-1].split(',')
    nametovar = {}
    parttotal = 0
    for value in values:
        lr = value.split('=')
        nametovar[lr[0]] = int(lr[1])
        parttotal += int(lr[1])
    currentflow = 'in'
    while True:
        currentflow = processworkflow(currentflow, nametovar)
        if (currentflow == 'A'):
            csum += parttotal
            break
        if (currentflow == 'R'):
            break

print(csum)
    
