n,x,y = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [(A[i]-B[i],i) for i in range(n)]
tipwho = [0]*n
C.sort(key=lambda y: y[0])
for i in range(n):
    if C[i][0]>=0 and i>=n-x:
        break
    else:
        tipwho[C[i][1]]=1
tottip = 0
for i in range(n):
    if tipwho[i]==0:
        tottip+=A[i]
    else:
        tottip+=B[i]
print(tottip)