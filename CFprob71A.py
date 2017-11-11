t=int(input())
for i in range(t):
    str=input()
    l=str.__len__()
    if l>10:
        print(str[0]+(l-2).__str__()+str[l-1])
    else:
        print(str)