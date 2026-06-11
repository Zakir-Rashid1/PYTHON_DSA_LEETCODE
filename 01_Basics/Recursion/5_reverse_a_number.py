


'''
Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

#Approach One: USING RECURSION
#Time Complexity: O(log_10(n))
#Space Complexity: O(log_10(n))

def reverse_number(num, rev=0):
    temp = -num if num < 0 else num #Convert negative number to +ive

    #Now check if the number is outside the range
    if temp < pow(-2, 31) or temp > pow(2, 31) - 1:
        return 0
    
    #Compute reverse of a number
    def compute_reverse(temp):
        if temp == 0:
            return rev
        return reverse_number(temp // 10, rev * 10 + temp % 10)
    
    rev_num = compute_reverse(temp)

    #Check if orginal number was even or odd, based on that rev. number
    return -rev_num if num < 0 else rev_num

  


print(f"Reverse of given number is: {reverse_number(-78798)}")
    
