def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1,2,3,4,5]
target = int(input("Enter target element: "))
index = linear_search(arr, target)
if index != -1:
    print("Target element found at index", index)
else:
    print("Target element not found")
