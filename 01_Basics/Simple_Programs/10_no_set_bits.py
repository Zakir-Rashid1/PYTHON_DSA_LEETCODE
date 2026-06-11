


'''
Problem Statement:
Given a positive integer n, write a function that returns the number of set bits
in its binary representation (also known as the Hamming weight)
'''


#Approach 01: Count number of set bits : USING ITERATION
#Time Complexity: O(log_2(n))
#Space Complexity: O(1)


def number_of_set_bits(num):
    count = 0 #Hold number of set bits

    while num:
        #Check if last bit is one, and this bit gets replaced by new
        #bit after right shift by 1
        if num & 1 == 1: 
            count += 1
        num = num >> 1 #Perform right shift by 1

    return count #Return number of set bits


print(f"Number of set bits are: {number_of_set_bits(3)}")


#Approach 02: Count number of set bits : USING RECURSION
#Time Complexity: O(log_2(n))
#Space Complexity: O(log_2(n))
def num_of_set_bits_rev(num):
    if num == 1:
        return 1
    
    return num % 2 + num_of_set_bits_rev(num // 2)



print(f"Number of set bits: {num_of_set_bits_rev(190)}")

