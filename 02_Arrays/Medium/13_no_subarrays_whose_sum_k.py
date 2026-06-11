'''
Problem Statement: Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

'''


#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def no_of_subarray_sum_k_1(nums, k):
    count = 0 #Count number of subarrays whose sum is k

    #Generate all possible subarrays
    for i in range(len(nums)):
        prefix_sum = 0 # Hold prefix sum

        for j in range(i, len(nums)):
            prefix_sum += nums[j]

            #Check if prefix_sum is equal to k
            if k == prefix_sum:
                count += 1 
            

    return count


nums = [1,2,3, 0, 0]
print(f"Number of such subarrays: {no_of_subarray_sum_k_1(nums, 3)}")


#Approach 02: Using Hashmap
#Time Complexity: O(n)
#Space Complexity: O(n)

def no_of_subarray_sum_k_2(nums, k):
    prefix_sum = 0
    # Prefix map stores prexfix sum and its frequency, prefix sum is initilized with 0
    #hence prefix sum 0 occurs 1 time that's y its initilized with {0: 1}
    prefix_map = {0: 1} 
    count = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        #The remaning part that we check was it the prefix sum earlier
        remaning = prefix_sum - k  

        # If remaning is in prefix map that means we've a valid subarray
        if remaning in prefix_map:
            count += prefix_map.get(remaning)

        # Store the frequency of prefix_sum 
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        '''
        Note: if we've nums=[0] and k = 0 and we print prefix_sum we will get
        {0:2} that means we've seen prefix sum of 0 twice one is bcoz of array
        and one is initially when prefix_sum was initialized
        '''
    return count
        
    

nums = [1, 1, 1]
print(f"Number of such subarrays: {no_of_subarray_sum_k_2(nums, 2)}")