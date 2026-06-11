


'''
Probalem Statement:

Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

Example 1
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
Output: nums = [3, 4, 5, 6, 1, 2]

Explanation:
rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

Example 2

Input: nums = [3, 4, 1, 5, 3, -5], k = 8
Output: nums = [1, 5, 3, -5, 3, 4]

Explanation:
rotate 1 step to the left: [4, 1, 5, 3, -5, 3]
rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]
rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]
rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]
rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]
rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]
rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]
rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]
'''

#Approach One: Using brute force
#Time Complexity: O(kn)
#Space Complexity: O(1)


def left_rotate_1(nums, k): #k : number of rotations
    '''
    If k > len(nums) say k = 35 and len(nums) = 10, then 35 can be written as
    (10 + 10 + 10 + 5) after 10 rotations the becomes same as given in input
    so i can say.  (3*10 + 5 )mod 10 = 5
    '''
    k = k % len(nums) 

    while k:
        first_element = nums[0]

        #Shift all the elements starting from index one to the left
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        
        #Now put the first element at last
        nums[-1] = first_element
        k -= 1

arr = [1, 2, 3, 4, 5, 6]
left_rotate_1(arr, 89)
print(f"Rotated array is: {arr}")


#Approach Second: Using Better method
#Time Complexity: O(k) + O(n - k) + O(k) = O(k + n -k + k) = O(n + k) = O(n) : k <= n
#Space Complexity: O(k)

def left_rotate_2(nums, k):
    k = k % len(nums)

    temp = [] #temp array stores the elements which i need to rotate
    for i in range(k):
        temp.append(nums[i])

    #Shift the non rotating elemnets in nums array
    for i in range(k, len(nums)):
        nums[i - k] = nums[i]

    #Copy the rotating elements from temp array to the orginal array nums
    for j in range(len(temp)):
        nums[len(nums) - k + j] = temp[j]

arr = [1, 2, 3, 4, 5, 6]
left_rotate_2(arr, 2)
print(f"Rotated array is: {arr}")



#Approach Third: Using Optimal approach
#Time Complexity: O(n + n) = O(n)
#Space Complexity: O(1)

def left_rotate_3(nums, k):
    k = k % len(nums) #Bcoz 2 mod 6 = 2 ::: 10 mod 6 = 4

    #Function used to reverse an array in O(n) time
    def reverse_array(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    #Reverse array in parts
    reverse_array(0, k - 1)
    reverse_array(k, len(nums) - 1)
    #Reverse whole array
    reverse_array(0, len(nums) - 1)


arr = [3, 4, 1, 5, 3, -5]
left_rotate_3(arr, 8)
print(f"Rotated array is: {arr}")