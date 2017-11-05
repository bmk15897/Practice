n = int(input())
count = [[-1,-1] for x in range(0,100001)]
arr = [int(x) for x in input().split()]
for i,e in enumerate(arr):
    if(count[e][0]==-1):
        count[e][0]=i
    else:
        count[e][1]=i
print(max([count[i][1]-count[i][0] for i in range(0,100001)])+1)

