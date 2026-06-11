


'''
Problem Statement: Unique Intersection (Duplicates Not Allowed)
Given two sorted arrays nums1 and nums2, return an array that contains the intersection of these two arrays.
The elements in the intersection must be in ascending order.


Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 2, 7]
Output: [1, 2]

'''

#Approach 01: Using Brute Force
#Time Complexity: O(mn) m: size of nums1 and n: size of nums2
#Space Complexity: O(k) k: size of intersection array

def intersection_1(nums1, nums2):
    intersection = []

    for i in range(len(nums1)):
        # skip duplicates in nums1
        if i > 0 and nums1[i] == nums1[i - 1]:
            continue
        
        #Find match in nums2 if found append that to intersection array and break
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                break

    return intersection


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 1, 1,  2, 2, 7]

print(f"Intersection of given two arrays is: {intersection_1(nums1, nums2)}")


#Approach 02: Using Better approach
#Time Complexity: O(m + n) m: size of nums1 and n: size of nums2
#Space Complexity: O(m + n) k: size of intersection array

def intersection_2(nums1, nums2):
    #Function used to remove duplicates
    def helper(nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1 #Return length of unique elements
    
    len_nums1 = helper(nums1)
    len_nums2 = helper(nums2)

    intersection = []
    freq = {}

    #Store each unique value as key and its value tells us the occurances
    for i in range(len_nums1):
        freq[nums1[i]] = freq.get(nums1[i], 0) + 1

    for i in range(len_nums2):
        freq[nums2[i]] = freq.get(nums2[i], 0) + 1

    #Now, check if the frequiency of occurance is == 2
    for key, value in freq.items():
        if value == 2:
            intersection.append(key)

    return intersection


nums1 = [1, 2, 3, 4, 5, 7, 7, 7]
nums2 = [-1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7, 7, 90]

print(f"Intersection of given two arrays is: {intersection_2(nums1, nums2)}")


#Approach 03: Optimal Using Two Pointer Approach
#Time Complexity: O(m + n) m: size of nums1 and n: size of nums2
#Space Complexity: O(1)


def intersection_3(nums1, nums2):
    intersection = []
    i, j = 0, 0 

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            # They are equal : not intersection is true only when intersection list is empty
            if not intersection or intersection[-1] != nums1[i]:
                intersection.append(nums1[i])
            
            # Increment both since we processed this match
            i += 1
            j += 1

    return intersection

nums1 = [1, 2, 3, 4, 5, 7, 7, 7]
nums2 = [-1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7, 7, 90]

print(f"Intersection of given two arrays is: {intersection_3(nums1, nums2)}")
                



