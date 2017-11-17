t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    sum1 = sum(arr[:k])
    sum2 = sum(arr[k:])
    temp = abs(sum2-sum1)
    sum1 = sum(arr[:n-k])
    sum2 = sum(arr[n-k:])
    temp1 = abs(sum2-sum1)
    print(max(temp,temp1))