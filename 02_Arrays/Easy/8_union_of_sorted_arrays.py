

'''
Problem Statement:
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are present in either
the first array, the second array, or both.


Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]

Explanation:
The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2
'''




#Approach One: Using Dictionary
#Time Complexity: O[(m + n) + klogk] = O(klogk) = O[(m + n) log(m + n)]
#       m = len(nums1) , n = len(nums2) and k = no. of unique elements (k <= (m + n))
#Space Complexity: O[(m + n) + (k)] = O[(m + n)] k: dictionary size (k <= (m + n))

def union_1(nums1, nums2):
    '''
    The reason why i don't use set here is bcoz, sets are unordered and i need
    union in sorted order, that's why i used dictionary, in which i store the keys

    '''
    seen = {}
    union = [] #Store union of arrays

    #Store nums in dictionaries
    def helper(nums):
        #Iterate over nums1 and nums2 to store their elements as keys in keys dict.
        for num in nums:
            seen[num] = ""

    #It doesn't matter weather you store num1 first then nums2 bcoz we sort it later
    helper(nums1)
    helper(nums2)
   
    #Iterate over keys only
    for key in seen:
        union.append(key) #Append keys to the union 


    union.sort()
    return union


nums1 = [10, 20, 30, 40, 50]
nums2 = [-1, 2, 35, 900]
print(f" Union of two given sorted arrays is: {union_1(nums1, nums2)}")




#Approach 02: Using Merge and Remove Duplicates
#Time Complexity: O[(m + n) + O(m + n)] = O[(m + n)]
#Space Complexity: O[(m + n) + k] = O[(m + n)] : k no. of unqiue elemets in the array
def union_2(nums1, nums2):
    nums3 = []

    #Remove duplicates from the sorted array
    def remove_duplicates(nums):
        i = 0
        j = i + 1

        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1 #Length of unqiue elements


    #Merge two sorted arrays
    i , j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1

    #Copy remaning elements
    while i < len(nums1):
        nums3.append(nums1[i])
        i += 1
    while j < len(nums2):
        nums3.append(nums2[j])
        j += 1

    #Remove duplicates
    length = remove_duplicates(nums3)
        
    return nums3[0:length] #Creating new array whose length is number of unique elements in array

nums1 = [1, 2, 3, 4, 5]; nums2 = [1, 2, 7]
print(f" Union of two given sorted arrays is: {union_2(nums1, nums2)}")



#Approach 03: Using 2 Pointer Method
#Time Complexity: O[(m + n)]
#Space Complexity: O[(m + n)]
def union_3(nums1, nums2):
    union = []
    i , j = 0, 0
  
    #It's same as merging two sorted arrays with one additional checking
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]: 
            if not union or nums1[i] != union[-1]:
                union.append(nums1[i])
            i += 1
        else:
            if not union or nums2[j] != union[-1]:
                union.append(nums2[j])
            j += 1

    #Now insert remainig elements
    while i < len(nums1):
        if nums1[i] != union[-1]:
            union.append(nums1[i])
            i += 1

    while j < len(nums2):
        if nums2[j] != union[-1]:
            union.append(nums2[j])
            j += 1

    return union

        

nums1 = [1, 2, 3, 4, 5]; nums2 = [1, 2, 7]
print(f" Union of two given sorted arrays is: {union_3(nums1, nums2)}")

