

#NOT DONE








n,m = [int(x) for x in input().split()]
square = [[0 for x in range (50)] for y in range(50)]

prevpnt = [-1,-1]
thispnt = [-1,-1]

def drawline(prevpnt,thispnt):
    for

def maxele(arr):
    maxA=0
    for i in range(n):
        temp = max(arr[i])
        if maxA<=temp:
            maxA=temp
    if
    return maxA

for i in range(m):
    arr = [[] for y in range(3)]
    for j in range(n):
        temp = [int(x) for x in input().split()]
        for k in range(n):
            arr[j].append(temp[k])
    temp = arr.copy()
    print(maxele(temp))