



'''
Problem Statement:
You're given a +ive number and you need to tell weather it's a power of
2 or not
e.g 64: yes
    0: yes
    9: no
'''

#Approach One: Using Iteration
#Time Complexity: O(log(n))
#Space Complexity: O(1)
def power_of_two(num):

    #Run loop as long as num != 0
    while num:
        if num == 1:
            return True
        
        lsb = num & 1 #Get LSB
        if lsb: #If lsb is 1, then number is odd hence not power of 2
            return False
        
        num = num >> 1 #Right shift by 1 bit

    return False if not num else True #Handles case when num = 0



print(f"Is power of 2? {power_of_two(64)}")


#Approach One: Using Recursion
#Time Complexity: O(log(n))
#Space Complexity: O(log(n))

def power_of_two_recursive(num):
    #Base case
    if num == 1:
        return True
    #Handle a special case when num == 0
    if num == 0:
        return False

    lsb = num & 1 #Get lsb
    if lsb:
        return False

    return power_of_two_recursive(num >> 1) 

print(f"Is power of 2? {power_of_two_recursive(0)}")

