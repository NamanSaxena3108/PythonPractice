#create a recursive function
def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)


result = Factorial(5)
print(result)