t = int(input())
def checklist(l1,l2):
    flag=0
    for i in range(3):
        if l1[i]!=l2[i]:
            flag=1
    if flag==0:
        return True
    else:
        return False

for i in range(t):
    arr = [[] for y in range(3)]
    for j in range(3):
        temp = [int(x) for x in input().split()]
        for k in range(3):
            arr[j].append(temp[k])
    if arr[1]==arr[2] or arr[2]==arr[0] or arr[0]==arr[1]:
        print('no')
    else:
        lowest=[]
        arrnew=arr.copy()
        for k in range(3):
            for j in range(3):
                temp=[arrnew[x][j] for x in range(arrnew.__len__())]
                temp.sort()
                for i in range(arrnew.__len__()):
                    arrnew[i][j]-=temp[0]
            for j in range(arrnew.__len__()-1):
                if checklist(arrnew[j],[0,0,0]):
                    arrnew.remove(arrnew[j])
            if checklist(arrnew[arrnew.__len__()-1],[0,0,0]):
                arrnew.remove(arrnew[arrnew.__len__()-1])

        if arrnew.__len__()==0:
            print('yes')
        else:
            print('no')