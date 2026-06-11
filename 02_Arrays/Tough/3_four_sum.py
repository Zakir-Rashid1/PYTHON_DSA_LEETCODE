'''
Problem Statment: 4 Sum
Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

#Approach One: Bruteforce
#Time Complexity: O(n^4)
#Space Complexity: O(1)

def four_sum_1(nums, target):
    quadtruplets = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for l in range(k + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        quadtruplets.append([nums[i], nums[j], nums[k], nums[l]])


    return quadtruplets

nums = [1,0,-1,0,-2,2]
print(f"All triplets are: {four_sum_1(nums, 0)}")


#Approach One: Using Better Approach
#Time Complexity: O(n^3)
#Space Complexity: O(n)

def four_sum_2(nums, target):
    quadtruplets = set() #Stores quadtruplets

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Check the existence of fourth element b/w j and k
            seen = set() #Checks if the fourth element is already seen or not
            for k in range(j + 1, len(nums)):
                fourth = target - (nums[i] + nums[j] + nums[k])

                if fourth in seen:
                    quadtruplet = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                    quadtruplets.add(quadtruplet)

                seen.add(nums[k])

    return [list(quadtruplet) for quadtruplet in quadtruplets]

nums = [1,0,-1,0,-2,2]
print(f"All triplets are: {four_sum_2(nums, 0)}")





'''
To Skip Any Duplicates in any array
if index > start and nums[index] == nums[index - 1]:
    continue
'''
#Approach One: Using Optimal Approach
#Time Complexity: O(n^3)
#Space Complexity: O(1)


'''
Keep i and j fix and use left and right as two pointers
'''
def four_sum_3(nums, target):
    quadtruplets = [] #Stores quadtruplets
    nums.sort() #Sort the orginal array

    for i in range(len(nums)):
        #Skip first duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            #Skip second duplicates
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    quadtruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


    return quadtruplets



nums = [1,0,-1,0,-2,2]
print(f"All triplets are: {four_sum_3(nums, 0)}")