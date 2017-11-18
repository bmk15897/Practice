from itertools import combinations


t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    l = 1
    ans = 0^k
    sub = []
    while l<=n:
        # print(l)
        for i in combinations(arr,l):
            print(i)
            if (sum(i)^k)>ans:
                ans = sum(i)^k
        l+=1
    print(ans)
