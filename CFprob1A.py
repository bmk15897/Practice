import math
m,n,a=[int(x) for x in input().split()]
p=math.ceil(m/a)
q=math.ceil(n/a)
print(p*q)