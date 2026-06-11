import math

'''
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
'''


#Approach One:
#Time Complexity: O(log_10(n))
#Space Complexity: O(1)

def reverse_num_i(num):
    rev_num = 0 #Hold reverse of a number
    temp = num

    while temp:
        rem = temp % 10
        rev_num = rev_num * 10 + rem
        temp = temp // 10

    

    return rev_num #Return reversed number


print(f"Reverse of number is: {reverse_num_i(3926)}")


#Apporach Second: Recursive 
#Time Complexity: O(log_10(n)) -Number of recursive calls == Number of digits in a number
#Space Complexity: O(log_10(n)) -Max heigh of stack

def reverse_num_ii(num):
    if num == 0:
        return 0
    rem = num % 10 #Compute remainder
    return rem * pow(10, math.floor(math.log10(num))) + reverse_num_ii(num // 10)


print(f"Reverse of given number is: {reverse_num_ii(3926)}")



