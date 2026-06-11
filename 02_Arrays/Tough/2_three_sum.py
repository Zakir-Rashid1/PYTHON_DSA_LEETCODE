


'''
Problem Statement: 3 Sum
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.


Notice that the solution set must not contain duplicate triplets.
One element can be a part of multiple triplets. The output and the triplets can be returned in any order.


Example 1
Input: nums = [2, -2, 0, 3, -3, 5]
Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

Explanation:
nums[1] + nums[2] + nums[0] = 0
nums[4] + nums[1] + nums[5] = 0
nums[4] + nums[2] + nums[3] = 0

Example 2
Input: nums = [2, -1, -1, 3, -1]
Output: [[-1, -1, 2]]

'''

#Approach 01: Bruteforce
#Time Complexity : O(n^3)
#Space Complexity: O(n)
def three_sum_1(nums, target=0):
    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    result.add((nums[i], nums[j], nums[k]))

    return [list(triplet) for triplet in result]


nums = [2, -2, 0, 3, -3, 5]
print(f"All triplets are: {three_sum_1(nums)}")




#Approach 02: Using Better Approach
#Time Complexity : O(n^2 * log3) = O(n^2)
#Space Complexity: O(n)

def three_sum_2(nums, target=0):
    triplets = set() #Store the triplets
    for i in range(len(nums)):
        first_ele = nums[i]

        seen = set() #Store the seen elements
        for j in range(i + 1, len(nums)):
            second_ele = nums[j]

            #The third element is calculated using below formula
            third_ele = -(first_ele + second_ele)
            if third_ele in seen:
                triplet = tuple(sorted([first_ele, second_ele, third_ele]))
                triplets.add(triplet)


            #Add second_ele to the seen set
            seen.add(second_ele)

    return [list(triplet) for triplet in triplets]


nums = [2, -2, 0, 3, -3, 5]
print(f"All triplets are: {three_sum_2(nums)}")



'''
The optimal approach for 3Sum is:
Sort the array.
Fix one element.
Use two pointers to find the other two elements.
'''
#Approach 03: Using Optimal Approach
#Time Complexity : O(n^2) = O(n^2)
#Space Complexity: O(1)

def three_sum_3(nums, target=0):
    triplets = []
    #Step 01: Sort the array
    nums.sort()

    for i in range(len(nums)):
        #Step 02: Skip dupilicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        #Step 03: Use two pointer approach
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                #Step 04: Skip dulpicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1



    return triplets

nums = [2, -2, 0, 3, -3, 5]
print(f"All triplets are: {three_sum_3(nums)}")
