import array as ar
a=ar.array('i',[10,20,30,40])
for i in a:
    print(i,end=" ")
print()
print("popped element:",a.pop(2))
for i in a:
    print(i)
print()