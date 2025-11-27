def partition(arr, st, end):
    idx = st - 1
    pivot = arr[end]
    for j in range(st, end):
        if arr[j] <=pivot:
            idx += 1
            arr[j], arr[idx] = arr[idx], arr[j]
    arr[end], arr[idx + 1] = arr[idx + 1], arr[end]
    return idx + 1

def quicksort(arr, st, end):
    if st < end:
        pivot = partition(arr, st, end)
        quicksort(arr, st, pivot - 1)#left half
        quicksort(arr, pivot + 1, end)#right half

arr = [12, 31, 35, 8, 32, 17]
quicksort(arr, 0, len(arr) - 1)
print(arr)

