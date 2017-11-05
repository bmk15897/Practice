t = int(input())

DP=[[-1 for x in range(1001)] for y in range(1001)]

def probablity(r,g):
    if r==0 or g==0:
        return float (1)
    if DP[r][g]!=-1:
        return DP[r][g]

    DP[r][g] =
    return DP[r][g]
for i in range(t):
    R,G = [int(x) for x in input().split()]
    print(probablity(R,G))