
'''
Problem Statement: Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

'''

#Approach 01: Using Bruteforce
#Time Complexity: O[k(m + n)] : k = mn in worst case, k is number of zeroes in orginal matrix
#   For square matrices it becomes n^2(n) = O(n^3)
#Space Complexity: O[k] : k = mn in worst case


def set_matrix_zeroes_1(matrix):
    zero_positions = []

    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Store positions of all original zeroes
    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] == 0:
                zero_positions.append((row, col))

    # Step 2: Make rows and columns zero
    for row, col in zero_positions:
        for c in range(cols): # Make entire row zero
            matrix[row][c] = 0

        for r in range(rows): # Make entire column zero
            matrix[r][col] = 0
    

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zeroes_1(matrix)
print(f"Resulting array is 01:  {matrix}")




#Approach 02: Using Bruteforce a bit better than above intersm of space complexity
#Time Complexity: O[mn(m + n)] 
#Space Complexity: O[1]
def set_matrix_zeroes_2(matrix):
    infinity = float('inf')
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            #Step 01: Mark the entire rows and cols who contains atleast one 0
            if matrix[row][col] == 0:
                #Mark entire column as infinity
                for i in range(rows):
                    matrix[i][col] = infinity

                #Mark entire row as infinity
                for j in range(cols):
                    matrix[row][j] = infinity

    #Step 02: Now make all inf to 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == infinity:
                matrix[row][col] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zeroes_2(matrix)
print(f"Resulting array is 02:  {matrix}")


#Approach 03: Using Better Approach
#Time Complexity: O[mn] 
#Space Complexity: O[m + n]

def set_matrix_zeroes_3(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_mark = [0] * rows
    col_mark = [0] * cols

    # Step 1: Mark rows and columns
    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] == 0:
                row_mark[row] = 1
                col_mark[col] = 1

    # Step 2: Set zeroes
    for row in range(rows):
        for col in range(cols):

            if row_mark[row] == 1 or col_mark[col] == 1:
                matrix[row][col] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zeroes_3(matrix)
print(f"Resulting array is 03:  {matrix}")


#Approach 03: Using Optimal Approach
#Time Complexity: O[mn] 
#Space Complexity: O(1)

def set_matrix_zeroes_4(matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])
        #Keep track if the first row and first column contains zeroes
        first_row , first_col = False, False


        # Set markers in first row and first column
        '''
        The reason i started from (0, 0) is to keep track if first row or first col has
        0's in it
        '''
        for row in range(rows):
            for col in range(cols):
                #Check if first row or first column has zeroes in it 
                if matrix[row][col] == 0:
                    if row == 0: first_row = True
                    if col == 0: first_col = True

                    matrix[0][col] = 0
                    matrix[row][0] = 0

        #Replace inner matrix
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # If first row has zero then make entrie row 0
        if first_row:
            for col in range(cols):
                matrix[0][col] = 0

        # If first col has zero then make entrie col 0
        if first_col:
            for row in range(rows):
                matrix[row][0] = 0  




matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_matrix_zeroes_4(matrix)
print(f"Resulting array is 04:  {matrix}")