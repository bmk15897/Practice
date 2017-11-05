t = int(input())
for i in range(t):
    n,p=[int(x) for x in input().split()]
    if n==p:
        if n>2:
            str='a'
            for x in range(n-2):
                str+='b'
            str+='a'
            print(str)
        else:
            print('impossible')
    elif p==1:
        print('impossible')
    elif n<p:
        print('impossible')
    elif p==2:
        print('impossible')
    else:
        str = 'a'
        for x in range(p - 2):
            str += 'b'
        str += 'a'
        str1=""
        for j in range(n//p):
            str1+=str
        print(str1)