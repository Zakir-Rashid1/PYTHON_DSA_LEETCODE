'''

Problem Statement: Find Missing and Repeated Values

You are given a 0-indexed 2D integer matrix grid of size n * n with values 
in the range [1, n2]. Each integer appears exactly once except a which appears
 twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

Example 1:
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].


Example 2:
Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
'''

#Approach one: Using extra space
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
def find_missing_and_repeated_values(grid):
    n = len(grid) * len(grid)
    grid_sum = 0
    freq = {} # Stores frequencies of each element

    #Step 01: Compute actual sum
    actual_sum = n * (n + 1) // 2

    #Step 02: Compute sum of grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr_ele = grid[i][j]
            grid_sum += curr_ele

            freq[curr_ele] = freq.get(curr_ele, 0) + 1

            if freq[curr_ele] == 2:
                num_appear_twice = curr_ele

    #Now remove the the number that appers twice from gird sum
    grid_sum -= num_appear_twice

    missing_num = actual_sum - grid_sum #Calculate missing number

    return [num_appear_twice, missing_num]


grid = [[9,1,7],[8,9,2],[3,4,6]]
print(f"Appear twice and missing number: {find_missing_and_repeated_values(grid)}")
    



#Approach one: Using Optimal Approach
#Time Complexity: O(n^2)
#Space Complexity: O(1)

# Approach: Mathematics
# Time Complexity: O(n²)
# Space Complexity: O(1)

def find_missing_and_repeated_values_2(grid):
    n = len(grid) * len(grid) # Numbers should be from 1 to n²
    grid_sum = 0
    grid_sum_squares = 0

    expected_sum = n * (n + 1) // 2 # Expected sum of 1..n

    # Expected sum of squares of 1..n
    expected_sum_squares = n * (n + 1) * (2 * n + 1) // 6

    # Compute actual values from grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            current = grid[row][col]

            grid_sum += current
            grid_sum_squares += current * current

    
    diff = expected_sum - grid_sum # x - y
    square_diff = expected_sum_squares - grid_sum_squares # x² - y²
    sum_xy = square_diff // diff # x + y

    
    missing = (diff + sum_xy) // 2 # Missing number (x)
    repeated = missing - diff # Repeated number (y)

    return [repeated, missing]

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(f"Appear twice and missing number: {find_missing_and_repeated_values_2(grid)}")
    
