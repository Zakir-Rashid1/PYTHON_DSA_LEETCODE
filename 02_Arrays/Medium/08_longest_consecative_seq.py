'''
Problem Statement: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''


#Approach 01: Using Bruteforce
#Time Complexity: O(n^3)
#Space Comeplexity: O(1)

'''
Suppose the sequence is [1, 6, 4, 3, 5, 2]

    num = 1
    count_consecutive_from function will take O(n^2) time

    slly when num = 6
    count_consecutive_from function will take O(n^2) time

    .
    .
    .

    Therefore total time complexity is O(n^3)
'''


# This function does simple linear search takes O(n) time
def is_present(nums, target):
    for num in nums:
        if num == target:
            return True

    return False


# This function finds the length of consecative sequence starting from target
def count_consecutive_from(nums, target):
    length = 1
    while is_present(nums, target):
        length += 1
        target += 1 #Increment target to the new target

    return length


def longest_consecutive_seq_1(nums):
    max_length = 1

    for num in nums:
        current_length = count_consecutive_from(nums, num + 1)
        max_length = max(max_length, current_length)

    return max_length


nums = [0,3,7,2,5,8,4,6,0,1]
print(f"Length of longest consecative sequence is: {longest_consecutive_seq_1(nums)}")





#Approach 02: Using Sorting
#Time Complexity: O(nlogn)
#Space Comeplexity: O(1)

def longest_consecutive_seq_2(nums):
    nums.sort() # Performs inplace sorting
    length = 1
    max_length = 1

    for i in range(1, len(nums)):
        #Ignore duplicates
        if nums[i] == nums[i - 1]:
            continue
        elif nums[i]  == nums[i - 1] + 1:
            length += 1
        else:
            length = 1 #Consecative sequence was broken, hence start as fresh

        #Update maximum length
        max_length = max(max_length, length)

    return max_length

nums = [1, 2, 2, 3]
print(f"Length of longest consecative sequence is: {longest_consecutive_seq_2(nums)}")



#Approach 02: Using Set Datastructure
# Time Complexity: O(n)
# Space Complexity: O(n)

def longest_consecutive_seq_3(nums):
    unique_nums = set(nums)
    max_length = 1

    for num in unique_nums:
        prev_num = num - 1

        # Start looking from the the num whose previous is not present
        if prev_num not in unique_nums:
            current_num = num
            current_length = 1

            #Compute current length
            while current_num + 1 in unique_nums:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


nums = [0,3,7,2,5,8,4,6,0,1]
print(f"Length of longest consecative sequence is: {longest_consecutive_seq_3(nums)}")
