


'''
Problem Statement:
Given an array nums of n integers, find the most frequent element in it i.e.,
the element that occurs the maximum number of times. If there are multiple elements
that appear a maximum number of times, find the smallest of them.

'''

#Approach One: Using observation
#Time Complexity: O(n)
#Space Complexity: O(n)


def most_frequent_element(nums):
    freq = {} # hashtable to store frequencies

    # Count frequencies
    for key in nums:
        freq[key] = freq.get(key, 0) + 1

    
    #Store minkey and maxvalue
    min_key, max_count = float('inf'), float('-inf')

    for key, count in freq.items():
        if max_count < count:
            max_count = count
            min_key = key

        #Special case to check if count and max_count are equal
        elif max_count == count:
            if key < min_key:
                min_key = key


    return min_key #Return maximum value of nums




print(most_frequent_element([4, 4, 5, 5,5,5,5, 6, 4, 6, 6, 6, 6,4,4,4,6,6,6,6]))