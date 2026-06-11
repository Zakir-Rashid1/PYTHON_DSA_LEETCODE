

#Approach Second: Using divide and conquer (LOMUTO PARTITITON SCHEME)
#Time complexity: O(n^2) :  worst : Wen array is already sorted, or contains same elements
#Time complexity: O(nlogn) : Best case/avg. case when array is unsorted or doesn't contains same elements
#Space complexity: O(n) : Worst case: sorted or same element case
#Space complexity: O(logn) : Best case: unsorted or all element are not same

def lomuto_partition(arr, low, high):
    pivot = arr[high] #Choose pivot arr[high] always
    i = low - 1

    for j in range(low, len(arr) - 1):
        if arr[j] < pivot:
            i += 1

            if i != j: #If i and j are not equal than swap
                arr[i], arr[j] = arr[j], arr[i]
    #Swap pivot with partition index
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1



def quick_sort_i(arr, low, high):
    if low < high:
        p = lomuto_partition(arr, low, high) #p is my partition index
        quick_sort_i(arr, low, p - 1) 
        quick_sort_i(arr, p + 1, high)



arr = [6, 10, 13, 5, 8, 3, 2, 11]
quick_sort_i(arr, 0, len(arr) - 1)
print(f"Array after sorting: {arr}")







#Approach Second: Using divide and conquer (HOARE PARTITITON SCHEME)
#Time complexity: O(n^2) :  worst : Wen array is already sorted, or contains same elements
#Time complexity: O(nlogn) : Best case/avg. case when array is unsorted or doesn't contains same elements
#Space complexity: O(n) : Worst case: sorted or same element case
#Space complexity: O(logn) : Best case: unsorted or all element are not same

def hoare_partition(arr, low, high):
    pivot = arr[low] #Choose pivot as arr[low] always
    i = low - 1 #i is used to maintain index for elements smaller than pivot
    j = high + 1 #j is used to maintain index for elements greater than pivot


    while True:
        i += 1
        while arr[i] < pivot: #Increment i whenever arr[i] < pivot
            i += 1
        
        j -= 1
        while arr[j] > pivot: #Decrement j whenever arr[j] > pivot
            j -= 1

        if i >= j:
            return j #Return partition index
        
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

        
def quick_sort_ii(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        '''
        y not low -> p -1 : Bcoz in HP pivot may or may not be
        in its correct/final position
        '''
        quick_sort_ii(arr, low, p)
        quick_sort_ii(arr, p + 1, high)




arr = [6, 10, 13, 5, 8, 3, 2, 11, -90]
quick_sort_ii(arr, 0, len(arr) - 1)
print(f"Array after sorting: {arr}")