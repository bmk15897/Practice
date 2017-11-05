import numpy as np
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    cnt =n
    for i,e in enumerate(arr):

        offset=1
        j=i
        while(j+offset!=arr.__len__()):
            s = sum(arr[j:j+offset+1])
            p = np.prod(arr[j:j+offset+1])
            if s == p:
                cnt+=1
            offset+=1
    print(cnt)