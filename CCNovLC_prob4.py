import string
li=list(string.ascii_lowercase)

t = int(input())
for i in range(t):
    n,a=[int(x) for x in input().split()]
    if a>2:
        temp = "".join(li[:a])
        ans = ""
        for j in range(n // a):
            ans += temp
        ans += "".join(li[:n % a])
        print(1, ans)
    elif a==1:
        print(n,'a'*n)
    elif a==2:
        if n<9:
            dict={1:(1,'a'),2:(1,'ab'),3:(2,'abb'),4:(2,'aabb'),5:(3,'aabab'),6:(3,'aababb'),7:(3,'aaababb'),8:(3,'aaababbb')}
            print(dict[n][0],dict[n][1])
        else:
            temp='abbaab'
            str=""
            for i in range(n//6):
                str+=temp
            str+=temp[:n%6]
            print(4,str)