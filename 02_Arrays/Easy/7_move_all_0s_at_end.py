


'''
Problem Statement:
Given an integer array nums, move all the 0's to the end of the array.
The relative order of the other elements must remain the same.
This must be done in place, without making a copy of the array.


Example 1
Input: nums = [0, 1, 4, 0, 5, 2]
Output: [1, 4, 5, 2, 0, 0]

'''

#Approach 01: Using Brute force
#Time Complexity: O[x + x + (n - x)] = O[(n + x)] = O(n) : In worst case x = n
                # x: Number of non zero elements
#Space Complexity: O(x) = O(n) : In worst case x = n

def move_zeroes_end_1(nums):
    temp = [] #Store non zero elements

    for i in range(len(nums)):
        if nums[i] != 0:
            temp.append(nums[i])

    #Now store back non zero element from temp to nums
    for i in range(len(temp)):
        nums[i] = temp[i]

    #Append 0's at the end of nums : Number of 0's = len(nums) - len(temp) 
    for i in range(len(temp), len(nums)):
        nums[i] = 0

nums = [0, 1, 4, 0, 5, 2]
move_zeroes_end_1(nums)
print(nums)

#Approach 02: Using Optimal Method : 2 pointer approach
#Time Complexity: O[x + x + (n - x)] = O[(n + x)] = O(n) : In worst case x = n
                # x: Number of non zero elements
#Space Complexity: O(x) = O(n) : In worst case x = n

def move_zeroes_end_2(nums):
    # j pointer will point the location that contains first 0
    j = -1
    for k in range(len(nums)):
        if nums[k] == 0:
            j = k
            break
    
    #Check if j == -1 if this holds then there is no zero element hence, return
    if j == -1:
        return
    
    #Second pointer 'i' will simply iterate the list
    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


nums = [0, 1, 4, 0, 5, 2]
move_zeroes_end_2(nums)
print(nums)