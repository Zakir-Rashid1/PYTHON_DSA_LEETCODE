

'''
Problem Statement: Rotate matrix by 90 degrees anticlockwise
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees anti-clockwise.
The rotation must be done in place, meaning the input 2D matrix must be modified directly.


Example 1

Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: matrix = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)



#Approach 01: Using Reverse & Transpose
#Time Complexity: O(n^2)
#Space Complexity: O(1)


def rotate_by_90_deg_2(matrix):
    length = len(matrix)

    #Reverse each row inplace
    for row in matrix:
        row.reverse()

    #Transpose the matrix (in place)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
    return matrix



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Rotated matrix is: {rotate_by_90_deg_2(matrix)}")
