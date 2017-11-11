n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
cnt=0
if arr[k-1]!=0:
    j=k
    cnt=k
    if j!=n:
        while(arr[j]==arr[k-1]):
            cnt+=1
            j+=1
            if j==n:
                break
    else:
        cnt=n
    print(cnt)
else:
    j=k-1
    m=arr.index(0)
    if m!=0:
        cnt=m
    print(cnt)
