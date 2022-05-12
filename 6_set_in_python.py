''' Some important functions in Set in Python:
add(): Adds an element to the set.
clear(): Removes all elements from the set
discard(): Removes an element from the set if present.
remove(): Removes an element from the set. If the element is not present, it raises an error.
pop(): Removes and returns an arbitrary set element. Raise the error if the set is empty.
union(): Returns the union of sets in a new set
update(): Updates the set with the union of itself and others
len(): Return the length of the set.
sorted(): Return a new sorted list from elements in the set.
sum(): Return the sum of all elements in the set.

Let's implement these methods through a question. Given Q queries to do some operation on Set, the task is to perform all the queries in the Set as given below:
a. i element: Adds an element to the set.
b. r element: Remove an element from the set.
c. s: Find the sum of elements in the set. Returns the sum of elements in the set.

Example:

Input:
Q = 4
S = {1, 2}
i 5
i 6
r 5
s
Output:
6
Explanation:
5 is added into the set
6 is added into the set
5 is removed from the set
So, now set is S = {1, 2, 6}
sum = 9
Your Task:

Your task is to complete the functions insert(), remove_from_set() and sum_set() that performs the specified tasks.

Constraints:
1 <= S[i] <= 10^4 '''




# Function to insert
# no return should be there, and no print statement
def insert(S, element):
    # Your code here
    S.add(element)
        

# Function to remove element from set
# No return and nothing to print
def remove_from_set(S, element):
    # Your code here
    S.discard(element)
        
    
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(S):
    # Your code here
    a = sum(S)
    return a
    
