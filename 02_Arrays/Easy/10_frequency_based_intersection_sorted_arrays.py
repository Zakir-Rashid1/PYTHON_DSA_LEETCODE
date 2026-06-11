'''
Problem Statement: Intersection (Duplicates Are Allowed)
Given two sorted arrays nums1 and nums2, return an array that contains the intersection of these two arrays.
The elements in the intersection must be in ascending order.


Example 1
Input: nums1 = [1, 2,2 , 3, 4, 5], nums2 = [1, 2, 2, 7]
Output: [1, 2, 2]

'''

#Approach One: Brute Force
#Time Complexity: O(mn)
#Space Complexity: O(k + n) = O(n): k length of inteersection array

"""
The length of visited_list is same of len(nums2) it's not necessary, i can also
make it's length same as len(nums1) it's completely my choice, this array keeps
track of 1 to 1 correspondence of elements

"""
def intersection_1(nums1, nums2):
    visited_list = [0] * len(nums2) #Holds the 
    intersection = []

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j] and visited_list[j] == 0:
                intersection.append(nums1[i])
                visited_list[j] = 1
                break
            
            #As arrays are sorted, if nums2[j] > nums1[i] then we don't have match beyound that
            if nums2[j] > nums1[i]:
                break

    return intersection


nums1 = [1, 2, 2, 2, 3, 3, 4, 5, 7]
nums2 = [1, 1, 1,  2, 2, 7]

print(f"Intersection of given two arrays is: {intersection_1(nums1, nums2)}")


#Approach One: Optimal Approach (Using 2 Pointer)
#Time Complexity: O(min(m, n))
#Space Complexity: O(k) : k length of inteersection array

def intersection_2(nums1, nums2):
    intersection = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        else:
            intersection.append(nums1[i])
            i += 1
            j += 1

    return intersection

nums1 = [1, 2, 2, 2, 3, 3, 4, 5, 7, 7, 7]
nums2 = [1, 1, 1,  2, 2, 7]

print(f"Intersection of given two arrays is: {intersection_2(nums1, nums2)}")