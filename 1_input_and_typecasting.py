''' In Python, we use the input() function and put this function in either int(), float(), or bool() to typecast the input into required data type. Also, integers, 
floating-points and boolean variables don't have any range in Python. As long as you have enough memory, you can work with them.
In this question, you will take input of 4 variables that are in separate lines. The first variable is an integer, the second is a string(single/multiple words possible), the third is a floating number, the fourth is a boolean value.
You need to take the inputs and print the outputs.

Example:

Input:
a = 56
b = 'fdg fgdf'
c = 3.43534
d = True
Output:
56 
fdg fgdf 
3.43534 
True   '''

def inPut():
    a = int(input())## a is integer
    b = input()## b is string
    c = float(input())## c is float
    d = bool(input())## d is a boolean
    
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
