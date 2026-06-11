'''
Problem Statement: Sort an Array of 0's, 1's and 2's
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.


Example 1

Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]

Explanation:
The nums array in sorted order has 2 zeroes, 2 ones and 1 two

'''

#Approach 01: Using Comparasion Based Sorting
#Time Complexity: O(nlogn)
#Space Complexity: O(logn)
def sort_012_1(nums, low, high):

    # Base condition
    if low < high:

        # Partition index
        pivot_index = partition(nums, low, high)

        # Sort left half
        sort_012_1(nums, low, pivot_index)

        # Sort right half
        sort_012_1(nums, pivot_index + 1, high)


def partition(nums, low, high):

    # Choose first element as pivot
    pivot = nums[low]

    # Start outside boundaries
    i = low - 1
    j = high + 1

    while True:

        # Move from left until element >= pivot
        i += 1
        while nums[i] < pivot:
            i += 1

        # Move from right until element <= pivot
        j -= 1
        while nums[j] > pivot:
            j -= 1

        # Pointers crossed
        if i >= j:
            return j

        # Swap misplaced elements
        nums[i], nums[j] = nums[j], nums[i]




nums = [1, 0, 2, 1, 0]
sort_012_1(nums, 0, len(nums)-1)
print(nums)


#Approach 02: Using Counters
#Time Complexity: O(n)
#Space Complexity: O(1)


def sort_012_2(nums):
    zeroes_count, ones_count, twos_count = 0, 0, 0
    for num in nums:
        if not num: # Count number of zeroes
            zeroes_count += 1
        elif num == 1: # Count number of ones
            ones_count += 1
        else:
            twos_count += 1 # Count number of twos

    #Put back into nums
    i = 0
    while zeroes_count or ones_count or twos_count:
        if zeroes_count:
            nums[i] = 0
            zeroes_count -= 1
        elif ones_count:
            nums[i] = 1
            ones_count -= 1
        else:
            nums[i] = 2
            twos_count -= 1
        i += 1


nums = [1, 0, 2, 1, 0]
sort_012_2(nums)
print(nums)
    


#Approach 02: Using Dutch National Flag (3 Pointer Approach)
#Time Complexity: O(n)
#Space Complexity: O(1)


def sort_012_3(nums):
    low, mid, high = 0, 0, len(nums) - 1

    #Keep moving as long as mid <= high
    while mid <= high:

        # If nums[mid] == 0 then swap nums[mid] with nums[low] because from
        # 0 to low - 1 array contains only zeroes
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        # If nums[mid] == 1 then only increment mid because from low to mid - 1
        # array contains only ones
        if nums[mid] == 1:
            mid += 1

        # If nums[mid] == 2 then swap nums[mid] with nums[high] because from
        # high + 1 to len(nums) - 1 array contains only twos
        if nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

        

nums = [1, 0, 2, 1, 0]
sort_012_2(nums)
print(nums)
    
