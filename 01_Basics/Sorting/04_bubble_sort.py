



#Approach one: Using iterative algo.
#Time complexity: O(n^2) :  worst/avg
#Time complexity: O(n) : Best case when array is already sorted or having few unsorted elements
#Space complexity: O(1)


def bubble_sort_iter(arr):
    length = len(arr)
    '''
    It's a flag that is used to know weather the array is already sorted
    or not, it also helps us to exit earlier if we need some swaps only
    e.g     : [1, 2, 120, 20, 21, 90, 99]
    '''

    for i in range(length):
        swapped = False #Set flag 

        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]: #Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True #Set flag

        #Check if there's no swap then exit earlier
        if not swapped:
            break







arr = [1, 2, 9, 0, -1, 22, 90, 987]
bubble_sort_iter(arr)
print(f"Array after sorting is: {arr}")



#Approach Second: Using recursive algo.
#Time complexity: O(n^2) :  worst/avg
#Time complexity: O(n) : Best case when array is already sorted or having few unsorted elements
#Space complexity: O(n) : Height of stack
def bubble_pass(arr, i, last, swapped):
    if i == last:
        return swapped
    
    #Swap if adjancent elements are not in desired order
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True

    return bubble_pass(arr, i + 1, last, swapped)



def bubble_sort_recur(arr, last):
    if last == 0:
        return
    
    #Perfrom one full bubble pass
    swapped = bubble_pass(arr, 0, last, False)

    #If not swapped then, already sorted
    if not swapped:
        return
    #Call bubble sorted recursively
    bubble_sort_recur(arr, last - 1)



arr = [5, 200, 9, 10, 1]

bubble_sort_recur(arr, len(arr) - 1)
print(f"Array after sorting is: {arr}")
