#update the first set with item that doesn't exist in second set
set1={1,2,3,4}
set2={3,4,5,6}
update=set2 - set1
set1.update(update)
print("the updates list is:",set1)