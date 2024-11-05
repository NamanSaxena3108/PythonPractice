arr= [28,29,18,13,23,25,16]
n=int(input())
arr.sort()
flag=0
u=0
l=len(arr)
while l >=0:
    mid = (u+l)//2
    if arr[mid]==n:
        flag = 1
        break
    elif arr[mid]>n:
        l=mid-1
    else:
        u=mid+1
if flag == 0:
    print("Number is not found")
else:
    print(f"Number is found at location {mid}")
