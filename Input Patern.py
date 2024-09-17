no_of_array=int(input())
main_list=[]
for i in range(0,no_of_array):
    size_of_array=int(input())
    user_list=list(map(lambda x:int(x) * 2,(input()).split()))
    if size_of_array==len(user_list):
        main_list.append(user_list)
    else:
        exit()
length=len(main_list)
for j in range(0,length):
    print(main_list[j])