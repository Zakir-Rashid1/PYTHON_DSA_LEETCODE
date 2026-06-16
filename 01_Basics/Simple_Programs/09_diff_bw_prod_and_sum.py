



'''
Problem Statement:
You'are given a number you need to return the difference b/w the product and 
sum of its digits
'''

#Approach One: Using iteration
#Time Complexity: O(log_10(n))
#Space Complexity: O(log_10(n))
def diff_bw_product_sum(num):
    product = 1 #Hold product of digits
    sum = 0 #Hold sum of digits
    
    temp = num
    while temp:
        product *= (temp % 10) # Store product of digits
        sum += (temp % 10) # store sum of digits
        temp //= 10

    return product - sum 


print(f"Diff. b/w product and sum is: {diff_bw_product_sum(1999)}")