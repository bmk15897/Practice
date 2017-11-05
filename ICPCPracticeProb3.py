t = int(input())
for i in range(t):
    n,m = [int(x) for x in input().split()]
    if n==1:
        print(0)
    elif n==2:
        print(m)
    else:
        print(((n-1)+2*(m-1)))