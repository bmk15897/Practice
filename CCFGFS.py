t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    cust_comp={}
    for _ in range(n):
        s,e,c = [int(x) for x in input().split()]
        if c not in cust_comp:
            cust_comp[c]=[[s,e]]
        else:
            cust_comp[c].append([s,e])
    ans =0
    for i in cust_comp:
        cust_comp[i].sort(key=lambda x:x[1])
        # print(cust_comp[i])
        m = cust_comp[i][0][1]
        ans+=1
        ln = len(cust_comp[i])
        for j in range(1,ln):
            if cust_comp[i][j][0]>=m:
                m=cust_comp[i][j][1]
                ans+=1
    print(ans)