

n=5

DP=[0 for x in range(n+1)]

DP[0] = DP[1] = DP[2] = 1
DP[3] = 2
for i in range(4,n+1):
    DP[i] = DP[i-1] + DP[i-3] + DP[i-4]

print(DP[n])