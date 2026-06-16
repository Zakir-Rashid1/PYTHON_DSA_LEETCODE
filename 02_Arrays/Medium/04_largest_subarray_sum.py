'''
Problem Statement: Largest Subarray Sum
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''


#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)


def largest_subarray_sum_1(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        current_sum = 0 #Candidate for maximum sum

        for j in range(i, len(nums)):
            current_sum += nums[j] # Compute current sum

            #Hold maximum among max_sum and current_sum
            max_sum = max(max_sum, current_sum)

    return max_sum


nums = [5,4,-1,7,8]
print(f"Maximum subarray sum is: {largest_subarray_sum_1(nums)}")


#Approach 02: Using Kadans Algo
#Time Complexity: O(n)
#Space Complexity: O(1)


'''
Kadane says:
If current sum becomes negative, it can never help future subarrays.
Because adding a negative prefix only decreases future sums.
'''
# Approach 2: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

def largest_subarray_sum_2(nums):
    max_sum = float('-inf')
    current_sum = 0 # Running sum of current subarray
    
    for num in nums:
        current_sum += num # Extend current subarray
        max_sum = max(max_sum, current_sum) # Update global maximum

        # If current sum becomes negative, discard it and start fresh
        if current_sum < 0:
            current_sum = 0

    return max_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]
print(f"Maximum subarray sum is: {largest_subarray_sum_2(nums)}")