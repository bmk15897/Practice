t = int(input())

def sendquery(flag):
    if flag<10**10:
        return polshort[flag]
    else:
        return polyarray[flag-10**10]

for _ in range(t):
    n = int(input())
    polyarray = []
    polshort =[]
    polquery = {}
    cnt=0
    for _ in range(n):
        temp=[int(x) for x in input().split()]
        if temp[2]==0 and temp[3]==0:
            polshort.append(temp[:2])
            cnt+=1
        else:
            polyarray.append(temp)
    # print('polshort',polshort)
    # print('polyarray',polyarray)
    q = int(input())

    flag = -1

    for _ in range(q):
        query = int(input())
        polquery[query]=-1
        tempquery=-1
        for k in polquery:
            if k < query:
                tempquery+=1
        if tempquery!=-1  and flag!=-1:
            # print('polquery',polquery)
            tempflag=polquery[max(k for k in polquery if k < query)]
            # print(query,'yes it can be simplified','flag=',tempflag)
            temp = sendquery(tempflag)
            # print('temp',temp)
            if tempflag<10**10:
                k = temp[0]+query*temp[1]
            else:
                k = temp[0]+query*temp[1]+query*query*temp[2]+query*query*query*temp[3]
            print(k)
            polquery[query] = tempflag
        else:
            temp = [query, query * query, query * query * query]
            min = 10**100
            for i in range(n-cnt):
                k =polyarray[i][0]+ polyarray[i][1] * temp[0] + polyarray[i][2] * temp[1] + polyarray[i][3] * temp[2]
                if min>k:
                    min = k
                    flag = 10**10+i
                    polquery[query]=flag
            for i in range(cnt):
                k = polshort[i][0] + polshort[i][1] * temp[0]
                if min > k:
                    min = k
                    flag = i
                    polquery[query] = flag
            # print(s[0][0]+s[0][1]*temp[0]+s[0][2]*temp[1]+s[0][3]*temp[2])
            print(min)