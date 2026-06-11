

'''
Problem Statement: Rearrange array elements by sign

Given an integer array nums of even length consisting of an equal number of positive and
negative integers.Return the answer array in such a way that the given conditions are met:
Every consecutive pair of integers have opposite signs.


For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.



Example 1

Input : nums = [2, 4, 5, -1, -3, -4]
Output : [2, -1, 4, -3, 5, -4]

Explanation:
The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4
maintain their relative positions

'''

#Approach 01: Using Two Loops
#Time Complexity: O(n)
#Space Complexity: O(n)
def rearrange_pos_and_neg_1(nums):
    postives = []
    negatives = []


    #Store +ives and negatives seperately
    for num in nums:
        if num >=0 :
            postives.append(num)
        else:
            negatives.append(num)

    for i in range(len(nums) // 2):
        nums[2 * i] = postives[i] # +ive elements are at indices 0 2 4 6 ... etc 
        nums[2*i + 1] = negatives[i] # -ive elements are at indices 1 3 5 7 .. etc



nums = [1, 2, -3, -5]
rearrange_pos_and_neg_1(nums)
print(f"After modification nums becomes: {nums}")



#Approach 02: Using Single Loop
#Time Complexity: O(n)
#Space Complexity: O(n)
def rearrange_pos_and_neg_1(nums):
    temp = [None] * len(nums) 
    pos_index = 0 #Index for postive numbers
    neg_index = 0 #Index for negative numbers

    for i in range(len(nums)):
        if nums[i] >= 0:
            temp[2 * pos_index] = nums[i] # +ive elements are at indices 0 2 4 6 ... etc 
            pos_index += 1
        else:
            temp[2*neg_index + 1] = nums[i] # -ive elements are at indices 1 3 5 7 .. etc
            neg_index += 1

    return temp


nums = [2, 4, 5, -1, -3, -4]
print(f"After modification nums becomes: {rearrange_pos_and_neg_1(nums)}")