t = int(input())
DP = [0 for x in range(100001)]
DP[0]=DP[1]=1
def fact(n):
    if DP[n]!=0:
        return DP[n]%(1000000007)
    DP[n] = fact(n-1)*n
    return DP[n]%(1000000007)
for i in range(t):
    print(fact(int(input()))%1000000007)