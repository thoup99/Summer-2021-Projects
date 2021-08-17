def sumoftwo(itemA, itemB, targ):
    for a in itemA:
        for b in itemB:
            if (a + b == targ):
                return (True)
    return (False)

def sumoftwo1(itemA, itemB, targ):
    for item in itemA:
        if (targ - item in itemB):
            return(True)
    return(False)

def sumoftwo2(itemA, itemB, targ):
    comp = []
    for item in itemA:
        comp.append(targ - item)
    for item in itemB:
        if (item in comp):
            return(True)
    return(False)

a = [0, 0, -5, 30212]
b = [-10, 40, -3, 9]
targ = -8
print(sumoftwo2(a, b, targ))