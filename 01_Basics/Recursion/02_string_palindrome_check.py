


'''
Problem Statement:
Given a string s, return true if the string is palindrome, otherwise false.
A string is called palindrome if it reads the same forward and backward
'''


#Approach one: Using two pointer strategy
#Time complexity: O(n)
#Space comeplexity: O(1)

def palindrome_check(s):
    #Initilize both the pointers
    first, last = 0, len(s) - 1

    while first < last:
        if s[first] != s[last]: #Check if first and last chars of s are same or not
            return False
        
        first += 1
        last -= 1

    return True


print(palindrome_check("Zaaaaz"))



#Approach one: Using recursion
#Time complexity: O(n) : Number of calls n/2
#Space comeplexity: O(n) : Heigh of stack n/2

def palindrome_check_using_rec(s, start, end):

    if start < end:
        if s[start] != s[end]: #Exit earlier if s[start] and s[end] are not equal
            return False
        
        return palindrome_check_using_rec(s, start + 1, end - 1)
    else:
        return True #Return true when start becomes >= end



my_str = "ZZAAAAAAZZ"
print(palindrome_check_using_rec(my_str, 0, len(my_str) - 1))






