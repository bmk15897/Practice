
t = int(input())
for i in range(t):
    y=int(input())
    maxA=int((y**0.5)//1)
    cnt=0
    while maxA>0:
        temp=(maxA)**2
        if 0<=y-(temp)<700:
            cnt += y - temp
            maxA-=1
            temp=(maxA)**2
            while 0<=y-(temp)<700 and maxA>1:
                cnt+=temp-(maxA-1)**2
                maxA-=1
                temp=(maxA) ** 2
        else:
            cnt+=700
            maxA-=1
    print(int(cnt))




















    '''    for j in range(1,701):
        if (maxA+1)**2+j<=y:
            cnt+=1
    maxA-=1
    while ((maxA + 1) ** 2 - maxA ** 2) < 700 and maxA!=-1:
        for j in range(1, 701):
            if (maxA + 1) ** 2 + j <= y:
                cnt += 1
        maxA -= 1'''