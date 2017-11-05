'''
10 5
1 7 8 9 3 2 4 10 6 5
1 5
10 15
1 15
0 5
15 20
'''

n,q=[int(x) for x in input().split()]
mountains=[int(x) for x in input().split()]
temp=mountains
temp.sort()

# lr=[[-1 for y in range(100001)] for x in range(100001)]


    # for k in mountains:
    #     if k in range(s,h+1):
    #         cnt+=1
    # print(cnt)

for i in range(q):
    s,h=[int(x) for x in input().split()]
    t=0
    u=0
    for index, elem in enumerate(temp):
        if elem >= s:
            t=index
    # for index, elem in enumerate (temp.reverse()):
        if temp[temp.__len__()-index-1] <= h:
            u=temp.__len__()-index-1
        print(t,u)