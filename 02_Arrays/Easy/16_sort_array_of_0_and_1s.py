
'''
Problem Statement:
You're given an array of zeros and ones only and you need to sort them

e.g [0, 1, 1, 0, 1, 0]
Return [0, 0, 0, 1, 1, 1]

Note: Sorting should be done inplace
'''



#Approach 01: Using Inbuilt sorting function
#Time Complexity: O(nlogn)
#Space Complexity: O(1)


def sort_0s_and_1s_1(nums):
    nums.sort()

    return nums


nums = [0, 1, 1, 0, 1, 0]
print(f"Sorted array is: {sort_0s_and_1s_1(nums)}")


#Approach 01: Using Counters
#Time Complexity: O(n)
#Space Complexity: O(1)

def sort_0s_and_1s_2(nums):
    zeros_count = 0 #Count number of zeros
    ones_count = 0 #Count number of ones

    #Check for each element and increment counts respectivelly
    for num in nums:
        if not num: #Condition for zero_count
            zeros_count += 1

    #Add right number of zeros
    for i in range(zeros_count):
        nums[i] = 0

    #Add right number of ones
    for j in range(zeros_count, len(nums), 1):
        nums[j] = 1

    return nums


nums = [0, 1, 1, 0, 1, 0]
print(f"Sorted array is: {sort_0s_and_1s_2(nums)}")


#Approach 01: Using Two Pointer Approach
#Time Complexity: O(n)
#Space Complexity: O(1)

def sort_0s_and_1s_3(nums):
    left = 0 #Holds the right index where i need to insert 0
    right = 0 #Iterates through the array

    while right < len(nums):
        if nums[right] == 0:
            #Swap only when they're pointing to different indices
            if left != right:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
  
        right += 1

    return nums
        
nums = [1, 1, 0, 0]
print(f"Sorted array is: {sort_0s_and_1s_3(nums)}")
        
        