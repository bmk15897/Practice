#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     temp=n
#     while (n**0.5).is_integer()==False:
#         n-=1
#     temp-=n
#     ans = temp//n**0.5
#     print(ans.__int__())


t = int(input())
for _ in range(t):
    #factors = []
    n = int(input())
    i = int(n**0.5)
    while(n%i!=0):
        i-=1
    print(int(n/i-i))
