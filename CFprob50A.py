import math
m,n=[int(x) for x in input().split()]
ans1 = math.floor(n/2)*math.floor(m/1)
ans2 = math.floor(m/2)*math.floor(n/1)

print(max(ans1,ans2))