t = int(input())
for _ in range(t):
    s = input()
    size = s.__len__()
    dict1 = {}
    dict2 = {}
    if size%2==0:
        for i in s[:size//2]:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in s[size//2:]:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
    else:
        for i in s[:size//2]:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in s[size//2+1:]:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
    flag = 0
    for i in set(s[:size//2]):
        if i in dict1 and i in dict2:

            if dict1[i]!=dict2[i]:
                flag=1
                break
        else:
            flag=1
            break

    if flag==1:
        print('NO')
    else:
        print('YES')

