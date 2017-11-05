n = int(input())
arr=[]
for i in range(n):
    e,l,r=[int(x) for x in input().split()]
    arr.append(e)
    cnt = 0
    for j in range(l,r+1):


























#cnt = 0
# t = int(input())
# cntr = {}
# cntr1 = {}
# li = [int(i) for i in input().split()]
# for i in range(len(li)):
#     if li[i] not in cntr:
#         cntr[li[i]] = i
#
# for i in range(len(li) - 1, -1, -1):
#     if li[i] not in cntr1:
#         cntr1[li[i]] = i
#
# for x in li:
#     val = cntr1[li[i]] - cntr[li[i]] + 1
#     if (cnt < val):
#         cnt = val
# print(cntr, cntr1)
# print(cnt)