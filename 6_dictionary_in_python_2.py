''' You are now familiar with the dictionary in Python. It's time to dive deeper into the dictionary in Python. How can you use a dictionary to store the frequency of 
elements in list L. Given below is one method:

for i in L:
     dict[i] = 0

for i in L:
     dict[i] += 1
     
Now, use this concept to solve a question. Given a list arr, of N positive integers, and a sum. The task is to check if any pair exists in the array whose sum is present in the array.

Example:

Input:  N = 7  , sum = 8  , arr = [1, 2, 3, 3, 5, 5, 5] 
Output: Yes

Explanation: Pair with sum 8 is present in the array which is (5, 3). '''





def pair_sum(dict, N, arr, sum):
    for x in arr:
        for y in range(1,N):
            if(x+arr[y]==sum):
                return True
    return False
