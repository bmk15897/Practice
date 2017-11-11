t = int(input())
for i in range(t):
    arr = [[] for y in range(3)]
    for j in range(3):
        temp = [int(x) for x in input().split()]
        for k in range(3):
            arr[j].append(temp[k])
    if arr[1]==arr[2] or arr[2]==arr[0] or arr[0]==arr[1]:
        print('no')
    else:
        max=[]
        for j in range(3):
            temp=[arr[0][j],arr[1][j],arr[2][j]]
            max.append(max(temp))
    # arrsort=[[] for y in range(3)]

    # maxele=[]
    # for j in range(3):
    #     temp=[arr[0][j],arr[1][j],arr[2][j]]
        # for k in range(3):
        #     arrsort[j].append(temp[k])
        # arrsort[j].sort(reverse=True)
        # maxA=max(temp)
        # maxele[]=temp.index(maxA)


    #print(arr,arrsort)




    # arr1=[int(x) for x in input().split()]
    # arr2=[int(x) for x in input().split()]
    # arr3=[int(x) for x in input().split()]






    # maxele=[0,0,0]
    # maxpos=[0,0,0]
    # for i in range(3):
    #
    #     maxele[i]=max(arr1[i],arr2[i],arr3[i])
    #     maxpos[i]=[arr1[i],arr2[i],arr3[i]].index(maxele[i])







