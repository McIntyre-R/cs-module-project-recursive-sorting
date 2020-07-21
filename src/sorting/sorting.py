# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0
    r = 0
    while len(arrA)>i and len(arrB)>j:
        if arrA[i]<arrB[j]:
            merged_arr[r] = arrA[i]
            i+=1
        else:
            merged_arr[r] = arrB[j]
            j+=1
        r+=1

    while i < len(arrA):
        merged_arr[r] = arrA[i]
        i+=1
        r+=1
    while j < len(arrB):
        merged_arr[r] = arrB[j]
        j+=1
        r+=1

    return merged_arr
            

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)
        
        new_arr = merge(left_arr,right_arr)

        return new_arr

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

