for _ in range(int(input())):
    n=int(input())
    nList=list(map(int,input().split()))
    x=[]
    for item in range(1000):
        x.append(0)
    for item in nList:
        x[item]+=1
    i=min(nList)
    j=max(nList)
    count=0
    area=1
    while j>=i:
        if x[j]>1:
            area*=j
            count+=1
            if count==2:
                print (area)
                break
            x[j]-=2
        else:
            j-=1
    else:
        print (-1) 