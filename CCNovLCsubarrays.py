# n,q,L,R= [int(x) for x in input().split()]
#
# arr = [0 for x in range(n)]
# dp=[[0 for x in range(n)] for y in range(n)]
# for x in range(n):
#     for y in range(x+1,n):
#         dp[y][x]=-1
# dpbool = [[False for x in range(n)] for y in range(n)]
#
#
# def check(l,r):
#     cnt=0
#     for i in range(l,r+1):
#         offset=0
#         while l+offset!=r+1:
#             if dpbool[i][l+offset]==True:
#                 cnt+=1
#             offset+=1
#     print(cnt)
#
#
# def rearrange(val,pre,pos):
#
#     for i in range(pos+1):
#         for j in range(pos,n):
#             dp[i][j]=max(dp[i][j]-pre,val)
#             if dp[i][j] in range(L,R):
#                 dpbool[i][j]=True
#             else:
#                 dpbool[i][j] = False
#
#
# for i in range(q):
#     temp = [int(x) for x in input().split()]
#     if temp[0]==1:
#         rearrange(temp[2],arr[temp[1]-1],temp[1]-1)
#         arr[temp[1]-1]=temp[2]
#     else:
#         check(temp[1]-1,temp[2]-1)


n, q, L, R = [int(x) for x in input().split()]

arr = [0 for x in range(n)]
dp = [[0 for x in range(n)] for y in range(n)]
for x in range(n):
    for y in range(x + 1, n):
        dp[y][x] = -1


def check(l, r):
    cnt = 0
    for i in range(l, r + 1):
        offset = 0
        while l + offset != r + 1:
            if dp[i][l + offset] in range(L, R):
                cnt += 1
            offset += 1
            if l + offset == r + 1:
                break
    return cnt


def rearrange(val, pos):
    for i in range(pos + 1):
        for j in range(pos, n):
            if dp[i][j] != (-1, -1):
                if dp[i][j]<=val:
                    dp[i][j]=val
                else:
                    dp[i][j] = max(arr[i:j + 1])

cnt=0
process ={}
for i in range(q):
    temp = [int(x) for x in input().split()]
    if temp[0] == 1:
        cnt += 1
        process[temp[1]-1] = temp[2]
    else:
        for j in process.keys():
            arr[j] = process[j]
            rearrange(process[j], j)
            cnt=0
        print(check(temp[1] - 1, temp[2] - 1))