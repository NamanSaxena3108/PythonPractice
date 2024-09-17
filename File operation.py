f = open('C:/Users/RRIMT/Desktop/x1.txt', 'r')
lineno=int(input("enter the line"))
colineno=1
for lo in f:
    if colineno==lineno:
        print (lo)
        break
    colineno += 1
# print(f.read())
print(f.readline())