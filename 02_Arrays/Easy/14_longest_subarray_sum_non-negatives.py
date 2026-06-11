

'''
Problem Statement:
Given an array of +ive (including 0) nums of size n and an integer k, find the length of the longest
sub-array and indices that sums to k. If no such sub-array exists, return 0 and [None, None]


Example 1
Input: nums = [10, 5, 2, 7, 1, 9],  k=15
Output: 4

Explanation:
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a
length of 4. This sub-array starts at index 1 and ends at index 4, and the
sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

'''

#Approach one: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def longest_subarray_sum_1(nums, k):
    subarray_length = 0 #Store length of subarray having maximum sum
    indices = [None] * 2 #Store indices of subarry having maximum sum

    for i in range(len(nums)):
        subarray_sum = 0 #Store maximum subarry array sum : Reset for each new i
        for j in range(i, len(nums)):
            subarray_sum += nums[j]

            #Check if subarray_sum > k, if so then break and we're sure starting
            #from current i we won't get subarray_sum == k bcoz we've only +ive integers
            if subarray_sum > k:
                break #Optimization technique applicable only for +ive numbers
            
            if subarray_sum == k:
                length = j - i + 1 #Compute length of subarray

                if length > subarray_length:
                    subarray_length = length

                    #Store indices of subarry having maximum sum
                    indices[0:2] = i, j
          

    return subarray_length, indices




nums = [10, 5, 2, 7, 1, 9]
print(f"Subarray lenght and indicies: {longest_subarray_sum_1(nums, 15)}")



#Approach one: Using Optimal : SLIDING WINDOW
#Time Complexity: O(n)
#Space Complexity: O(1)

def longest_subarray_sum_2(nums, k):
    left, right = 0, 0
    current_sum = 0
    max_length = 0

    while right < len(nums):
        current_sum += nums[right]

        # shrink window properly
        while left <= right and current_sum > k:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            max_length = max(max_length, right - left + 1)

        right += 1

    return max_length



nums = [5, 9, 2, 12]
print(f"Subarray lenght: {longest_subarray_sum_2(nums, 0)}")