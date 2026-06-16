

'''

Problem Statement: Majority Element-II

Given an integer array nums of size n. Return all elements which
appear more than floor(n/3) times in the array. The output can be returned in any order.


Example 1
Input: nums = [1, 2, 1, 1, 3, 2]
Output: [1]

Explanation:
Here, n / 3 = 6 / 3 = 2.

Therefore the elements appearing 3 or more times is : [1]

Example 2
Input: nums = [1, 2, 1, 1, 3, 2, 2]
Output: [1, 2]

Explanation:
Here, n / 3 = 7 / 3 = 2.

Therefore the elements appearing 3 or more times is : [1, 2]


Note: At max only two element can appear more than n/3 times
'''

#Approach 01: Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(1)
def majority_element_1(nums):
    length = len(nums)
    result = []

    for i in range(length):
        current_element = nums[i]
        count= 0

        # Check if the result is empty or the element present in result != current element
        if len(result) == 0 or current_element != result[0]:
            for j in range(length):
                if current_element == nums[j]:
                    count += 1
        
        #Now check weather it was the majority element or not
        if count > length // 3:
            result.append(current_element)

        #Check if at any stage the list count becomes 2 then break
        if len(result) == 2:
            break


    return result



nums = [1, 2, 1, 1, 3, 2, 2]
print(f"Majority element are: {majority_element_1(nums)}")


#Approach 02: Using Hashing
#Time Complexity: O(n)
#Space Complexity: O(n)

def majority_element_2(nums):
    threshold = len(nums) // 3
    result = []
    freq = {}

    # Count frequency of each element
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

        # If the frequency becomes equal to threashold+1 then append that to the result
        '''
        Thre reason i've checked for threashold + 1 is that for duplicate
        elements like [3,3,3,3] the threshold is 1, if i don't use this
        technique then result will store duplicate elements
        '''
        if freq[num] == threshold + 1:
            result.append(num)

        # Check if length of result becomes equal to 2 then break
        if len(result) == 2:
            break

    return result


nums = [3, 3, 3, 3]
print(f"Majority element are: {majority_element_2(nums)}")

    


#Approach 02: Using Moores Voting Algo 
#Time Complexity: O(n)
#Space Complexity: O(1)

#This algo is the replica (with slightly modification) of the moores
# voting algo for majority element occuring morethan n//2
def majority_element_3(nums):
    majority_ele1, majority_ele2 = None, None
    count1, count2, = 0, 0

    for current_ele in nums:
        if count1 == 0 and current_ele != majority_ele2: #Checking current_ele !+ majority_ele2 is the edge case
            majority_ele1 = current_ele
            count1 = 1
        elif count2 == 0 and current_ele != majority_ele1: #Checking current_ele !+ majority_ele1 is the edge case
            majority_ele2 = current_ele
            count2 = 1
        elif current_ele == majority_ele1:
            count1 += 1
        elif current_ele == majority_ele2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    return [majority_ele1, majority_ele2]


nums = [2, 1, 1, 3, 1, 4, 5, 6]
print(f"Majority element are: {majority_element_3(nums)}")