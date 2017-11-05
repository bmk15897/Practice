t=int(input())
for i in range(t):
    num,tot=[int(i) for i in input().split()]
    solved=[int(i) for i in input().split()]
    cnt1=cnt2=0
    for e in solved:
        if e>=tot//2:
            cnt1+=1
        if e<=tot//10:
            cnt2+=1
    if cnt1==1 and cnt2==2:
        print("yes")
    else:
        print("no")

