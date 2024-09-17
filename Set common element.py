#check if two sets have element in common if yes the display them
set1={1,2,3,4}
set2={3,4,5,6}
common = set1 & set2
if common:
    print("common element",common)
else:
    print("no common element")