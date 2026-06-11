import math

'''
Problem Statment:
You are given an integer n. You need to check whether it is an armstrong number or not.
Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the
number, raised to the power of the number of digits.

'''



#Approach One: Using observation
#Time Complexity: O(dlog_10(d)) => O(log(n) log[logn]) n: input number
#Space Complexity: O(1) 

def isArmstrong( n):
    nod = math.floor(math.log10(n)) + 1 # number of digits
    temp = n
    sum = 0
    
    while temp:
        digit = temp % 10
        sum += digit ** nod #Time complexity: O(logd) d: number of digits
        temp = temp // 10


    return True if n == int(sum) else False





print(isArmstrong(153))