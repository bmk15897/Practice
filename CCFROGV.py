n,k,p = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
x_co = []
for i in range(n):
    x_co.append([arr[i],i])
x_co.sort(key=lambda x:x[0])
for _ in range(p):
    a,b = [int(x) for x in input().split()]
    start = a-1
    tstart = x_co.index([arr[start],start])
    end = b-1
    tend = x_co.index([arr[end],end])
    flag=0
    if tend>tstart:
        for i in range(tstart,tend):
            if x_co[i+1][0]-x_co[i][0]>k:
                flag = 1
                break
    elif tstart>tend:
        for i in range(tstart,tend-1,-1):
            if x_co[i][0]-x_co[i-1][0]>k:
                flag = 1
                break
    if flag==1:
        print('No')
    else:
        print('Yes')