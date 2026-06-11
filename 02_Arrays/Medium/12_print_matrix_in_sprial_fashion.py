

'''
Problem Statement: Print the matrix in spiral manner

Given an M * N matrix, print the elements in a clockwise spiral manner.
Return an array with the elements in the order of their appearance when printed in a spiral manner.


Example 1
Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Explanation:
The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

Example 2
Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
Output: [1, 2, 3, 4, 8, 7, 6, 5]

Explanation:
The elements in the spiral order are 1, 2, 3, 4 -> 8, 7, 6, 5

'''

#Approach 01: Using Optimal Method
#Time Complexity: O(mn)
#Space Complexity: O(1)


def print_sprial(matrix):
    left, right = 0, len(matrix[0]) - 1
    top , bottom = 0, len(matrix) - 1
    ans = []



    while left <= right and top <= bottom:
        #Go from left to right
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1 # Increment top by 1

        #Go from top to bottom
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1 # Decrement the right by 1

        #Go from right to left : we'll go from right to left when we've more than one row
        # that means top must be <= bottom
        if top <= bottom: #This condition is for when we've only one row
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1 # Decreement bottom by 1

        #Go from bottom to top : we'll go from bottom to top when we've more than one col
        # that means left must be <= right
        if left <= right: # Case of single column
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1 # Increment left by 1
    

    return ans
matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
print(f"Sprial pattern of above matrix is: {print_sprial(matrix)}")

    