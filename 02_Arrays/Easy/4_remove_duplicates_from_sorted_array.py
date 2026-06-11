'''
Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once.
Return the number of unique elements in the array.

If the number of unique elements be k, then,
Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.
The driver code will assess correctness by printing and checking only the first k elements of the modified array.

Example 1
Input: nums = [0, 0, 3, 3, 5, 6]
Output: 4

Explanation:
Resulting array = [0, 3, 5, 6, _, _]
There are 4 distinct elements in nums and the elements marked as _ can have any value.

'''

#Approach One: Using Set
#Time Complexity: O(n + nlogn + n) = O(nlogn)
#Space Complexity: O(n)


def remove_duplicates(nums):
    my_set = set() #Stores unique elemnets in unsorted fashion

    #Add elements to the set 
    for num in nums:
        my_set.add(num)
    
    #Sort the set elements bcoz set elemnts are unordered
    sorted_nums = sorted(my_set) #Sorted returns a new sorted list
    
    #Put elements of sorted nums back to nums
    for i in range(len(sorted_nums)):
        nums[i] = sorted_nums[i]

    return i + 1 #Return number of unique elements

arr = [0, 0, 0, 1, 1, 2, 3, 4]
print(f"Number of unique elemnts are {remove_duplicates(arr)}")
print(f"Resulting array: {arr}\n\n")




#Approach 2nd: Using Two Pointer Approach
#Time Complexity: O(n)
#Space Complexity: O(1)

def remove_duplicates_using_2pointer(nums):
    k = 0 #Points to the location in nums where we put the unique elements

    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    return k + 1 #Return number of unqiue elements in the array

arr = [0, 0, 0, 1, 1, 2, 3, 4, 4, 70]
print(f"Number of unique elemnts are {remove_duplicates_using_2pointer(arr)}")
print(f"Resulting array: {arr}\n\n")


#Approach 03: Using Recursion
#Time Complexity: O(n)
#Space Complexity: O(n)

def remove_duplicates_recursive(nums, i=1, k=0):
    if i == len(nums):
        return k + 1
    
    if nums[i] != nums[k]:
        k += 1
        nums[k] = nums[i]


    return remove_duplicates_recursive(nums, i+1, k)


arr = [0, 0, 0, 1, 1, 2, 3, 4, 4, 70, 190]
print(f"Number of unique elemnts are {remove_duplicates_recursive(arr)}")
print(f"Resulting array: {arr}")

