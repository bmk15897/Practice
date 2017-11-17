t =int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    arr = [int(x)+k for x in input().split()]
    cnt = 0
    for i in arr:
        if i%7==0:
            cnt+=1
    print(cnt)