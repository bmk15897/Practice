str = input()
str = str.lower()
ans=""
for i in range(str.__len__()):
    if str[i] not in ('a','e','i','o','u','y'):
        ans+='.'+str[i]
print(ans)