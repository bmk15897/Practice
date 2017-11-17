t = int(input())

for _ in range(t):
    str = input()
    str = [*str]
    #cnter = 0
    n=str.__len__()
    for cnter in range(n-4,-1,-1):
        # temp="".join(str[cnter:cnter+4])
        # if temp=="?HEF" or temp=="C?EF" or temp=="CH?F" or temp=="CHE?" or temp=="??EF" or temp=="C??F" or temp=="CH??" or temp=="?HE?" or temp=="???F" or temp=="C???" or temp=="?H??" or temp=="??E?" or temp=="????" or temp=="CHEF" or temp=="?H?F" or temp=="C?E?":
        if (str[cnter]=='C' or str[cnter]=='?' ) and (str[cnter+1]=='H' or str[cnter+1]=='?' ) and (str[cnter+2]=='E' or str[cnter+2]=='?' ) and (str[cnter+3]=='F' or str[cnter+3]=='?' ) :
            str[cnter:cnter+4]='C','H','E','F'
            cnter=cnter+4
        else:
            cnter+=1

    for i in range(n):
        if str[i]=='?':
            str[i]='A'
    print("".join(str))