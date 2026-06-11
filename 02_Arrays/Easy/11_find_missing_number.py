

"""
Problem Statement:
Given an integer array of size n containing distinct values in the range from 0 to n
(inclusive), return the only number missing from the array within this range.


Example 1
Input: nums = [0, 2, 3, 1, 4]
Output: 5

Explanation:
nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

"""


#Approach One: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def missing_number_1(nums):
    is_missing = 1 #Flag used to check which number is missing

    #Assume the missing number is the number that comes from full array
    for curr in range(len(nums) + 1): 
        for num in nums: #Now iterate through the given array
            if curr == num:
                is_missing = 0 #Set flag to 0, when it's not a missing number
                break
        
        #Check if current number is missing
        if is_missing:
            return curr
        is_missing = 1




nums = [0 , 3, 4, 2, 5]
print(f"Missing number is: {missing_number_1(nums)}")


#Approach 2nd: Using Optimal Approach
#Time Complexity: O(n)
#Space Complexity: O(1)

def missing_number_2(nums):
    #Length of orginal array
    length = len(nums) + 1 #Because one number is missing
    arr_sum = 0 #Array sum

    #Sum of first n whole numbers 
    total_sum = length * (length - 1) // 2

    #Given array sum
    for num in nums:
        arr_sum += num

    return total_sum - arr_sum # Return missing number


nums = [0 , 1, 4, 2, 5]
print(f"Missing number is: {missing_number_2(nums)}")



#Approach 3rd: Using XOR (Most Optimal)
#Time Complexity: O(2n) = O(n)
#Space Complexity: O(1)

def missing_number_3(nums):
    xor1 = 0 #Stores XOR of given numbers : one Missing
    xor2 = 0 #Stores XOR of orginal numbers: nothing is missing

    #XOR of given numbers
    for num in nums:
        xor1 = xor1 ^ num

    #XOR of orginal numbers
    for i in range(len(nums) + 1):
        xor2 = xor2 ^ i

    return xor1 ^ xor2 #Return missing number


nums = [0 , 1, 4, 2, 5]
print(f"Missing number is: {missing_number_3(nums)}")




#Approach 4nd: Using XOR (Most Optimal) : Same logic as above with only differenece
#             That it uses only one loop
#Time Complexity: = O(n)
#Space Complexity: O(1)
def missing_number_5(nums):
    xor1 = 0 #Stores XOR of given numbers : one Missing
    xor2 = 0 #Stores XOR of orginal numbers: nothing is missing

    for i in range(len(nums)):
        xor2 = xor2 ^ i #It computes the XOR for only 0 1 2 3 4 5 is missing
        xor1 = xor1 ^ nums[i] #Performs XOR of given array

    xor2 = xor2 ^ len(nums) #Last element was missing that's equal to the array length

    return xor1 ^ xor2 #Return missing number


nums = [0 , 1, 4, 2, 5]
print(f"Missing number is: {missing_number_5(nums)}")