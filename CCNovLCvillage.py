t = int(input())
for i in range(t):
    str = input()
    flag=0  #1 for A and 2 for B
    cA=0
    cB=0
    cnt=0
    for k in str:
        if k=='.':
            cnt+=1
        elif k=='A':
            if flag==1:
                cA+=cnt+1
                cnt=0
            else:
                cA+=1
                cnt=0
            flag=1
        else:
            if flag==2:
                cB+=cnt+1
                cnt=0
            else:
                cB+=1
                cnt=0
            flag=2
    print(cA,cB)