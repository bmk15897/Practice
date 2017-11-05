t=int(input())
kiwi='*'
for i in range(t):
    s=[(i,x) for i,x in enumerate(input())]
    u=[x[1] for x in s]
    x,y=[x for x in input().split()]

    alim=u.count('a')
    blim=u.count('b')

    res=''
    if(u[0]=='a'):
        res+='a'
        alim-=1
        while(blim!=0 and alim!=0):
            res+='b'
            blim-=1
            res+='a'
            alim-=1
        while alim!=0:
            res+=kiwi
            res+='a'
            alim-=1
        if blim!=0:
            res+='b'
            blim-=1
        while blim!=0:
            res+=kiwi
            res+='b'
            blim-=1
    elif (u[0] == 'b'):
        res += 'b'
        blim -= 1
        while (alim != 0 and blim != 0):
            res += 'a'
            alim -= 1
            res += 'b'
            blim -= 1
        while blim != 0:
            res += kiwi
            res += 'b'
            blim -= 1
        if alim!=0:
            res+='a'
            alim-=1
        while alim!=0:
            res+=kiwi
            res+='a'
            alim-=1
    print(res)
    # acnt=bcnt=0

    # loc=0
    # so=alim+blim-2
    # while(alim!=0 or blim!=0):
    #     if loc<so:
    #         if u[loc]=='a':
    #             if acnt==x:
    #                 if u[loc+1]=='b' and bcnt!=y and blim!=0:


