def hasEqualChars(s):
    for i, char in enumerate(s):
        if not i == len(s)-1:
            next_char = s[i+1]
            if char == next_char:
                return True
    return False

def reduceString(s):
    result = ""
    ignored_indexes = []

    for i, char in enumerate(s):
        if not i == len(s)-1 and not i in ignored_indexes:
            next_char = s[i+1]
            if char == next_char:
                result += ""
                ignored_indexes.append(i+1)
            else:
                result += char
        if i == len(s)-1 and not i in ignored_indexes:
            result += char

    return result


def superReducedString(s):    
    while hasEqualChars(s):
        s = reduceString(s)

    if not s:
        return "Empty String"
    return s
    
print(superReducedString("aaabccddd"))
print(superReducedString("baab"))

