'''
Problem Statement: Search X in sorted array

Given a sorted array of integers nums with 0-based indexing, find the
index of a specified target integer. If the target is found in the array,
return its index. If the target is not found, return -1.


Example 1
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: The target integer 9 exists in nums and its index is 4

Example 2
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: The target integer 2 does not exist in nums so return -1

'''

# Approach: Iterative Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)


def bs_1(nums, target):
    # Search space is initially the entire array
    low, high = 0, len(nums) - 1

    while low <= high:

        # Middle index of the current search space
        mid = (low + high) // 2

        # Target found
        if nums[mid] == target:
            return mid

        # Target lies in the right half
        elif nums[mid] < target:
            low = mid + 1

        # Target lies in the left half
        else:
            # We use high = mid - 1 because
            # nums[mid] has already been checked.
            high = mid - 1

    # Target does not exist in the array
    return -1


nums = [-1, 2]
print(f"Index of target element is: {bs_1(nums, -10)}")


#Approach 01: Using Recursion
#Time Complexity: O(logn)
#Space Complexity: O(log(n))

# Approach: Recursive Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(log n)  # Due to recursion stack

def bs_2(nums, low, high, target):

    # Base case:
    # If the search space becomes empty,
    # the target does not exist in the array.
    if low > high:
        return -1

    # Middle index of the current search space
    mid = (low + high) // 2

    # Target found
    if nums[mid] == target:
        return mid

    # Target must lie in the right half
    elif nums[mid] < target:
        return bs_2(nums, mid + 1, high, target)

    # Target must lie in the left half
    else:
        return bs_2(nums, low, mid - 1, target)

nums = [-1, 2, 9, 0, 8, 3, 4, 5]
print(f"Index of target element is: {bs_2(nums, 0, len(nums) - 1, 110)}")

