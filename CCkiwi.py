t=int(input())
for i in range(t):
    s=input()
    x,y=[int(x) for x in input().split()]
    lim1=s.count('a')
    lim2=s.count('b')
    cnt2=0
    cnt1=0
    res=""













    # for per,item in enumerate(s):
    #     if(item=='a' and lim1!=0):
    #         if(cnt1<x):
    #             cnt1+=1
    #             res+='a'
    #             lim1-=1
    #         else:
    #             cnt1=0
    #             if(lim2!=0):
    #                 res+='b'
    #                 lim2-=1
    #             else:
    #                 res+='*'
    #             res+='a'
    #             cnt1=1
    #             lim1-=1
    #     elif (item == 'b' and lim2!=0):
    #         if (cnt2 < y):
    #             cnt2 += 1
    #             res += 'b'
    #             lim2 -= 1
    #         else:
    #             cnt2 = 0
    #             if (lim1 != 0):
    #                 res += 'a'
    #                 lim1 -= 1
    #             else:
    #                 res += '*'
    #             res+='b'
    #             cnt2=1
    #             lim2-=1
    # print(res)
    #

    #     print(s)
    #     if(item=='a'):
    #         lim1+=1
    #         cnt1-=1
    #         if(lim1>x):
    #             lim1=0
    #             if(cnt2!=0):
    #                 arr.append(('b',per))
    #             else:
    #                 arr.append(('*',per))
    #     if(item=='b'):
    #         lim2+=1
    #         cnt2 -= 1
    #         if (lim2 > y):
    #             lim2=0
    #             if (cnt1 != 0):
    #                 arr.append(('a', per))
    #             else:
    #                 arr.append(('*', per))
    # for a in arr:
    #     print(a)
    #     s=s[:a[1]]+a[0]+s[a[1]:]
    #     print(a[0],a[1])
    # print(s)


    # for per,item in enumerate(s):
    #     if item=='a':
    #         cnt1+=1
    #         if(cnt1>x):
    #             cnt1=0
    #             arr.append(per)
    #     else:
    #         cnt2 += 1
    #         if (cnt2 > y):
    #             cnt2 = 0
    #             arr.append(per)