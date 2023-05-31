import math

def getColumn(rows, i):
    column = ""
    for row in rows:
        if i < len(row):
            column += row[i]
    return column
        
def encryption(s):
    s = s.replace(" ", "")
    l = len(s)
    square_root_l = math.sqrt(l)
    floor = math.floor(square_root_l)
    ceil = math.ceil(square_root_l)

    print(floor)
    print(ceil)

    rows = [s[i:i+ceil] for i in range(0, len(s), ceil)]
    print(rows)
        
    columns = []
    for i in range(ceil):
        columns.append(getColumn(rows, i))
    
    print(columns)
    return " ".join(columns)
        

print(encryption("if man was meant to stay on the ground god would have given us roots"))
print(encryption("haveaniceday"))