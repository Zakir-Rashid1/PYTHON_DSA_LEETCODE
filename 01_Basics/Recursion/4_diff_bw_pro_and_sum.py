

'''
Problem Statement:
You are given a number you need to return the difference b/w its product
and sum using pure recursion
'''

#Approach one: Using Recursion
#Time Complexity: O(log_10(n))
#Space Complexity: O(log_10(n))

def diff_bw_product_sum(num):

    #Return product
    def product(num):
        if num == 0:
            return 1
        
        return num % 10 * product(num // 10)

    #Return sum
    def sum(num):
        if num == 0:
            return 0
        
        return num % 10 + sum(num // 10)
    
    return product(num) - sum(num) #Return diff b/w product and sum


print(f"Difference b/w product and sum is: {diff_bw_product_sum(1999)}")