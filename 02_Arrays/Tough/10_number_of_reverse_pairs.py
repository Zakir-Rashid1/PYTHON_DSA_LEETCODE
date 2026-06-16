'''
Problem Statement: Number of Reverse Pairs

Given an integer array nums. Return the number of reverse pairs in the array.
An index pair (i, j) is called a reverse pair if:
0 <= i < j < nums.length
nums[i] > 2 * nums[j]

Example 1
Input: nums = [6, 4, 1, 2, 7]
Output: 3

Explanation:
The reverse pairs are:
(0, 2) : nums[0] = 6, nums[2] = 1, 6 > 2 * 1
(0, 3) : nums[0] = 6, nums[3] = 2, 6 > 2 * 2
(1, 2) : nums[1] = 4, nums[2] = 1, 4 > 2 * 1
'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def num_reverse_pairs_1(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > 2 * nums[j]:
                count += 1

    return count

nums = [6, 4, 1, 2, 7]
print(f"Number of reverse paris are: {num_reverse_pairs_1(nums)}")







#Approach 02: Using Divide & Conquer
#Time Complexity: O()
#Space Complexity: O(n)

def merge(nums, low, mid, high):

    reverse_pairs = 0

    # ------------------------------------------------------------------
    # STEP 1: Count reverse pairs between the two sorted halves
    # Left half  : nums[low ... mid]
    # Right half : nums[mid+1 ... high]
    
    # We need to count pairs (i, j) such that:
    # nums[i] > 2 * nums[j]
    
    # Since both halves are already sorted, we can use a two-pointer
    # technique and count all valid pairs in O(n) time.
    # ------------------------------------------------------------------

    right = mid + 1

    # Fix each element in the left half
    for left in range(low, mid + 1):

        # Move the right pointer until the reverse pair condition
        # becomes false.
        
        # Since the right half is sorted, once an element fails the
        # condition, all elements after it will also fail.
        while right <= high and nums[left] > 2 * nums[right]:
            right += 1

        # All elements from (mid + 1) to (right - 1)
        # satisfy:
        # nums[left] > 2 * nums[j]
        
        # Therefore, number of valid reverse pairs contributed by
        # nums[left] is:
        reverse_pairs += right - (mid + 1)

    # ------------------------------------------------------------------
    # STEP 2: Merge the two sorted halves
    # This is the standard merge operation used in Merge Sort.
    # After merging, nums[low ... high] becomes sorted.
    # ------------------------------------------------------------------

    temp = []

    left = low
    right = mid + 1

    # Compare elements from both halves and place the smaller one
    # into the temporary array.
    while left <= mid and right <= high:

        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    # Copy any remaining elements from the left half
    while left <= mid:
        temp.append(nums[left])
        left += 1

    # Copy any remaining elements from the right half
    while right <= high:
        temp.append(nums[right])
        right += 1

    # Copy the merged sorted array back to the original array
    nums[low:high + 1] = temp

    return reverse_pairs
        



#Perfrom merge sort
def mergesort(nums, low, high):
    count = 0
    mid = (low + high) // 2

    if low < high:
        count += mergesort(nums, low, mid)
        count += mergesort(nums, mid + 1, high)
        count += merge(nums, low, mid, high)

    return count


def num_reverse_pairs_2(nums):
    return mergesort(nums, 0, len(nums) - 1)


nums =[6, 4, 4, 2, 2]
print(f"Number of reverse paris are: {num_reverse_pairs_2(nums)}")



'''
NOTE:

In the "Count Inversions" problem, we can count inversions directly during
the merge step.

Reason:
If nums[left] > nums[right], then because the left half is already sorted,
all elements from left to mid will also be greater than nums[right].

Therefore, we can immediately add:

    (mid - left + 1)

inversions without checking each element individually.


However, the same technique DOES NOT work for the "Reverse Pairs" problem.

Reverse Pair Condition:

    nums[i] > 2 * nums[j]

Suppose:

    Left Half  = [2, 5]
    Right Half = [3]

During merge:

    2 <= 3

so no inversion exists.

But:

    5 > 2 * 3

is false.

Now consider:

    Left Half  = [4, 7]
    Right Half = [3]

During merge:

    4 > 3

which would make us count all remaining elements in the left half if we used
the inversion logic.

But:

    4 > 2 * 3  -> False
    7 > 2 * 3  -> True

Only one reverse pair exists, not two.

Therefore, when nums[left] > nums[right], we CANNOT conclude that all
remaining elements in the left half form reverse pairs.

The condition depends on the value:

    2 * nums[right]

rather than just the ordering of elements.

Because of this, reverse pairs must be counted separately BEFORE merging
using a dedicated two-pointer scan over the two sorted halves.

This preserves the O(n log n) time complexity while ensuring correctness.
'''