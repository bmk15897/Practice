nEle,nOp = input().split()
nEle = int(nEle)
nOp = int(nOp)

Arr = [int(x) for x in input().split()]

for t in range(nOp):
    op, x, y = input().split()
    x = int(x)
    y = int(y)
    if(op == 'U'):
        Arr[x] = y
        # print(Arr)
    else:
        i = x
        #count = 1
        # print(max(Arr[x:]) - Arr[x])
        # print(Arr.index((max(Arr[x:]))))
        if(max(Arr[x:]) - Arr[x] < y):
            ans2 = max(Arr[x:]) - Arr[x]
            ans1 = x-i+1
        elif i-x>1:
            ans2 = y
            ans1 = x - i + 1
        else:
            ans2 = -1
            ans1 = -1

        print(ans1,ans2)
        # while(i < nEle and (Arr[i] in range(Arr[x] - y, Arr[x] + y +1))):
        #     print(range(Arr[x]-y,Arr[x]+y +1))
        #     #count+=1
        #     i+=1
        # print(i-x+1)

