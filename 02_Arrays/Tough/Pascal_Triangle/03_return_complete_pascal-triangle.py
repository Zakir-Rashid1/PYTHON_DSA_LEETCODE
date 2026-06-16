'''
Problem Statement: Return Complelte Pascal triangle
You'll be given number of rows and you need to return the whole pascal triangle

Example 1

Input: r = 5
Output:
1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

'''


#Approach One: Compute and add each value
#Time Complexity: O(r^2 * c)
#Space Complexity: O(1)


#Return pascal value
def pascal_value(r, c):
    ans = 1
    for i in range(c):
        ans *= (r - i) / (i + 1)

    return int(ans)


def pascal_triangle_1(rows):
    pascal_tri = [[None] * i for i in range(1, rows+1)] #Store result
    for row in range(rows):
        for col in range(row + 1):
            pascal_tri[row][col] = pascal_value(row, col)

    return pascal_tri


# print(f"Pascal triangle is: {pascal_triangle_1(6)}")



#Approach 02: Compute and add each value
#Time Complexity: O(rc)
#Space Complexity: O(1)

#Return pascal row
def pascal_row(row):
    temp = [1]
    ans = 1
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        temp.append(ans)

    return temp

def pascal_triangle_2(rows):
    pascal_tri = [] #Store final result

    #Iterate over all the rows
    for row in range(1, rows + 1):
        pascal_tri.append(pascal_row(row)) #Append each generated row of pascal triangle

    return pascal_tri # Return pascal triangle

print(f"Pascal triangle is: {pascal_triangle_2(3)}")



