#
# t = int(input())
# for i in range(t):
#     x=1
#     try:
#         checkpoints = int(input())
#         cost = [int(x) for x in input().split()]
#         amount = [int(x) for x in input().split()]
#         min = cost[0]
#         loc = 0
#         reqsum = 0
#         for i,item in enumerate(cost):
#             if(min>item):
#                 loc=i
#                 min=item
#             temp = min*amount[i]
#             reqsum += temp
#         print(reqsum)
#     except ValueError:
#         x += 1


t = int(input())
for i in range(t):
    checkpoints = int(input())
    cost = [int(x) for x in input().split()]
    amount = [int(x) for x in input().split()]
    min = cost[0]
    reqsum = 0

    for point,litreq in zip(cost,amount):
        if(min>point):
            min=point
        temp= min*litreq
        reqsum+=temp
    print(reqsum)

    # for item in cost:
    #     if(min>item):
    #         min=item
    #     temp = min*amount[i]
    #     reqsum += temp

