n=int(input())
arr=[int(x) for x in input().split()]
a=[0 for x in range(arr.__len__())]
b=[0 for x in range(arr.__len__())]
for i in range(arr.__len__()):
    if arr[i]==0:
        j=i
        while j< arr.__len__() and arr[j]==0:
            a[i]+=1
            j+=1
    if arr[i]==1:
        j=i
        while j< arr.__len__() and arr[j]==1:
            b[i]+=1
            j+=1
print(min(max(a),max(b)))