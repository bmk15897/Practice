t = int(input())
for _ in range(t):
    str = input()
    cnt = str.count('1')
    if cnt!=0:
        pos = str.index('1')
        temp = 0
        length = str.__len__()
        while(pos<length and str[pos]=='1'):
            temp+=1
            pos+=1
        if temp==cnt:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')