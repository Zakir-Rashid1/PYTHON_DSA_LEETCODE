


'''
Problem Statement:
Given an array arr of n elements. The task is to reverse the given array.
The reversal of array should be inplace.
'''


#Time Complexity: O(n) : I need to do n/2 number of recursive calls
#Space Complexity: O(n) : Height of stack is n/2
def reverse_arr(arr, first, last):
    #Special case: return when we've only one element
    if first == last:
        return
    
    #Swap first and last element
    arr[first], arr[last] = arr[last], arr[first]
    reverse_arr(arr, first + 1, last - 1) #Swap recursively




arr=[1,2,3,4,5]
reverse_arr(arr, 0, len(arr) - 1)
print(arr)