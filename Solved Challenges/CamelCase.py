def camelCase(s):
    number_words = 1

    for char in s:
        if char.isupper():
            number_words +=1
            
    return number_words


print(camelCase("saveChangesInTheEditor"))