# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def encryptPassword(pwd):
    s = ""
    ignored_chars = []

    for i, char in enumerate(pwd):
        if char.isnumeric():
            s = char + s + '0'
        elif char.islower():
            if not i == len(pwd)-1: # namely, if there's next char
                next_char = pwd[i+1]
                if next_char.isupper():
                    s += next_char + char + '*'
                    ignored_chars.append((i+1, next_char))
                else: 
                    s += char
            else: # if last char is lower case
                s += char
        elif (char.isupper() and not (i, char) in ignored_chars):
            s += char
        
    return s

def decryptPassword(s):
    msg = ""
    zero_index = 0
    
    numbers=[]
    for char in s:
        if char.isnumeric() and not char == '0':
            numbers.append(char)
    # print(numbers)
            
    for i, char in enumerate(s):
        if char == '*':
            msg = msg[:-2] + s[i-1] + s[i-2]
        
        if char == '0':
            msg += numbers[(len(numbers)-1) - zero_index]
            zero_index += 1
            
        if not char.isnumeric() and not char == '*':
            msg += char
    
    return msg

    
print(encryptPassword("hAck3rr4nk"))
print(decryptPassword("43Ah*ck0rr0nk"))