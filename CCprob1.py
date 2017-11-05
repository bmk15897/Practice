
def fun():
    return m
t=int(input())
for i in range(t):
    arr=list(input())
    arrsize=arr.__len__()
    cnt = 0
    for j,item in enumerate(arr):
        size = 2
        while(j+size!=arrsize+1):
            if arr[j]==arr[j+size-1]:
                if size==2:
                    cnt+=1
                else:
                    str=''.join(arr[j+1:j+size-1])
                    if str==str[::-1]:
                        cnt+=1
            size+=1
    print(cnt)