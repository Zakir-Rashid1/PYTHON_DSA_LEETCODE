




#Sorting algo 03: Insertion sort
#   -Time complexity: O(n^2)
#   -Space complexity: O(1)




#Approach one: Using iterative algo.
#Time complexity: O(n^2)
#Space complexity: O(1)
def insertion_sort_iter(arr):
    for i in range(1, len(arr)):
        key = arr[i] #Key is the element for which we want to find the right position
        j = i - 1 # j pointer points i - 1

        #Now check key should be < arr[j]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        #Put key on its right place
        arr[j + 1] = key


arr = [9, 7, 6, 10, 2, 1, -9]
insertion_sort_iter(arr)
print(f"Array after sorting: {arr}")



#Approach one: Using recursive algo.
#Time complexity: O(n^2)
#Space complexity: O(n) : Height of stack


def insertion_sort_recur(arr, end):
    if end == 0: #Stop calling when only one element remains
        return
    
    insertion_sort_recur(arr, end - 1) #Recursively call insertion sort
    key = arr[end]

    #First element is always sorted, now start sorring from second element
    insert(arr, end, key) 

def insert(arr, index, key):
    if index >= 1 and key < arr[index - 1]:
        arr[index] = arr[index - 1]
    else:
        arr[index] = key
        return
    insert(arr, index - 1, key)



arr = [9, 7, 6, 0, 2, 1, -9]
insertion_sort_recur(arr, len(arr) - 1)
print(f"Array after sorting: {arr}")