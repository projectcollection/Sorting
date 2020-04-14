def add_remaining(append_to, to_check, curr_index, append_to_index):
    while curr_index < len(to_check):
        append_to[append_to_index] = to_check[curr_index]
        curr_index += 1
        append_to_index += 1
    return append_to_index

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    i = j = k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    if i < len(arrA):
        add_remaining(merged_arr, arrA, i, k)
    else: 
        add_remaining(merged_arr, arrB, j, k)
        
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
