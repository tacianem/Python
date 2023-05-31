# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.

def fizzBuzz(n):
    if (n > 0 and n < (2 * (10**5))):

        for i in range(1, n+1):
            multiple_of_3 = True if (i % 3 == 0) else False # Ternary operator
            multiple_of_5 = True if (i % 5 == 0) else False
            
            if multiple_of_3 and multiple_of_5:
                print("FizzBuzz")
            elif multiple_of_3:
                print("Fizz")
            elif multiple_of_5:
                print("Buzz")
            else:
                print(i)



if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)
