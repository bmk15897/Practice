t = int(input())
# DP=[[0 for x in range(100001)] for y in range(100001)]

for t in range(t):
    n,q=map(int,input().split())
    arr=[int(x) for x in input().split()]
    seglower = [[i, 0] for i in range(1, n + 1)]
    segupper = [[i, arr[i - 1]] for i in range(1, n + 1)]
    for j in range(q):
        op = [x for x in input().split()]
        if op[0] == '?':
            #query 2
            res=[]
            i,L,R = map(int,op[1:])
            rays = [[i - 0.5 , L + j - 1.5] for j in range(1,R - L + 2)]
            m = [x for x in range(1,n+1) if x > (i - 0.5)][0]
            shot = [0 for x in range(rays.__len__())]
            for num,ray in enumerate(rays):
                k=m
                while(k<=n):
                    if seglower[k - 1][1] <= ray[1] <= segupper[k - 1][1]:
                        shot[num]=k
                        break
                    k+=1
            temp = set(shot)
            if 0 in temp:
                print(temp.__len__()-1)
            else:
                print(temp.__len__())
        else:
            #query 1
            i, X = map(int, op[1:])
            arr[i-1] = arr[i-1]+X
            #seglower = [[i, 0] for i in range(1, n + 1)]
            #segupper = [[i, arr[i - 1]] for i in range(1, n + 1)]
            segupper[i-1]=[i,arr[i-1]]


# for k in range(m,n+1):
            #     print("k = ",k)
            #     for ray in rays:
            #         print(res)
            #         print(seglower[k - 1][1], ray[1], segupper[k - 1][1])
            #         if k in res:
            #             break
            #         elif seglower[k-1][1]<=ray[1]<=segupper[k-1][1]:
            #             #if k not in res:
            #             res.append(k)
            #             break
            #     if k != n:
            #         seglower[k][1] = segupper[k - 1][1]
            #     print("OK")