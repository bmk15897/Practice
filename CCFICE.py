t = int(input())
dp = [0]*1001
dp[0]=dp[1]=1
def fibo(num):
    global dp
    print(dp[:10])
    if dp[num]!=0:
        return dp[num]
    else:
        dp[num]=fibo(num-1)+fibo(num-2)
        return dp[num]

for _ in range(t):
    n,m = [int(x) for x in input().split()]
    print((2*fibo(n+1))%m)