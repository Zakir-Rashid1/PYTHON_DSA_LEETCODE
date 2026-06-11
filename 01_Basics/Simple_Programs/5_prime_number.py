
import math
'''
Problem Statment:
You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number,
otherwise return false.
A prime number is a number which has no divisors except 1 and itself.

'''



#Approach 01: Using brute force
#Time Complexity: O(n) n: input number
#Space Complexity: O(1) 

def check_prime_i(num):

    #Special case for number 1
    if num == 1:
        return False
    #Check if there is any divisor b/w 2 and num-1
    for div in range(2, num):
        if num % div == 0:
            return False #Return false if there exits a divisor b/w 2 and num-1
    return True


print(check_prime_i(2))


#Approach 02: Using observation
#Time Complexity: O(sqrt(n)) n: input number
#Space Complexity: O(1) 

def check_prime_ii(num):
    #find upper bound for number of divisors
    bound = math.floor(math.sqrt(num))
    count = 0 #Count number of divisors

    for div in range(1, bound + 1):
        if num % div == 0:
            count += 1
            other_factor = num // div #Second factor
            if div != other_factor: #Check for duplicate factors
                count += 1

    #Check if number of divisors are 2 or not
    return True if count == 2 else False



print(check_prime_ii(1))



#Approach 02: Using keen observation
#Time Complexity: O(sqrt(n)) n: input number
#Space Complexity: O(1) 
'''
We know all factors can be found in O(sqr(n)), now suppose if there is no factor
b/w 1 to sqrt(n) than there won't be another factor
'''

def check_prime_iii(num):
    #find upper bound for number of divisors
    bound = math.floor(math.sqrt(num))
    #Special case when num == 1
    if num == 1:
        return False

    #Check if there exisits a divisor b/w  [2, sqrt(num))], if so return True else return False 
    for div in range(2, bound):
        if num % div == 0:
            return False

    return  True



print(check_prime_iii(3))