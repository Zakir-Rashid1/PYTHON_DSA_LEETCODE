import math

'''
Problem Statement:
You are given an integer n. You need to find all the divisors of n. 
Return all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.
'''


#Approach One: Using brute force
#Time Complexity: O(n) n: input number
#Space Complexity: O(m) m: number of divisors

def print_all_div_1(n):
    div_list = [] #Divisor list
    for div in range(1, n + 1):
        if n % div == 0:
            div_list.append(div)

    return div_list

print(print_all_div_1(36))


#Approach 2nd: Using observation
#Time Complexity: O(sqrt(n) + mlogm) = O(sqrt(n)) bcoz n dominates when n->inf
#Space Complexity: O(m)

def print_all_div_2(n):
    upper_bound = math.isqrt(n)
    div_list = [] #Divisor list

    for div in range(1, upper_bound + 1):
        if n % div == 0:
            div_list.append(div)
            if n // div != div: #Check for duplicate divisors
                div_list.append(n // div)

    div_list.sort() #Sort divisors: Time comlexity: O(mlogm) m: number of divisors
    return div_list



print(print_all_div_2(21))


#Approach 3rnd: Using Recursion
#Time Complexity: O(sqrt(n) + mlogm) = O[sqrt(n) + sqrt(n)log(n)]
                #In worst case number of divisors(m) = sqrt(n)
#Space Complexity: O(sqrt(n) + m) = O[sqrt(n) + sqrt(n)] = O(sqrt(n)) in worst case m = sqrt(n)
                #sqrt(n) : Number of recursive calls

def print_all_div_3(num, div=1,  div_list=[]):
    #Base condition
    if div > math.isqrt(num):
        div_list.sort()
        return div_list
    
    if num % div == 0:
        div_list.append(div)
        other_div = num // div
        
        if other_div != div: #Check for duplicate divisors
            div_list.append(other_div)
    return print_all_div_3(num, div + 1)


print(print_all_div_3(21))
