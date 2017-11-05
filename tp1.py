def fnumber(k,arr):
    n=arr.__len__()
    temp1=[0]
    for i in range(n):
        if i>0:
            temp=[]
            for j in range(n-arr[i]+1):
                tempsum=arr[j]
                num=j
                cnt=0
                print(arr[j])
                while num<n and cnt<arr[j]:
                    tempsum+=arr[j]
                    num+=1
                    cnt+=1
                print(tempsum)
                temp.append(tempsum)   #stores subarray of required f-number
            print(temp)
            temp1.append((max([x for x in temp]))) #gets max of that subarray

    if [x for x in temp1 if x>=k]:
        return temp1.index(min([x for x in temp1 if x>k]))
    elif sum(arr)>k:
        return arr.pop()
    else:
        return -1




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