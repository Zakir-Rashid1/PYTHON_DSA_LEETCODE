


'''
Problem Statement:
You're given a +ive integer and you need to convert it into binary number
'''

#Approach One: USING RECURSION
#Time Complexity: O(log_2(n))
#Space Complexity: O(log_2(n))

def dec_to_binary(num):
    if num == 0:
        return 0
    #Recursively call dec_to_binary function
    return dec_to_binary(num // 2) * 10 + num % 2

print(f"Binary representation of given number is: {dec_to_binary(463)}")

# Note: For smaller numbers above approach is okay, but for large
#numbers it's not feasiable




#Approach Two: USING RECURSION (Returing as a string)
#Time Complexity: O([log_2(n)]^2)
#Space Complexity: O(log_2(n) + log_2(n)) = O(log_2(n))

def dec_to_binary_str(num):
    if num == 0:
        return "0"
    
    #Recursively call dec_to_binary_str function
    return dec_to_binary_str(num // 2) + str(num % 2)


print(f"Binary representation of given number is: {dec_to_binary_str(463846837)}")



#Approach 03: Using iteration
#Time complexity: O(log(n)* log(logn))
#Space complexity: O(1)
#Time complexity for pow(10, i) = O(log(i))
'''
Time Complexity: log1 + log2 + log3 + ... + logk. : k kth iteration
    = log(k!)
    = O(klogk)
    = O(log(n) * log(log(n)))

'''

def dec_to_binary_iter(num):
    binary_number = 0
    i = 0

    while num:
        binary_digit = num & 1 #Getting LSB (Least significant bit)
        binary_number += binary_digit * pow(10, i)

        num = num >> 1 #Perform right shift by 1 bit 
        i += 1

    return binary_number #Return binary number


print(f"Binary representation of given number is: {dec_to_binary_iter(100)}")


