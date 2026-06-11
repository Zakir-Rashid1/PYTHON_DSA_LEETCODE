import math
'''
Problem Statement:
You are given two integers n1 and n2. You need find the Greatest Common Divisor
(GCD) of the two given numbers. Return the GCD of the two numbers.

The Greatest Common Divisor (GCD) of two integers is the largest positive integer 
that divides both of the integers
'''

#Approach 01: Using Bruteforce
#Time Complexity: O(min(x, y))
#Space Complexity: O(1)

def gcd_1(x, y):
    min_num = min(x, y) #Find minimum among two
    gcd = 1
 
    for div in range(2, min_num + 1):
        if x % div == 0 and y % div == 0:
            gcd = div

    return gcd #Return gcd 
        


print(f"Gcd of given numbers is: {gcd_1(10, 80)}")



#Approach 02: Using Bruteforce(Slighlty better than approach 01)
#Time Complexity: O(min(x, y)) : Slightly better than Apporach 01 for some programs
#Space Complexity: O(1)

def gcd_2(x, y):
    min_num = min(x, y) #Find minimum among two
    gcd = 1
 
    for div in range(min_num, 0, -1):
        if x % div == 0 and y % div == 0:
            gcd = div
            break

    return gcd #Return gcd 


print(f"Gcd of given numbers is: {gcd_2(10, 11)}")





#Approach 03: Using divisors 
#Time Complexity: O(sqrt(min(x, y)))
#Space Complexity: O(1)

def gcd_3(x, y):
    min_num , max_num= min(x, y), max(x, y) #Find minimum and maximum among two
    gcd = 1


    # Only need to iterate up to the square root to find all factor pairs
    search_limit = math.isqrt(min_num) #Return integer square root value e.g sqrt(27) = 5
    for div in range(1, search_limit + 1):

        if min_num % div == 0: #If true than one factor is div
            other_factor = min_num // div #Other factor

            #Now check weather the two factors are the factors of maximum number
            if max_num % div == 0:
                gcd = max(gcd, div)
            if max_num % other_factor == 0:
                gcd = max(gcd, other_factor)
        
          

    return gcd

print(f"Gcd of given numbers is: {gcd_3(24, 12)}")


#Approach 04: Using Eculedian Algorithm
#Time Complexity: O(log_phi(min(a, b)) : phi because a and b are changing
#Space Complexity: O(1)
def gcd_04(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return b if a == 0 else a


print(f"Gcd of given numbers is: {gcd_04(100, 201)}")



