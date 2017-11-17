n,m = [int(x) for x in input().split()]
square = [[0 for x in range (50)] for y in range(50)]

# bigarray = [[[] for x in range(n)]for y in range(m)]

prevpnt = [-1,-1]
thispnt = [-1,-1]
cnt=0
for i in range(m):
    arr = [[] for x in range(n)]
    max = 0
    ti=-2
    tj=-2
    for j in range(n):
        temp = [int(x) for x in input().split()]
        for k in range(n):
            if temp[k]>=max and prevpnt!=[j,k]:
                max=temp[k]
                tj = k
                ti = j
                prevpnt=[ti,tj]
    if cnt<2:
        print(prevpnt[0]+1,prevpnt[1]+1)
    elif cnt==2:
        print(-1,-1)
    cnt+=1
    # bigarray[i]=arr

# print(bigarray)

