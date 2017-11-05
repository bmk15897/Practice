t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(arr[(n+k)//2])