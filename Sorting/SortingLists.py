# Sort a list
# Receives a list of numbers and a string (asc, desc, or none)

def sortList(num_list, order): 
    if len(num_list) < 2:
        return num_list
    
    if order == "asc":
        num_list.sort()
        return num_list

    if order == "desc":
        num_list.sort(reverse=True)
        return num_list
        
    else:
        return num_list
            
sorted_list = sortList([5, 9, 7, 1, 2, 9], "asc")
sorted_list_desc = sortList([5, 9, 7, 1, 2, 9], "desc")
print(sorted_list)
print(sorted_list_desc)