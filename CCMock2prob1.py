t = int(input())
for _ in range(t):
    n,c = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    s = sum(arr)
    if c>=s:
        print('Yes')
    else:
        print('No')