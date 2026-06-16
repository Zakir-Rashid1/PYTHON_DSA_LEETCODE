'''
Problem Statement: Merge Overlapping Subintervals
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals and return an array of the
non-overlapping intervals that cover all the intervals in the input.


Note: You can return the intervals in any order.


Example 1
Input: intervals = [[1,5],[3,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,5] and [3,6] overlap, so they are merged into [1,6].

Example 2
Input: intervals = [[5,7],[1,3],[4,6],[8,10]]
Output: [[1,3],[4,7],[8,10]]
Explanation: Intervals [4,6] and [5,7] overlap and are merged into [4,7]
'''

#Approach 01: Using Optimal Approach
#Time Complexity: O(nlogn)
#Space Complexity: O(n) 


def merge_overlapping_intervals(nums):
    # Step 1: Sort intervals based on start time
    nums.sort()
    merged = [nums[0]] # Store the first interval as the starting merged interval

    # Step 2: Process remaining intervals
    for i in range(1, len(nums)):
        #Hold current and last starts and ends
        current_start, current_end = nums[i]
        last_start, last_end = merged[-1]

         # If current interval overlaps with the last merged interval
        if current_start <= last_end:
            # Extend the end of the merged interval if needed
            merged[-1] = [last_start, max(last_end, current_end)] #One classical example is [[1, 4], [2, 3]] = [1, 4]
        else:
            # No overlap, start a new interval
            merged.append(nums[i])



    return merged


nums = [[1, 4], [2, 3]]
non_overlapping_intervals = merge_overlapping_intervals(nums)
print(f"Non overlapping intervals are: {non_overlapping_intervals}")