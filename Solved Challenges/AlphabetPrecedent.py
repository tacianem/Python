# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.

import string

def transformSentence(sentence):
    words = sentence.split(" ")
    new_words = []
    
    sentence_length = len(sentence) 
    if sentence_length >= 1 or sentence_length <= 100:
        alphabet = list(string.ascii_lowercase)
        print(alphabet)
               
        for word in words:
            print(word)
            new_word = word[0]
            for i, char in enumerate(word[1:]):
                print(char)
                preceding = word[i-1]
                lower_char = char.lower()
                # print(preceding)
                preceding_in_alphabet = alphabet.index(preceding.lower())
                current_in_alphabet = alphabet.index(lower_char)
                
                if preceding_in_alphabet < current_in_alphabet:
                    char = char.upper()
                    print("upper")
                elif preceding_in_alphabet > current_in_alphabet:
                    char = lower_char
                    print("lower")
                new_word += char
                print(word)

            new_words.append(new_word)

    
    return " ".join(new_words)

print(transformSentence("a Blue MOON"))
#expected output: a BLUe MOOn