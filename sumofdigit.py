n=int(input())
oddsu=0
evensu=0
p=1
while n>0:
    b=n%10
    n=n//10
    if p & 1:
        oddsu+=b
    else:
        evensu+= b
    p = p +1
print(oddsu-evensu)