''' Your are familiar with input, output and data types in Python. Let us move on to play with operators in Python. Operators used widely in Python are '+',  '-', '*', '/', '**', '//'.


Arithmetic Operations:
a. Add ("+"): Adding X and Y.
b. Subtract ("-"): Subtracting X and Y.
c. Multiply ("*"): Multiply X and Y.
d. Divide ("/"): Divide X by Y.
e. Multiplying X, Y times ("**"): X raised to power Y.
f. Divide and floor the result ("//"): Divide and result is in integer form.

Example: 

Input: X = 10, Y = 5
Output:
15
5
50
2.0
100000
2
Explanation:
Adding X and Y: 15
Subtracting Y from X: 5
Multiplying X and Y: 50
Divide Y from X: 2.0
X raised to power Y: 100000
Divide Y from X and taking floor
value as int: 2  '''

def do_operation(x,y):
   print(x+y)
   print(x-y)
   print(x*y)
   print(x/y)
   print(x**y)
   print(x//y)
