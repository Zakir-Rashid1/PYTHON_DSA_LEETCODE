





'''
Problem Statement: Rotate matrix by 90 degrees
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
The rotation must be done in place, meaning the input 2D matrix must be modified directly.


Example 1

Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
'''

#Approach 01: Using Bruteforce
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
def rotate_by_90_deg_1(matrix):
    length = len(matrix)
    temp_matrix = [[None] * length for _ in range(length)]

    '''
    Observation: 
    temp_matrix[0][2] = matrix[0][0]
    temp_matrix[1][2] = matrix[0][1]
    temp_matrix[2][2] = matrix[0][2]

    temp_matrix[0][1] = matrix[1][0]
    temp_matrix[1][1] = matrix[1][1]
    temp_matrix[2][1] = matrix[1][2]

    ...
    '''
    for i in range(length):
        for j in range(length-1, -1, -1):
            temp_matrix[j][length - 1 - i] = matrix[i][j]

    return temp_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Rotated matrix is: {rotate_by_90_deg_1(matrix)}")



#Approach 01: Using Transpose & Reverse
#Time Complexity: O(n^2)
#Space Complexity: O(1)


def rotate_by_90_deg_2(matrix):
    length = len(matrix)

    #Transpose the matrix (in place)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #Now reverse each row inplace
    for row in matrix:
        row.reverse()
        
    return matrix



matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(f"Rotated matrix is: {rotate_by_90_deg_2(matrix)}")