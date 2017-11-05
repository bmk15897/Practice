t = int(input())

for i in range(t):
    count = [0 for x in range(0, 101)]
    n = int(input())
    arr = [int(x) for x in input().split()]
    for x in arr:
        count[x]+=1
    j = 1
    while(count[j]!=1):
        j+=1
    print(j)