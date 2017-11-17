t = int(input())
def sign(x):
    if x<0:
        return -1
    else:
        return 1
for _ in range(t):
    n =int(input())
    arr = [int(x) for x in input().split()]
    dict = [1 for x in range(n)]
    i = n-2
    dict[n-1] = 1
    while(i>-1):
        if sign(arr[i])!=sign(arr[i+1]):
            dict[i]=1+dict[i+1]
        else:
            dict[i]=1
        i-=1
    print(*dict)