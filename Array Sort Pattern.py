import array as ar
a=ar.array('i',[1,14,4,12,67,225,351])
length=len(a)
l=list(a)
l1=[]
l2=[]
for i in range(0,length//2):
        l1.append(l[i])
        l2.append(l[length // 2 + i])
l1.sort()
l2.sort(reverse=True)
#print(l2)
l1.extend(l2)
print(l1)