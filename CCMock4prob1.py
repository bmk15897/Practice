t = int(input())
for _ in range(t):
    n = int(input())

    arr = [int(x) for x in input().split()]

    i=1
    c = 0
    flag = 1
    p = arr[:n//2 + 1]
    while(i<8):

        if arr[c]!=i:
            flag =0
            break
        c += p.count(i)

        if c==0:
            flag=0
            break
        i+=1
    rev = arr[::-1]
    if arr==rev and flag:
        print('yes')
    else:
        print('no')
