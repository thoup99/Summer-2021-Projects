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
        
to_sort = [3, 7, 1, 9, 20 , 4]
#print(sort(to_sort))
print(sort2(to_sort))