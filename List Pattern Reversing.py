list1=[100,200,300,400]
list2=[2,3,7,9]

list2 = list2[::-1]


for i in range(len(list1)):
    print(f"{list1[i]}, {list2[i]}")