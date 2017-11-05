t=int(input())
for i in range(t):
    num,ele=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    arr=set(arr)
    tem=0
    while(ele!=0):
        if tem not in arr:
            ele -= 1
        else:
            arr.remove(tem)
        tem+=1
    while(tem in arr):
        tem+=1
    print(tem)