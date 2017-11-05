t = int(input())
for i in range(t):
    n,rid = [int(c) for c in input().split()]
    arr = [int(c) for c in input().split()]
    arrlow = 0
    arrhigh = 100000001

    for i,e in enumerate(arr):
        if e>rid:
            if e in range(rid,arrhigh):
                arrhigh=e
            else:
                print('NO')
                break
        if e<rid:
            if e in range(arrlow,rid):
                arrlow=e
            else:
                print('NO')
                break
    else:
        print('YES')