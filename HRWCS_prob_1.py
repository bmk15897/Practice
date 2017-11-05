#!/bin/python3

import sys

def productOfPages(a, b, c, d, p, q):
    arr=[a,b,c,d]
    #if(arr.count(p)==1 and arr.count(q)==1):
    arr.remove(p)
    arr.remove(q)
    return arr[0]*arr[1]
    # else:
    #     if(arr.count(p)==1):
    #         arr.remove(p)
    #         arr.remove(q)
    #         print(arr)
    #         return arr[0]*q
    #     else:
    #         arr.remove(p)
    #         arr.remove(q)
    #         print(arr)
    #         return arr[0]*p


    # Return the product of the page counts of the missing books

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a, b, c, d = input().strip().split(' ')
        a, b, c, d = [int(a), int(b), int(c), int(d)]
        p, q = input().strip().split(' ')
        p, q = [int(p), int(q)]
        answer = productOfPages(a, b, c, d, p, q)
        print(answer)