
'''
Problem Statement: Merge two sorted arrays without extra space

Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
Merge both the arrays into a single array sorted in non-decreasing order.



The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
nums2 has a length of n.

Example 1
Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]
Output: [-5, -3, -2, 1, 4, 5, 8]

Explanation:
The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2

'''

#Approach one: Using Optimal Approach
#Time Complexity: O(mlogm + nlogn + min(m, n))
#Space Complexity: O(m) : This much of extra space is fine
'''
nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]
for nums1 start from last and for nums2 start from begning

'''
def merge_two_sorted_arrays(nums1, m, nums2, n):
        right = m - 1
        left = 0

        while right >= 0 and left < n:
            if nums1[right] > nums2[left]:
                nums1[right], nums2[left] = nums2[left], nums1[right]
                right -= 1
                left += 1
            else:
                break

        #Sort both nums1 and nums2
        nums1[0:m] = sorted(nums1[0:m])
        nums2.sort()

        #Now add elements of nums2 to the nums1
        for i in range(0, n):
            nums1[i + m] = nums2[i]



nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
merge_two_sorted_arrays(nums1, len(nums1)-3, nums2, len(nums2))
print(nums1)