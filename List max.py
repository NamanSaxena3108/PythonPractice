#to find the max item in list
l=[]
n=int(input("enter the no. of element"))
for i in range(0,n):
    a=int(input("enter the element"))
    l.append(a)
large=max(l)
print(f"the largest number is {large}")