


'''
Problem Statement: 
Given an array of integers, nums,sort the array in non-decreasing
order using the merge sort algorithm. Return the sorted array.

A sorted array in non-decreasing order is one in which each element
is either greater than or equal to all the elements to its left in the array

'''

#Approach one: Using top down method
#Time complexity: O(nlogn)
#Space complexity: O(n + logn) = O(n) : log(n) -> Height of stack
def mergeSort_topdown(arr, low, high):

    #If there is only one element in the array then return
    if low == high:
        return
    
    #Compute mid and call mergesort recursively
    mid = (low + high) // 2
    mergeSort_topdown(arr, low, mid)
    mergeSort_topdown(arr, mid + 1, high)

    #Merge two sorted arrays
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    leftArr = arr[low : mid + 1]
    rightArr = arr[mid + 1 : high + 1]

    #Now sort arr from index low to high
    i = j = 0
    k = low
    while k <= high and i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1


    #Copy remaining elements
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1



arr = [1, 2, 3, 4, -5, 600, 7, 80, 9]
mergeSort_topdown(arr, 0, len(arr) - 1)
print(f"Array after sorting: {arr}")




#Approach Second: Using top down approach with slightly different
#Time complexity: O(nlogn)
#Space complexity: O(nlogn) : log(n) -> Height of stack
                    #Slicing always creates a new array

def ms(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    sortedLeftSubArray = ms(arr[:mid])
    sortedRightSubArray = ms(arr[mid:])
    return mergeSortedArrays(sortedLeftSubArray, sortedRightSubArray)

def mergeSortedArrays(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #Copy remainig
    result.extend(left[i : len(left)])
    result.extend(right[j : len(right)])

    return result

arr1 = [1, 2, 3, 4, -5, 600, 7, 80, 9]
result = ms(arr1)
print(f"Array after sorting: {result}")
