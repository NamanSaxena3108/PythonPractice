a = 0
b = 1
n = 0
print(a, b, sep=" ", end=",")
while n < 50:
    n = a+b
    print(n, end=",")
    a = b
    b = n
