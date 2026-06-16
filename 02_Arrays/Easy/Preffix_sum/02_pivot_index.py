
'''
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of
the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

'''


#Approach One: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def pivot_index_1(nums):

    for i in range(len(nums)):
        left_sum, right_sum = 0, 0

        #Compute left sums
        for j in range(i - 1, -1, -1):
            left_sum += nums[j]

        #Compute right sum
        for k in range(i + 1, len(nums), 1):
            right_sum += nums[k]
    

        if left_sum == right_sum:
            return i #Return pivot index


    return -1 #Return -1 if there's no pivot index
nums = [1,7,3,6,5,6]
print(f"Pivot index is: {pivot_index_1(nums)}")


#Approach One: Using Prefix Sum
#Time Complexity: O(n)
#Space Complexity: O(1)

def pivot_index_2(nums):

    # Total sum of the array
    total_sum = sum(nums)

    # Running sum of elements on the left side
    left_sum = 0

    for i in range(len(nums)):

        # Right sum = total sum - current element - left sum
        right_sum = total_sum - left_sum - nums[i]

        # Pivot condition
        if left_sum == right_sum:
            return i

        # Update left sum for next iteration
        left_sum += nums[i]

    # No pivot index found
    return -1


nums = [2,1,-1]
print(f"Pivot index is: {pivot_index_2(nums)}")