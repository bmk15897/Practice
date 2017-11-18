arr = [5,4,6,6,2,1,3]
count = [0]*10
count1 = [0]*10
for i in arr:
    print(i)
    count[i]+=1
for i in range(10):
    count1[i]=count[i]+count1[i-1]
ans = []
for i in range(10):
    if i==0:
        for j in range(count1[i]):
            ans.append(i)
    else:
        for j in range(count1[i]-count1[i-1]):
            ans.append(i)
print(ans)