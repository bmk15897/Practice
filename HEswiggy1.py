num = input()

rev = [int(x) for x in num.split()]
res=[]
num = int(''.join(map(str,rev[:1])))
print(num)
for i in range(1,rev.__len__()):
    if int(''.join(map(str,rev[:i])))>7 :
        res.append('7')
print(res)
