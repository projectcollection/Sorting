#helpers 

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): #O(n)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for index, item in enumerate(arr[cur_index:]): #O(n)
            smallest = arr[smallest_index]
            if item < smallest:
                smallest_index = cur_index + index
        # TO-DO: swap
        swap(arr, cur_index, smallest_index)
    return arr 

#O(n^2)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorted = False
    while not sorted:
        swaps = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                swaps += 1
        if(swaps == 0):
            sorted = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return []
    elif min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    maximum = max(arr) + 1
    count = [0] * maximum
    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    sorted = [0] * count[-1] 

    for i in arr:
        sorted[count[i] - 1] = i
        count[i] -= 1
        
    return sorted