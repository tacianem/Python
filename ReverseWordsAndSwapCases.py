# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.

def reverse_words_order_and_swap_cases(sentence):
    
    begins_and_ends_with_letter = False
    if (sentence[0].isalpha() and sentence[len(sentence)-1].isalpha()):
        begins_and_ends_with_letter = True
        
    while "  " in sentence:
        sentence = sentence.replace("  ", " ")
        
    words = sentence.split(" ")

    short_words = True
    only_letters = []
    
    for word in words:
        if len(word) > 10:
            short_words = False
            
        if word.isalpha():
            only_letters.append(True)

            
    if len(words) <= 10 and short_words and begins_and_ends_with_letter and len(only_letters) == len(words):
        sentence = ""
        
        for word in words:
            sentence = word + " " + sentence
            
        return sentence.swapcase()

        
print(reverse_words_order_and_swap_cases("aWESOME is cODING"))
