#copy specific element from tuple 1 to a new tuple
tup=(1,2,3,4,5,6)
copy=(1,3,5)
new_tuple=tuple(tup[i] for i in copy)
print(new_tuple)