from collections import deque
import math


f = open("twenty.txt", "r")

info = f.readlines()
#% -> flip
#& -> conjunction


broadcasterdest = []#list of all the destinations from the initial broadcaster

srctodest = {}#keys: modules, values are a list of the modules they broadcast signals to

fliptostate = {}#keys: flipflop modules, values are True if the module is on False if it's off

conjtoparents = {}#keys: conj modules, values are a dictionary with keys=modules sending signal to this module values are that signal
#INNER DICTIONARY: key=modules, values is False if the remembered signal is low, True if it's high

#populate the brodcaster destination list, and the dictionaries with the different modules->destinations
for line in info:
    sp = line.split(" -> ")
    src = sp[0].strip()
    dests = sp[1].split(',')
    for i in range(len(dests)):
        dests[i] = dests[i].strip()
    
    if (src[0] == '%'):
        fliptostate[src[1:]] = False
    elif (src[0] == '&'):
        conjtoparents[src[1:]] = {}
    else:
        broadcasterdest = dests
        continue
    srctodest[src[1:]] = dests



#populate the parent modules for the conjugate modules
for key in srctodest.keys():
    for module in srctodest[key]:
        if module in conjtoparents.keys():
            conjtoparents[module][key] = False

print(conjtoparents['xm'])#xm is the conj module feeding into rx so we need it to have high signals from
#all of its parents to send a low signal to rx
parents = list(conjtoparents['xm'].keys())


def pressbutton(i):
    global broadcasterdest
    global srctodest
    global fliptostate
    global conjtoparents
    global parents


    moduleq = deque()#queue of the order of the modules to process
    pulseq = deque()#queue of the signalse sent to the module, true if sent high pulse, false if sent low pulse

    for module in broadcasterdest:
        moduleq.append(module)
        pulseq.append(False)
    
    while (len(moduleq) != 0):
        module = moduleq.popleft()
        pulse = pulseq.popleft()

        

        if module in fliptostate.keys():#module is a flipflop module
            if (not pulse):#pulse is low, (ignores high pulses)
                fliptostate[module] = not fliptostate[module] #flips off if on, on if off
                #if it was off, fliptostate[module] is now True, and we want to send a high signal, so we just send fliptostate[module] as our signal
                #same for if it was on
                if module == parents[i] and fliptostate[module]:
                    return True
                for futuremod in srctodest[module]:
                    moduleq.append(futuremod)
                    pulseq.append(fliptostate[module])


                    #remembering signal for future conj modules
                    if (futuremod in conjtoparents.keys()):
                        conjtoparents[futuremod][module] = fliptostate[module] #module (parent)'s newest signal to the conjugate module is of signal fliptostate[module]
        elif module in conjtoparents.keys():#module is a conj module
            allhigh = True
            for parent in conjtoparents[module].keys():
                allhigh = allhigh and conjtoparents[module][parent]
                if (not allhigh):
                    break
            if module == parents[i] and not allhigh:
                return True
            #sends future pulse of (not allhigh)
            for futuremod in srctodest[module]:
                moduleq.append(futuremod)
                pulseq.append(not allhigh)

                #remembering signal for future conj modules
                if (futuremod in conjtoparents.keys()):
                    conjtoparents[futuremod][module] = not allhigh
        
    return False


lcmnums = []
cnum = 0
while True:
    cnum += 1
    res = pressbutton(0)#changed this from 0-3 one by one because we have to reset the whole system to find
    #how many presses it takes from the very beginning
    if (res):
        break
lcmnums.append(cnum)

print(lcmnums)#[3877, 3917, 3889, 3803]
print(math.lcm(3877,3917,3889,3803))


