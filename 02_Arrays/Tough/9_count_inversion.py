'''
Problem Statement: Count Inversions
Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.

A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.

Example 1

Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5

Explanation:
The responsible indexes are:
nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5



                            [9, 8, 7, 2, 1, 0, 7, 8, 12]

                         [9, 8, 7, 2, 1]                 [0, 7, 8, 12]

                [9, 8]             [7, 2, 1]         [0, 7]         [8, 12]

            [9]      [8]         [7]    [2, 1]      [0]       [7]   [8]       [12]                        [1, 0].    [7]
        
                                      [2]   [1]                            
    


'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def count_inversions_1(nums):
    count = 0 #Count number of inversions

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1

    return count

nums = [2, 3, 7, 1, 3, 5]
print(f"Number of inversions are: {count_inversions_1(nums)}")









#Approach 02: Using Divide and Conquer
#Time Complexity: O(nlogn)
#Space Complexity: O(n)

#Note: DONOT USE GLOBAL VARIABLES IN ANY DSA CODE

# Merge two sorted halves and count inversions
def merge(nums, low, mid, high):

    inversions = 0
    temp = []

    left = low
    right = mid + 1

    # Merge the two sorted halves
    while left <= mid and right <= high:

        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1

        else:
            # All remaining elements in left half
            # form inversions with nums[right]
            inversions += (mid - left + 1)

            temp.append(nums[right])
            right += 1

    # Append remaining elements
    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    # Copy merged array back
    nums[low:high + 1] = temp

    return inversions
        



#Perfrom merge sort
def mergesort(nums, low, high):
    count = 0
    mid = (low + high) // 2

    if low < high:
        count += mergesort(nums, low, mid)
        count += mergesort(nums, mid + 1, high)
        count += merge(nums, low, mid, high)

    return count


def count_inversions_2(nums):
    return mergesort(nums, 0, len(nums) - 1)



nums = [-10, -5, 6, 11, 15, 17]
print(f"Number of inversions are: {count_inversions_2(nums)}")
