t = int(input())
for i in range(t):
    n = int(input())
    arr = [85900 for x in range(n)]
    for j in range(49999,n):
        arr[j] = 1
    print(*arr)




# t = int(input())
# for i in range(t):
#     n = int(input())
#     parts = (((2**32)-1)//n)+1
#     sum=0
#     arr = [0 for x in range(n)]
#     # for k in range(n):
#     #     arr[k] =(parts+k)
#     #     if k!=1:
#     #         sum+=k
#     # arr[1]=sum+1
#     # print(*arr)
#     for k in range(n):
#         if k<99991:
#             arr[k]=10^5
#         for
