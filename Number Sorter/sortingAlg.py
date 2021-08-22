def sort(set):
    sorted_set = []
    for x in range(len(set)):
        to_add = set[0]
        to_add_loc = 0
        for loc, item in enumerate(set):
            if (item < to_add):
                to_add = item
                to_add_loc = loc
        sorted_set.append(set[to_add_loc])
        set.pop(to_add_loc)
    return(sorted_set)

def sort2(set):
    for x in range(len(set)):
        to_add = set[x]
        to_add_loc = x
        for loc, item in enumerate(set):
            if (loc > x):
                if (item < to_add):
                    to_add = item
                    to_add_loc = loc
        set.pop(to_add_loc)
        set.insert(x, to_add)
    return(set)

def sortbub(set):
    for iteration in range(len(set)):
        for loc in range(len(set) - iteration - 1):
            if set[loc] > set[loc+1]:
                set[loc], set[loc + 1] = set[loc + 1], set[loc]
    return(set)


to_sort = [3, 7, 1, 9, 20 , 4, 3270, 534, 847, 30, 47, 24, 68, 65]
#print(sort(to_sort))
#print(sort2(to_sort))
print(sortbub(to_sort))