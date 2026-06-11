'''

Problem Statement: Leaders in an Array
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all
elements to its right in the given array. The rightmost element is always a
leader. The elements in the leader array must appear in the order they appear in the nums array.


Example 1
Input: nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]
Explanation:
2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

Example 2
Input: nums = [-3, 4, 5, 1, -4, -5]
Output: [5, 1, -4, -5]
Explanation:
-5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]

'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)


def leaders_in_an_array_1(nums):
    leaders = [] #Stores all leaders

    for i in range(len(nums)):
        curr_number = nums[i] #Pick the current number
        is_leader = True #Assume each element is the leader

        #Now check weather the current number is the leader or not
        for j in range(i + 1, len(nums)):
            # If any greater or equal element exists, current number is not a leader
            if nums[j] > curr_number:
                is_leader = False
                break

        if is_leader:
            leaders.append(curr_number)

    return leaders

nums = [-3, 4, 5, 1, -4, -5]
print(f"Learders of given array is: {leaders_in_an_array_1(nums)}")



#Approach 01: Using Observation
#Time Complexity: O(n)
#Space Complexity: O(n) : In worst case

def leaders_in_an_array_2(nums):
    leaders = []
    max_from_right = float('-inf')

    for i in range(len(nums)-1, -1, -1):
        if nums[i] > max_from_right:
            leaders.append(nums[i])

            # Update max from right
            max_from_right = nums[i]

    leaders.reverse() # Reverse leaders

    return leaders
        
        
nums = [-3, 4, 5, 1, -4, -5]
print(f"Learders of given array is: {leaders_in_an_array_2(nums)}")


