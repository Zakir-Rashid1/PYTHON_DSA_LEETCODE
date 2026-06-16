


'''
Probalem Statement:

Given an integer array nums and a non-negative integer k, rotate the array to the right by k steps.

Example 1
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
Output: nums = [5, 6, 1, 2, 3, 4]

Explanation:
rotate 1 step to the right: [6, 1, 2, 3, 4, 5]
rotate 2 steps to the right: [5, 6, 1, 2, 3, 4]

'''

#Approach One: Using brute force
#Time Complexity: O(kn)
#Space Complexity: O(1)


def right_rotate_1(nums, k): #k : number of rotations
    '''
    If k > len(nums) say k = 35 and len(nums) = 10, then 35 can be written as
    (10 + 10 + 10 + 5) after 10 rotations the becomes same as given in input
    so i can say.  (3*10 + 5 )mod 10 = 5
    '''
    k = k % len(nums) 
    while k:
        last_element = nums[-1]

        #Shift all the elements starting from index len(nums) - 1 to the right
        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i - 1]
        
        #Now put the last element at the first
        nums[0] = last_element
        k -= 1

arr = [1, 2, 3, 4, 5, 6]
right_rotate_1(arr, 39)
print(f"Rotated array is: {arr}")


#Approach Second: Using Better method
#Time Complexity: O(k) + O(n - k) + O(k) = O(k + n -k + k) = O(n + k) = O(n) : k <= n
#Space Complexity: O(k)

def right_rotate_2(nums, k):
    k = k % len(nums)
    nums_length = len(nums)

    temp = [] #temp array stores the elements which i need to rotate
    for i in range(nums_length - k, nums_length):
        temp.append(nums[i])

    #Shift right the non rotating elemnets in nums array
    j = 1
    for i in range(nums_length - k - 1, -1, -1):
        nums[nums_length - j] = nums[i]
        j += 1


    #Copy the rotating elements from temp array to the orginal array nums
    for j in range(len(temp)):
        nums[j] = temp[j]

arr = [1, 2, 3, 4, 5, 6]
right_rotate_2(arr, 3)
print(f"Rotated array is: {arr}")



#Approach Third: Using Optimal approach
#Time Complexity: O(n + n) = O(n)
#Space Complexity: O(1)

def right_rotate_3(nums, k):
    k = k % len(nums) #Bcoz 2 mod 6 = 2 ::: 10 mod 6 = 4

    #Function used to reverse an array in O(n) time
    def reverse_array(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    #Reverse array in parts
    reverse_array(0, len(nums) - k - 1)
    reverse_array(len(nums) - k, len(nums) - 1)
    #Reverse whole array
    reverse_array(0, len(nums) - 1)


arr = [3, 4, 1, 5, -3, -5]
right_rotate_3(arr, 2)
print(f"Rotated array is: {arr}")