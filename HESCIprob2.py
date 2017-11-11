k, n = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
if n > k:
    cnt = 0
    temp = []
    while (cnt != k):
        if cnt == k - 1:
            temp.append(sum(arr[:k]))
        else:
            temp.append(sum(arr[:cnt]) + sum(arr[-k + cnt:]))
        cnt += 1
    print(max(temp))
else:
    print(sum(arr))


#
# arr.sort(reverse=True)
# sum=0
# for i in range(k):
#     sum+=arr[i]
# print(sum)
#


# if n!=k:
#     i=0
#     j=n-1
#     cnt=0
#     sum=0
#     while cnt!=k:
#         if arr[i]>arr[j]:
#             sum+=arr[i]
#             arr.remove(arr[i])
#             i+=1
#             j-=1
#         else:
#             sum+=arr.pop()
#             j-=1
#         cnt+=1
#     print(sum)
# else:
#     print(sum(arr))






#
# k,n=[int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# sum1=sum2=0
# size=arr.__len__()
# for i in range(k):
#     sum1+=arr[i]
#     sum2+=arr[size-1-i]
# print(max(sum1,sum2))



#
# k,n=[int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# size=arr.__len__()
# prevmax=0
# if n!=k:
#     for i in range(n-k):
#         sum1 = sum2 = 0
#         for j in range(k):
#             sum1+=arr[i+j]
#             sum2+=arr[size-1-i-j]
#         thismax=max(sum1,sum2)
#         if thismax>=prevmax:
#             prevmax=thismax
#     print(prevmax)
# else:
#     print(sum(arr))
