
import math
"""
Problem Statement
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.

"""


#Approach One:
#Time Complexity: O(log_10(n))
#Space Complexity: O(1)
def num_of_digits_i(num):
    count = 0 #Count number of digits
    while num:
        count += 1
        num = num // 10


    return count #Return number of digits



print(f'Number of digits: {num_of_digits_i(10990)}')


#Apporach Second:
#Time Complexity: O(1)
#Space Complexity: O(1)
def num_of_digits_ii(num):
    return math.floor(math.log10(num)) + 1


print(f'Number of digits: {num_of_digits_ii(10990)}')


'''
Note: Number of digits in any number is log_10(number)
'''


