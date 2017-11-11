t = int(input())
for _ in range(t):
    N,P,Q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    x=0
    L = [0 for _ in range(Q)]
    R = [0 for _ in range(Q)]

    for i in range(Q):
        print(i)
        if i%64==0:
            L[i] = ( B[i//64] + x ) % N
            R[i] = ( B[i//64 + 1] + x ) % N
        else:
            L[i] = (L[i - 1] + x) % N
            R[i] = (R[i - 1] + x) % N
        if i %64 in range(B.__len__()-1):
            if 0 not in arr[L[i]:(R[i]+1)%P]:
                sum=1
                if L[i]%P>R[i]%P:
                    L[i],R[i]=R[i]%P,L[i]
                for j in range(L[i]%P,(R[i]+1)%P):
                    sum*=arr[j]
            else:
                sum=0
            x = (sum + 1) % P
            print(L[i],R[i],x)


            # print(L[i],R[i],x)
    print(x)