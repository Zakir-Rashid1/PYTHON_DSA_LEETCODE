

'''
Problem Statement:
Given an array of integers nums, return the value of the largest
element in the array

'''

#Approach One: Using Iteration
#Time Complexity: O(n)
#Space Complexity: O(1)

def find_min_max(arr):
    min_value = max_value = arr[0] #Assuming first element is my both min and max
    '''
    There is a greate catch here if we initilize min_value = max_value = 0
    and my array doesn't contain zero it contains only all +ive or -ive
    numbers, in that case this above initilization yeilds wrong results
    '''
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i] #Update min_value

        if arr[i] > max_value:
            max_value = arr[i] #Update max_value

    return min_value, max_value #Return both min and max value



arr = [10, 9, 3, 8, 99, 324, 7682]
print(f"Min and max values are: {find_min_max(arr)}")


#Approach 2nd: Using Recursion
#Time Complexity: O(n)
#Space Complexity: O(n)

def find_min_max_recursive(arr, i=0, min_value=None, max_value=None):
    if i == len(arr):
        return min_value, max_value
    
    #Assume min and max values are first element of array
    if i == 0:
        min_value = max_value = arr[i]

    if arr[i] < min_value:
        min_value = arr[i] #Update min_value

    if arr[i] > max_value:
        max_value = arr[i] #Update max_value
  
    return find_min_max_recursive(arr, i + 1, min_value, max_value)

arr = [190, 23, 43, 89, 1, 2, 22]
print(f"Min and max values are: {find_min_max_recursive(arr)}")


    


