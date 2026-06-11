


'''
Problem Statement:
Given an array nums of size n and an integer k, find the length of the longest
sub-array that sums to k. If no such sub-array exists, return 0.


Input: nums = [-3, 2, 1], k=6
Output: 0

Explanation:
There is no sub-array in the array that sums to 6. Therefore, the output is 0.
'''

#Approach one: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)
def longest_subarray_sum_1(nums, k):
    subarray_length = 0 #Store length of subarray having maximum sum

    for i in range(len(nums)):
        curr_sum = 0 #Store maximum subarry array sum : Reset for each new i
        for j in range(i, len(nums)):
            curr_sum += nums[j]
 
            if curr_sum == k:
                length = j - i + 1 #Compute length of subarray
                subarray_length = max(subarray_length, length)

          

    return subarray_length



nums = [-3, 2, 1]
print(f"Longest subarray lenght: {longest_subarray_sum_1(nums, 0)}")



#Approach 2nd: Using hashmap
#Time Complexity: O(n)
#Space Complexity: O(n)

def longest_subarray_sum_2(nums, k):

    current_sum = 0
    max_length = 0
    prefix_map = {}


    for i in range(len(nums)):
        current_sum += nums[i] # Update running prefix

        # Case 1:
        # Subarray from index 0 to i
        if current_sum == k:
            max_length = i + 1

        remaning = current_sum - k

        # (If remaning) exists in prefix_map then we've a valid subarray
        if remaning in prefix_map:
            current_length = i - prefix_map[remaning] # Calculate current subarray length
            max_length = max(current_length, max_length)

        '''
        Store first occurrence of prefix sum only.
        We do NOT update existing values because
        earlier index gives longer subarray length
        '''
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_length

    
nums = [3, -2, -1]
print(f"Longest subarray lenght: {longest_subarray_sum_2(nums, 0)}")
