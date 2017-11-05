def fnumber(k,arr):
    n=arr.__len__()
    print(n)
    newarr = [[0 for x in range(n)] for y in range(n + 1)]
    res = [0 for x in range(n + 1)]
    resloc = [0 for x in range(n + 1)]
    for i in range(n):
        if (i >= 1):
            for j in range(n - i + 1):
                print(arr[j:j + i])
                temp = sum(arr[j:j + i])
                if temp > k:
                    newarr[i][j] = temp
            res[i] = max(newarr[i])
            resloc[i] = newarr[i][newarr[i].__len__()-1]

    res[n]=newarr[n][0]=sum(arr)
    resloc[n]=arr[n-1]
    print(newarr)
    print(res)
    print(resloc)
    #print(resloc[res.index(min(i for i in res if i > 0))])
    return resloc[res.index(min(i for i in res if i > 0))]

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