t = int(input())

for _ in range(t):
    str=input()
    size = str.__len__()
    sum=0
    for i in range(size//2):
        if str[size//2 - i -1]!=str[size-size//2 + i]:
            k=(min(str[size//2 - i -1],str[size-size//2 + i]))
            sum+=(ord(k)-96)
    print(sum)