''' Given a list of strings containing names of students and another list containing marks of corresponding students. The task is to create a dictionary to store marks of students with their names (name will be unique).

Example:

Input: 
N = 5 
names = [john, ala, ilia, sudan, mercy] 
marks = [100, 200, 150, 80, 300]
Output:
ala 200 
ilia 150 
john 100 
mercy 300 
sudan 80
Your Task:
The task is to complete the function create_dict() which takes arr as input and creates a dictionary then returns it.

Constraints:
1 <= N <= 104
1 <= marks <= 104  '''

def create_dict(arr):
    
    dict = {}
    for i in range(0,len(arr),1):        #Used a loop here to iterate over the array arr and then assign each of the value to the dictionary
        dict[arr[i][0]]=arr[i][1]
    
    
    return dict
