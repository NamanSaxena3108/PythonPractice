l=[5,4,3,2,6,1,8,9,2]
n=int(input("enter the number"))
s=set(l)
l1=list(s)
while n!=0:
    ma=max(l1)
    mn=min(l1)
    l1.remove(ma)
    l1.remove(mn)
    n -= 1
print(ma,mn)
