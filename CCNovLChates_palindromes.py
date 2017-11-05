import string,math
t=int(input())
li=list(string.ascii_lowercase)
for i in range(t):
    n,a=[int(x) for x in input().split()]
    if a>=n:
        print(1,''.join(li[:n]))
    else:
        if a%2==1:
            str=''.join(li[:a])
            str1=""
            for j in range(n//a):
                str1+=str
            str1+=str[:n%a]
            print(1,str1)
        else:
            str = ''.join(li[:a-1])
            lbit=li[a-1]
            str1 = ""
            k=n%a
            if k==0:
                for j in range(n//a):
                    str1+=str
                for j in range(n//a):
                    str1+=lbit
            else:
                for j in range(int(math.ceil(n/a))):
                    str1+=str
                for j in range(n-int(math.ceil(n/a))):
                    str1+=lbit
            print(int(math.ceil(n/a))-1,str1)

