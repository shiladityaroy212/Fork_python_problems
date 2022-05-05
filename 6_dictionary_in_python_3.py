''' You are familiar with most of the properties of the dictionary in Python. Add some more info about dictionaries through dictionary formatting and deleting key-value pairs.

Formatting:
hash = {}
hash['Geeks'] = 5
hash['geeksforgeeks'] = 13
key = 'Geeks'
s = ("Count of characters is " + hash[key] + " in " + key)             # results in: Count of characters is 5 in Geeks.

Deleting:
dict = {'a' : 1, 'b': 2, 'c' : 3, 'd' : 4}
del dict['c']          # delete entry for 'c'

Let's get this into the head by solving a question. Given a list of some students in a list and their corresponding marks in another list. The task is to do some operations as described below:
a. i key value: Inserts key and value in the dictionary, and print 'Inserted'.
b. d key: Delete the entry for a given key and print 'Deleted' if the key to be deleted is present, else print '-1'.
c. key: Print marks of a given key in a statement as "Marks of student name is : marks".

Example:

Input:
N = 5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks

Output:
Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300

Explanation:
For first four queries, insert and del operation happens, correspondingly Inserted And Deleted is printed. For the last query, marks of geeks is printed.  '''



# insert into dictionary
def insert_dict(query, dict):
    
    # Your code here
    dict[query[1]]=query[2]
    

# deleting from dictionary
def del_dict(query, dict):
    
    # Your code here
    if(dict[query[1]]):
       del dict[query[1]]
       return True
    else:
       return False
    

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    if key in dict:
       print("Marks of {} is {}".format(key,dict[key]))
       return True
    else:
       return False
