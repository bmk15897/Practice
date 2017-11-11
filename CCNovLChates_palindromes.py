import string,math
t=int(input())
li=list(string.ascii_lowercase)
for i in range(t):
    n,a=[int(x) for x in input().split()]
    if a >= n:
        print(1, ''.join(li[:n]))
    elif a==2:
        if n==1:
            print(1,'a')
        elif n==2:
            print(1,'ab')
        elif n==3:
            print(2,'aab')
        elif n>= 10:
            temp = 'baab'
            m=n-10
            k=0

            rem = n - 4
            ans = temp
            l = 1
            while (rem != 0):
                rem-=1
                if k==0:
                    print('ok')
            print(l-1, ans)
        else:
            temp='bab'
            rem = n-3
            ans=temp
            l=1
            while(rem!=0):
                ans='a' + ans
                rem-=1
                l+=1
                if(rem!=0):
                    ans=ans+'b'
                    rem-=1
            if n==5:
                print(l+1,ans)
            if n==10:
                print(l-1,ans)
            else:
                print(l,ans)
    else:
        str=''.join(li[:a])
        str1=""
        for j in range(n//a):
            str1+=str
        str1+=str[:n%a]
        print(1,str1)

