l=[5,7,6,3,9,7]
l1=l.copy()
n=int(input("Enter the number :"))
left=[l[n:]+l[:n]]
right=[l[-n:]+l[:-n]]
print(left)
print(right)

