

'''
Problem Statement: Two Sum Problem
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''


#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def two_sum_1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

nums = [2,7,11,15]
target = 9
print(f"Indicies array is: {two_sum_1(nums, target)}")


#Approach 01: Using Hashmap
#Time Complexity: O(n)
#Space Complexity: O(n)

def two_sum_2(nums, target):
    hash = {}

    for i in range(len(nums)):
        second_num = target - nums[i] #Find second number

        #Check if second_num is not in hash
        if second_num not in hash:
            hash[nums[i]] = i
        else:
            return [hash[second_num], i]

        
nums = [2,7,11,15]
target = 9
print(f"Indicies array is: {two_sum_2(nums, target)}")
