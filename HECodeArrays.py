t=int(input())
for i in range(t):
    a,b=[int(i) for i in input().split()]
    k=0
    sum=2
    jump=2*(max(a,b)+1)
    print("jump is",jump)
    while(k+1<min(a,b)):
        print(sum)
        sum+=jump
        k+=1
    if(a!=b):
        sum=sum-jump-1
    print(sum)