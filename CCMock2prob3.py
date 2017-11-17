t = int(input())
for _ in range(t):
    p = int(input())
    if p<4096:
        b = bin(p)
        p = b[2:].count('1')
        print(p)
    else:
        temp = p//2048-1
        temp1 = p - temp*2048
        tempb = bin(temp1)
        print(tempb[2:].count('1')+temp)