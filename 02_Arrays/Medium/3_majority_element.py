

'''
Problem Statement: Majority Element in an Array
Given an integer array nums of size n, return the majority element of the array.

The majority element of an array is an element that appears more than n/2 times in
the array. The array is guaranteed to have a majority element.


Example 1

Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
Output: 7

Explanation:
The number 7 appears 5 times in the 9 sized array

'''



#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)


def majority_element_1(nums):
    count = 0

    for i in range(len(nums)):
        curr_element = nums[i] # Pick current element

        for j in range(len(nums)):
            if nums[j] == curr_element:
                count += 1

        # Check if current element appers morethan n/2 times
        if count > len(nums) // 2:
            return curr_element
        
        count = 0 #Reset count

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(f"Element that appears morethan n/2 times is: {majority_element_1(nums)}")



#Approach 02: Using Sorting
#Time Complexity: O(nlogn)
#Space Complexity: O(n)


def majority_element_2(nums):
    # Sort array : Python uses Time Sort which is a combination of insertion sort
    # and merge sort hence requires extra space of O(n)
    nums.sort() 

    return nums[len(nums) // 2]

nums = [7, 0, 0, 1, 7, 7, 2, 7]
print(f"Element that appears morethan n/2 times is: {majority_element_2(nums)}")



#Approach 03: Using Hash
#Time Complexity: O(n)
#Space Complexity: O(n)


def majority_element_3(nums):
    freq = {}

    # Count frequiency of each element
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

        #Now check which element has frequiency greater than n // 2
        if freq[num] > len(nums) // 2:
            return num
        

nums = [7, 0, 0, 1, 7, 7, 7, 7]
print(f"Element that appears morethan n/2 times is: {majority_element_3(nums)}")


#Approach 04: Using Moores Voting Algorithm
#Time Complexity: O(n)
#Space Complexity: O(1)

'''
Moores voting algo. only gives us candidate for majority elements, it only guarentees
to return the majority element only when there exists one. If there is none then
we need to check using one more loop

'''
def majority_element_4(nums):

    candidate = None
    count = 0

    for num in nums:
        # Choose new candidate : when count == 0 that means our choosen candidate was not majority
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

nums = [7, 1, 1, 1]
print(f"Element that appears morethan n/2 times is: {majority_element_4(nums)}")