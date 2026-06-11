


'''
Problem Statement:
Given an array of nums of n integers. Every integer in the array appears twice except one integer.
Find the number that appeared once in the array.


Example 1
Input : nums = [1, 2, 2, 4, 3, 1, 4]
Output : 3

Explanation : The integer 3 has appeared only once.

'''

#Approach one: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def single_number_1(nums):
    count = 0

    #Take a number and check if that appears morethan ones
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        #Check if count is equal to 1
        if count == 1:
            return nums[i]
        count = 0 #Reset count


nums = [1, 2, 2, 4, 3, 1, 4]
print(f"Number that appears only ones: {single_number_1(nums)}")




#Approach 2nd: Using Sorting
#Time Complexity: O(nlogn + n//2) = O(nlogn)
#Space Complexity: O(1)


def single_number_2(nums):
    nums.sort() # Sort nums in increasing order
    i = 0

    #Now check if nums[i] == nums[i + 1]
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            i += 2
        else:
            return nums[i]
        
    return nums[-1] #If nothing gets returned in the while loop then last element is unique


nums = [1, 2, 2, 4, 3, 1, 4]
print(f"Number that appears only ones: {single_number_2(nums)}")


#Approach 3rd: Using Hashmap
#Time Complexity: O(n)
#Space Complexity: O(n//2) = O(n)


def single_number_3(nums):
    hash = {}

    for num in nums:
        hash[num] = hash.get(num, 0) + 1

    for key, value in hash.items():
        if value == 1:
            return key
        

nums = [1, 2, 2, 4, 3, 1, 4]
print(f"Number that appears only ones: {single_number_3(nums)}")


#Approach 4rd: Using XOR
#Time Complexity: O(n)
#Space Complexity: O(1)

def single_number_4(nums):
    unique_number = 0

    for num in nums:
        unique_number = unique_number ^ num

    return unique_number


nums = [1, 2, 2, 4, 3, 1, 4]
print(f"Number that appears only ones: {single_number_4(nums)}")
