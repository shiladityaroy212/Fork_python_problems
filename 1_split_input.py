''' There are times when all the inputs are provided in a single line and are separated by spaces. In such cases, the input() function takes the whole line as input and 
treats the line as a single input. We can use input().split() functionality to split the string into multiple words.

Example:
Input: string = Geeks 2 2.3445
Output: Geeks 4.3445 '''

def inPutS():
    string = input() 
    s, i, f = string.split() 
    print(s + " " + str(int(i) + float(f))) 
