t = int(input())
for _ in range(t):
    n,q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort(reverse=True)
    for _ in range(q):
        k = int(input())
        ans = 0
        for i in range(n):
            if arr[i]>=k:
                ans+=1
            else:
                break
        if ans==n:
            print(n)
        else:
            if ans==0:
                rem = n-1
            else:
                rem = n-ans-1
            needed = k - arr[ans]
            i = ans+1
            while(needed<=rem):
                ans+=1
                rem = rem - k + arr[i] -1
                needed = k - arr[i]
                i+=1
            print(ans)


