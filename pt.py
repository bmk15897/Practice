







def fnumber(k,arr):
    dic={}
    n=arr.__len__()
    for i in range(arr.__len__()):
        temp=[]
        print("i = ",i)
        for j in range(n-arr[i]+1):
            print("j = ", j)
            temp.append(arr[j:j+arr[i]])
        dic[i]=max([sum(x) for x in temp])
    print(min([dic[x] for x in dic if dic[x]>k]))
    temp=[]
    for ke, va in dic.items():
        if va >= k:
            temp.append(ke+1)
    print(min(x for x in temp))
    return 0


ip1 = int(input())
ip2_cnt = int(input())
ip2_i=0
ip2 = []
while ip2_i < ip2_cnt:
    ip2_item = int(input())
    ip2.append(ip2_item)
    ip2_i+=1

output = fnumber(ip1,ip2)
print(str(output))