'''
Problem Statement: Pascal's Triangle II
You'll be given the row number and you need to return the whole row


Example 1

Input: r = 4
Output: 1 3 3 1


The Pascal's Triangle is as follows:
1

1 1

1 2 1

1 3 3 1

1 4 6 4 1
'''


#Approach 01: Using Formula Keenly
#Time Complexity: O(rc)
#Space Complexity: O(1)


#Compute pascal value
def pascal_value(r, c):
    ans = 1
    for i in range(c):
        ans *= (r - i)
        ans //= (i + 1)

    return ans


def pascal_row_1(row):
    pascal_row = [] #Store row of pascal triangle

    #Number of columns and rows are same in pascal triangle
    for col in range(row):
        #Value in a pascal triangle is given by (r-1)C(c-1)
        pascal_row.append(pascal_value(row - 1, col))

    return pascal_row
        


print(f"Pascal row is: {pascal_row_1(6)}")


#Approach 01: Using Intuition
#Time Complexity: O(r)
#Space Complexity: O(1)

#The next pascal value given previous value is calculated as prev*((row - col)/col)

def pascal_row_2(row):
    pascal_row = [1] #Store row of pascal triangle
    ans = 1

    for col in range(1, row ):
        ans *= ((row - col) / col)
        pascal_row.append(int(ans))

    return pascal_row

print(f"Pascal row is: {pascal_row_2(6)}")
