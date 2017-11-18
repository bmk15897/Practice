t = int(input())
# store = {}
# store[0] = 1
# store[1] = 1
for _ in range(t):
    n = int(input())
    # for i in range(n):
    #     if i not in store:
    #         store[i]=store[i-1]+i
    arr = [int(x) for x in input().split()]
    num = 0
    count = [0]*n

    for i in range(n):
        if i==0:
            count[i]=1
        elif arr[i]>=arr[i-1]:
            count[i]+=count[i-1]+1
        else:
            count[i]=1

    for i in range(count.__len__()):
        num = num+count[i]
    print(num)
    # prevloc = 0
    # num = 0
    # for loc,item in enumerate(arr):
    #     if item < arr[loc-1]:
    #         num+=store[loc - prevloc]
    #         prevloc = loc
    #     else:
    #         if loc==n-1:
    #
    #
