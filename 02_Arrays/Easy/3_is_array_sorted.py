

'''
Given an array nums of n integers, return true if the array nums
is sorted in non-decreasing order or else false.
1 <= n <= 100
1 <= nums[i] <= 100
'''

#Approach One: Using iteration
#Time Complexity: O(n)
#Space Complexity: O(1)
def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]: #If voilation occur return False
            return False
        
    return True




arr = [1, 2, 4, 9, 0]
print(f"Is array sorted? {is_sorted(arr)}")