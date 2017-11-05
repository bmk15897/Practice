n , q =[int(x) for x in input().split()]
ax = [int(x) for x in input().split()]
idol = [int(x) for x in input().split()]

dp = [[-1,-1] for x in range(n)]

def fun(x):
    if x==1:
        return [ax[0],1]
    else:
        if dp[idol[x-2]][0]!=-1:
            return [dp[idol[x-2]]]
        else:
            if fun(idol[x-2]).__getitem__(0)+1<ax[x-1]:
                dp[x-1][0]=ax[x-1]
                dp[x-1][1]=1
            elif fun(idol[x-2]).__getitem__(0)+1>ax[x-1]:
                dp[x-1][0]=fun(idol[x-2]).__getitem__(0)+1
                dp[x-1][1]=dp[idol[x-2]][1]
            else:
                dp[x-1][0]=fun(idol[x-2]).__getitem__(0)+1
                dp[x-1][1]=dp[idol[x-2]][1]+1
            return dp[x-1]


for i in range(q):
    temp = [int(x) for x in input().split()]
    if temp[0] == 0:
        axtemp = ax[0]
        ax[temp[1]]=temp[2]
        dp = [[-1, -1] for x in range(n)]
    else:
        ans = fun(temp[1])
        print(ans[0]," ",ans[1])

# def fun(x):
#     if dp[idol[x]] != -1:
#         return dp[x]
#     else:
#         if fun(x)
#
# for i in range(q):
#     temp = [int(x) for x in input().split()]
#     if temp[0]==0:
#         axtemp = ax[0]
#         ax = [x+temp[1]-axtemp for x in ax]
#         dp = [-1 for x in range(n)]
#     else:
#         #for j,e in enumerate(ax):
