



#Approach one: Using iterative algo.
#Time complexity: O(n^2) :  Best/worst/avg
#Space complexity: O(1)
def selection_sort_iter(arr):
    for i in range(len(arr)):
        min_index = i #Hold index, where minimum element will be placed

        #Find minimum index from remaining array
        for j in range(i, len(arr)):
            if arr[j] <= arr[min_index]:
                min_index = j

        #Check if index and i are same
        if min_index != i:
            #Swap if they're not same
            arr[i], arr[min_index] = arr[min_index], arr[i] 


arr = [1, 2, 9, 0, -1, 2, 88, 0, 1]
selection_sort_iter(arr)
print(f"Array after sorting: {arr}")



#Approach Second: Using recursive algo.
#Time complexity: O(n^2) :  Best/worst/avg
#Space complexity: O(n) : height of stack
def selection_sort_recur(arr, start):
    if start == len(arr):
        return
    
    #Find minimum index from start to the len(arr) - 1
    min_index = find_minimum(arr, start) 

    #Now check if start and min_index are not same, if not than swap
    if start != min_index:
        arr[start], arr[min_index] = arr[min_index], arr[start]

    #Call selection sort recursive on unsorted part
    selection_sort_recur(arr, start + 1)


#Function used to find index of minimum element
def find_minimum(arr, index):
    if index == len(arr) - 1:
        #Assuming index of last element as index of minimum element
        return index 
    
    min_index = find_minimum(arr, index + 1)
    #Update min_index to index if, arr[index] <= arr[min_index]
    if arr[index] <= arr[min_index]:
        min_index = index
    
    return min_index


arr = [4, 3, 2, 1, 0, -98]
selection_sort_recur(arr, 0)
print(f"Array after sorting: {arr}")


