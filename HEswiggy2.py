n,m = map(int,input().split())
arr=[[0 for x in range(m)] for y in range(n)]
for x in range (0,n):
    for y in range (0,m):
        arr[x][y]=input()
def fun(x,y):
    if arr[x][y]==2:
        if x==0:
            if y==0:
                if(arr[x+1][y]==1):
                    arr[x+1][y]=2
                fun(x+1,y)
                if(arr[x][y+1]==1):
                    arr[x][y+1]=2
                fun(x,y+1)
            else:

        else:

for x in range (0,n):
    for y in range (0,m):
        fun(x,y)