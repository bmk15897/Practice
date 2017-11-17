t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt=0
    sum=0
    for i in s:
        if i == '1':
            cnt+=1
            sum+=cnt
    print(sum)