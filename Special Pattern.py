n=int(input())
main_list=[]
for i in range(0,n):
    number_list=int(input())
    l1=list(map(int,input().split()))
    if number_list==len(l1):
        main_list.append(l1)
    else:
        exit()
for j in range(0,len(main_list)):
    dic={}
    l2=[]
    profit=0
    l2.extend(main_list[j])
    if j!=(len(main_list)-1):
        for i in range(0,len(l2)):
            dic[i]=l2[i]
        for k in range(1,2):
            buy1  = dic[k]
            sell1 = dic[k+1]
            buy2  = dic[k+2]
            sell2 = dic[k+3]
            profit=(sell1-buy1)+(sell2-buy2)
            print(profit)
    if j==(len(main_list)-1):
        for i in range(0,len(l2)):
            dic[i]=l2[i]
        for k in range(0,1):
            buy1 = dic[k]
            sell1 = dic[k+4]
            profit=(sell1-buy1)
            print(profit)

'''
input
3
6
6 1 4 2 5 3
7 
6 1 4 2 5 3 5
5
1 2 3 4 5
output
6
6
4
'''