




'''
Problem Statement:
You're give a base 10 number and your job is to find its complement.
complement means changing 0 to 1 and 1 to 0
e.g num = 20 complement of 20 is: 11

'''

#Approach One: Using Iteration
#Time Complexity: O(log(n))
#Space Complexity: O(1)
def complement(num):
    comp = 0 #Store complement of num
    i = 0

    while num:
        lsb = num & 1 #Get LSB: Least significant bit

        if not lsb: #If LSB is 0, then compute it's weight
             '''1 << i is equivalent to 2^i, with benifit
               1 << i takes constant time'''
             comp += 1 << i
        num = num >> 1 #Right shift by one bit : equivalent to num //= 2
        i += 1

    return comp


print(f"Complement of given number is: {complement(20)}")



#Approach Two: Using Recursion
#Time Complexity: O(log(n))
#Space Complexity: O(log(n))

def complement_recursion(num, comp=0, i=0):
    if num == 0:
        return comp
    
    lsb = num & 1
    if not lsb:
        comp += 1 << i
    return complement_recursion(num >> 1, comp, i + 1)



print(f"Complement of given number is: {complement_recursion(20)}")
