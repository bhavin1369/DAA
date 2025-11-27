def min_max(arr):
    if len(arr)==1:
        return arr[0], arr[0]
    mid= len(arr) // 2
    l_min, l_max = min_max(arr[:mid])
    r_min, r_max = min_max(arr[mid:])
    return min(l_min, r_min), max(l_max, r_max)
arr= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(min_max(arr))