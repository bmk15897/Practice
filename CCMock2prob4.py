import bisect
t = int(input())
for _ in range(t):
    n = input()
    arr = [int(x) for x in input().split()]
    ans = []
    anslen = 0
    for i in arr:
        pos = bisect.bisect_right(ans,i)
        if pos==anslen:
            ans.append(i)
            anslen+=1
        else:
            ans[pos]=i
    print(anslen,*ans)
