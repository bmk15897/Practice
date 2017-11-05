#!/bin/python3

import sys

if __name__ == "__main__":
    n, s = input().strip().split(' ')
    n, s = [int(n), int(s)]
    arr = [i for i in range(0,n)]
    cnt = 0
    si = arr.__len__()
    for a0 in range(s):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        l-=cnt
        r-=cnt
        temp = sum(arr[l:r+1])
        lflag=rflag=-1
        if(l>0 and arr[l-1]!=-1):
            lflag=arr[l-1]
        else:
            while(l>0):
                if(arr[l-1]!=-1):
                    lflag = arr[l - 1]
                    break
                l-=1
        if(r!=si-1 and r>0 and arr[r+1]!=-1):
            rflag=arr[r+1]
        else:
            while(r!=si-1 and r>0):
                if(arr[r+1]!=-1):
                    rflag = arr[r + 1]
                    break
                r+=1
        # for i,e in enumerate(arr):
        #     print(e)
        #     if e in range(l,r+1):
        #         arr.remove(e)
        for i,e in enumerate(arr[l:r+1]):
            arr.remove(e)
        if(lflag!=-1):
            temp+=lflag
            arr.remove(lflag)
        if (rflag != -1):
            temp += rflag
            arr.remove(rflag)
        cnt=si-arr.__len__()
        print(temp)
        # Write Your Code Here