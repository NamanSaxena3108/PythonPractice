import array as ar
arr =ar.array('i',[])
for i in range(0,10):
    a=int(input("enter the number"))
    arr.append(a)
n = len(arr)
for i in range(n-1):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")