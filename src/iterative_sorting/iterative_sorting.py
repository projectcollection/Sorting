#helpers 

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for index, item in enumerate(arr[cur_index:]):
            smallest = arr[smallest_index]
            if item < smallest:
                smallest_index = cur_index + index
        # TO-DO: swap
        swap(arr, cur_index, smallest_index)
    return arr 


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

    return arr