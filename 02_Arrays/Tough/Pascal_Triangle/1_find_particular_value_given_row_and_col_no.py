import math
'''
Problem Statement: Pascal's Triangle I
Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.



In Pascal's triangle:
The first row contains a single element 1.
Each row has one more element than the previous row.
Every row starts and ends with 1.


For all interior elements (i.e., not at the ends), the value at position (r, c)
is computed as the sum of the two elements directly above it from the previous row:

Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
where indexing is 1-based

Example 1

Input: r = 4, c = 2
Output: 3
Explanation:
The Pascal's Triangle is as follows:

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

....

Thus, value at row 4 and column 2 = 3

'''

#In pascals triangle the value present at row r and column c is given by (r-1)C(c-1)

#Approach One: Using Formulla (n-1)C(r-1) : n and r are row no. and col no. in pascal triangle
#Time Complexity: O(n) : n number of rows
#Space Complexity: O(1)
#(n-1)C(r-1) = (n - 1)!/[(n-r-1)!*(r-1)!]

def pascal_value_1(row, col):
    row_1 = math.factorial(row - 1) #Compute (row-1)!
    col_1 = math.factorial(col - 1) #Compute (col-1)!
    row_col_1 = math.factorial(row - col) #Compute (row-col)!

    return row_1 // (col_1 * row_col_1) #Return integer value


print(f"Pascal value is: {pascal_value_1(5, 3)}")


#Approach 02: Using Intuition 5C3 = (5 * 4 * 3)/(3 * 2 * 1)
#Time Complexity: O(r) : r number of columns
#Space Complexity: O(1)
# 5C3 = (5 * 4 * 3)/(3 * 2 * 1)
def pascal_value_2(row, col):
    n = row - 1
    r = col - 1
    ans = 1

    for i in range(0, r):
        ans *= (n - i) / (i + 1)

    return int(ans)

print(f"Pascal value is: {pascal_value_2(5, 3)}")



#Approach 03: Using Recursion
#Time Complexity: O(2^r) : r number of rows
#Space Complexity: O(r)
def pascal_value(row, col):
    if col == row or col == 1:
        return 1
    
    return pascal_value(row - 1, col -1) + pascal_value(row - 1, col)


print(f"Pascal value is: {pascal_value(5, 3)}")