

'''
Problem Statement:
You are given an integer n. You need to check whether the number is a palindrome number or not.
Return true if it's a palindrome number, otherwise return false.

A palindrome number is a number which reads the same both left to right and right to left.
e.g 121
'''


#Approach 01: Comparing number and its reverse
#Time Complexity: O(log_10(n))
#Space Complexity: O(1)


def check_palindrome_i(num):
    

    rev_num = 0
    temp = num

    while temp:
        rem = temp % 10
        rev_num = rev_num * 10 + rem
        temp = temp // 10

    return True if num == rev_num else False



print(f"Is plaindrome? {check_palindrome_i(122001)}")





#Approach 02: Converting into string and then using two pointer apporach
#Time Complexity: O(log_10(n) + [log_10n]^2) = O([log_10n]^2)
#Space Complexity: O(1)

def check_palindrome_ii(num):
      
      str_num = str(num) # O([log_10n]^2)
      
      #Initilize two pointers
      start = 0
      end = len(str_num) - 1

      while start < end:
            if not str_num[start] == str_num[end]:
                  return False
            
            start += 1
            end -= 1

      return True



print(f"Is plaindrome? {check_palindrome_ii(122001)}")

            
