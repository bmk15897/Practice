t = int(input())
for _ in range(t):
    x,y,k,n = [int(x) for x in input().split()]
    arr=[]
    flag=0
    for i in range(n):
        temp = [int(x) for x in input().split()]
        if temp[1]<=k:
            if temp[0]>=x-y:
                flag = 1
    if flag==1:
        print('LuckyChef')
    else:
        print('UnluckyChef')