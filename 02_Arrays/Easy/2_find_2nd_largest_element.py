

'''
Problem Statement:
Given an array of integers nums, return the second-largest element in the array.
If the second-largest element does not exist, return -1.
'''

#Approach One: Using Sorting -BRUTEFORCE
#Time Complexity: O(nlogn)
#Space Complexity: O(1)

def second_largest_sorted(nums):
    nums.sort() #Perfroms inplace sorting in increasing order

    largest = nums[-1]
    second_largest = None

    sindex = len(nums) - 2 #Start index

    #Find second largest start from len(nums) - 2
    for i in range(sindex, -1, -1):
        if nums[i] != largest:
            second_largest = nums[i]
            break

    return second_largest if second_largest is not None else -1


nums = [8, 8, 8, 8, 7, 9, 2, -12, 12]
print(f"Second largest element: {second_largest_sorted(nums)}")




#Approach 2nd: Using 2 Loops -BETTER
#Time Complexity: O(n)
#Space Complexity: O(1)

def second_largest_element_using_2loops(nums):
    largest = second_largest = float('-inf')

    #Find first largest element
    for num in nums:
        if num > largest:
            largest = num

    #Find 2nd largest element
    for num in nums:
        if num > second_largest and num != largest:
            second_largest = num

    return -1 if second_largest == float('-inf') else second_largest

nums = [8, 8, 8, 8, 8]
print(f"Second largest element: {second_largest_element_using_2loops(nums)}")



#Approach 2nd: Using 1 Loops -OPTIMAL
#Time Complexity: O(n)
#Space Complexity: O(1)


def second_largest_element_using_1loops(nums):
    largest = second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num


    return -1 if second_largest == float('-inf') else second_largest

nums = [8, 8, 8, 8, 8, 7, 77, 89, 0, 89]

print(f"Second largest element: {second_largest_element_using_1loops(nums)}")
