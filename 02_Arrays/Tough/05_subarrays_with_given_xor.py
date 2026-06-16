
'''
Problem Statement: Count subarrays with given xor K

Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.


Example 1
Input : nums = [4, 2, 2, 6, 4], k = 6
Output : 4
Explanation : The subarrays having XOR of their elements as 6 are
[4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]

Example 2
Input :nums = [5, 6, 7, 8, 9], k = 5
Output : 2
Explanation : The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
'''


#Approach one: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)
def subarray_with_given_xor_1(nums, k):
    count = 0

    for i in range(len(nums)):
        current_xor = 0 #Rest current_xor
        for j in range(i, len(nums)):
            current_xor ^= nums[j]

            if current_xor == k:
                count += 1
    return count

nums = [4, 2, 2, 6, 4]
print(f"Number of such subarrays: {subarray_with_given_xor_1(nums, 6)}")



#Approach 2nd: Using Optimal
#Time Complexity: O(n)
#Space Complexity: O(n)

def subarray_with_given_xor_2(nums, k):
    current_xor = 0
    xor_map = {0: 1} #Current xor occurs ones
    count = 0

    for i in range(len(nums)):
        current_xor ^= nums[i]

        #Find x that will satisfy the equation x = xr ^ k
        x = current_xor ^ k

        #If x is in xor_map then we've a valid subarray
        if x in xor_map:
            count += xor_map.get(x)

        xor_map[current_xor] = xor_map.get(current_xor, 0) + 1

    return count

nums = [4, 2, 2, 6, 4]
print(f"Number of such subarrays: {subarray_with_given_xor_2(nums, 6)}")

