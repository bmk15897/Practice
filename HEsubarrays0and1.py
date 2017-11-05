
# k = int(input())
# lst = [int(x) for x in input().split()]
#
# lst.sort()
# if(lst[0]==0):
#     lst[0]=1
#
# count = 0
# def subs(l):
#     global count
#     if sum(l) % 2 != 0:
#         count += 1
#     if l == []:
#         return [[]]
#
#     if sum(l) % 2 != 0:
#          count += 1
#     x = subs(l[1:])
#
#     return x + [[l[0]] + y for y in x]
#
# lst = subs(lst)
# print(count)
#
# # for ls in lst:
# #     if(ls!=[]):
# #         tempsum = sum(ls)
# #         if tempsum % 2 != 0:
# #             count += 1
#
#
#
# #
# #
# # k = int(input())
# # lst = [int(x) for x in input().split()]
# #
# # count = 0
# # def subs(l):
# #     if l == []:
# #         return [[]]
# #     x = subs(l[1:])
# #     global count
# #     if sum(l) % 2 != 0:
# #         count += 1
# #     return x + [[l[0]] + y for y in x]
# #
# # lst = subs(lst)
# # print(count)
# #
# # #
# # # for ls in lst:
# # #
# # #     if(ls!=[]):
# # #         tempsum = sum(ls)
# # #         if tempsum % 2 != 0:
# # #             count += 1
#
#
# #submission one
# #
# # k = int(input())
# # lst = [int(x) for x in input().split()]
# # def subs(l):
# #     if l == []:
# #         return [[]]
# #
# #     x = subs(l[1:])
# #
# #     return x + [[l[0]] + y for y in x]
# # lst = subs(lst)
# # count = 0
# # for ls in lst:
# #     if(ls!=[]):
# #         tempsum = sum(ls)
# #         if tempsum % 2 != 0:
# #             count += 1
# # print(count)