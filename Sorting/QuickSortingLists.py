# Sort a list
# Receives a list of numbers and a string (asc, desc, or none)
from random import randint

def quickSort(list, order): 
    if len(list) < 2:
        return list
    
    if order == "asc":
        lower, equal, higher = [], [], []

        pivot = list[randint(0, len(list)-1)]

        for n in list:
            if n < pivot:
                lower.append(n)
            elif n > pivot:
                higher.append(n)
            else: #if n == pivot:
                equal.append(n)

        return (quickSort(lower, "asc") + equal + quickSort(higher, "asc"))

    if order == "desc":
        final_list = quickSort(list, "asc")
        final_list.reverse()
        return final_list

    else:
        return list
            
sorted_list = quickSort([5, 9, 7, 1, 2, 9], "desc")
print(sorted_list)