

'''
Problem Statement:
You're given a binary representation of a +ive integer and you need to find
it's equivalent decimal number
'''




#Approach 01: Using iteration : I
'''
Time Complexity: log1 + log2 + log3 + ... + log(n)
        = logn!
        = O(nlog(n))
Space Complexity: O(1)

'''
def binary_to_decimal_i(num):
    bin = 0
    j = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0': #Compute weights for only non zero bits
            bin += pow(2, j)
        j += 1

    return bin

print(f"Decimal euqivalent is: {binary_to_decimal_i("101011")}")


#Approach 02: Using iteration : II
#Time Complexity: O(n)
#Space Complexity: O(1)

def binary_to_decimal_ii(num):
    bin = 0
    j = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0': #Compute weights for only non zero bits
            bin += 1 << j # 1 << j equivalent to 2^j : Takes O(1) time
        j += 1

    return bin

print(f"Decimal euqivalent is: {binary_to_decimal_ii("101011")}")




#Approach 03: Using iteration : III
#Time Complexity: O(n)
#Space Complexity: O(1)

def binary_to_decimal_iii(num):
    bin = 0
    for bit in num:
        bin = bin * 2 + int(bit)

    return bin

print(f"Decimal euqivalent is: {binary_to_decimal_iii("101011")}")


#Approach 04: Using recursion 
#Time Complexity: O(n)
#Space Complexity: O(1)

def binary_to_decimal(num, i=0, bin=0):
    if i == len(num):
        return bin
    bin = bin * 2 + int(num[i])
    return binary_to_decimal(num, i + 1, bin)


print(f"Decimal euqivalent is: {binary_to_decimal("10100")}")


