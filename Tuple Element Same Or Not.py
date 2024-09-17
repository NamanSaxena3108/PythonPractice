#wap to check if all the item in tuple are same or not
t=(10,10,10,10,10)
c=t.count(t[0])
l=len(t)
if c==l:
    print("all element are same ")
else:
    print("element are different")
