arr=[1,4,2,1,6,4,2,1,3,5,6,4,2,1]
max_num=arr[0]
for i in range(len(arr)):
    if arr[i]>max_num:
        max_num=arr[i]
count=[0  for i in range(max_num+1)]
for i in range(len(arr)):
    count[arr[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i)