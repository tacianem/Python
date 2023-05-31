def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"
    min = 0

    one_digit = one_lowercase = one_uppercase = special_char = False

    for char in password:
        if char.isnumeric():
            one_digit = True
        elif char.islower():
            one_lowercase = True
        elif char.isupper():
            one_uppercase = True
        elif char in special_characters:
            special_char = True

    if not one_digit:
        min += 1
    if not one_lowercase:
        min += 1
    if not one_uppercase:
        min += 1
    if not special_char:
        min += 1
    if n + min < 6:
        min += 6 - (n+min)

    return min


print(minimumNumber(3, "Ab1"))
        


    
