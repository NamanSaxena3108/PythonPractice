import array as ar
a=ar.array('d',[10,20.4,30,40])
for i in range(0,len(a)):
    print(a[i],'\n', end=" ")
a.append(50)
a.insert(2,25)
print(a)
