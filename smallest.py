l=[5,6,4,2,3,8,1,9,8]
num=int(input())
s=set(l)
l1=list(s)
while num!=0:
    ms=min(l)
    l.remove(ms)
    num-=1
print(ms)
    