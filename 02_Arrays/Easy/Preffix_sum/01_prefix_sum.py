

'''
Problem Statement:
you're given an array and you need to compute prefix sum

Inclusive Prefix Sum
e.g [1, 2, 9, 0, 10, 11]
prefix: [1, 3, 12, 12, 22, 33]


Exclusive Prefix Sum
e.g [1, 2, 9, 0, 10, 11]
prefix: [0, 1, 3, 12, 12, 22, 33] #Size one greater than nums

'''


#Time Complexity: O(n)
#Space Complexity: O(n)
def subarray_sum_1(left, right, nums):

    #Perform inclusive prefix sum
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    
    if left == 0:
        prefix[right]

    #Return prefix sum b/w left and right both inclusive
    return prefix[right] - prefix[left - 1]





nums = [1, 2, 9, 0, 10, 11]
print(f"Prefix sum array is: {subarray_sum_1(1, 3, nums)}")




#Time Complexity: O(n)
#Space Complexity: O(n)
def subarray_sum_2(left, right, nums):

    #Perform exclusive prefix sum
    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]

    #Return prefix sum b/w left and right both inclusive
    return prefix[right + 1] - prefix[left]





nums = [1, 2, 9, 0, 10, 11]
print(f"Prefix sum array is: {subarray_sum_2(1, 3, nums)}")