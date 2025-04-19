def insertion_sort(arr, left, right):
    
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):

    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def hybrid_sort(arr, left, right):
    threshold = 32  
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
    else:
        mid = (left + right) // 2
        hybrid_sort(arr, left, mid)
        hybrid_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def sort(arr):
    if len(arr) > 1:
        hybrid_sort(arr, 0, len(arr) - 1)