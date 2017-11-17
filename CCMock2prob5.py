t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    i = [0]*n
    j = [0]*n
    k = [0]*n
    l = [0]*n

    i[0] = j[0] = arr[0]

    for q in range(1,n):
        i[q] = max(i[q-1]+arr[q],arr[q])
        j[q] = min(j[q-1]+arr[q],arr[q])

    k[n-1] = l[n-1] = arr[n-1]

    for q in range(n-2,0,-1):
        k[q] = max(k[q+1]+arr[q],arr[q])
        l[q] = min(l[q+1]+arr[q],arr[q])

    ans = max(abs(i[0] - l[1]),abs(j[0] - k[1]))
    for q in range(1,n-1):
        ans = max(ans,max(abs(i[q] - l[q+1]),abs(j[q] - k[q+1])))
    print(ans)
