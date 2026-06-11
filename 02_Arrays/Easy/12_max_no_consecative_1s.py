


'''
Problem Statement:
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.


Example 1
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
Output: 3

Explanation:
The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s
'''

#Approach one: Using Optimal 
#Time Complexity: O(n)
#Space Complexity: O(1)

def max_consecative_1s(nums):
    max_count = 0 #Store maximum number of consecative 1s
    count = 0 #Stores number of consecative 1s

    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0 #Rest count 

    return max_count

nums = [1,1,0,0,1,1,1,1,1,1,0,1,1,1,0]
print(f" Number of maximum consecative 1's are: {max_consecative_1s(nums)}")