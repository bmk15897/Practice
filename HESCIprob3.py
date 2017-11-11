# str=input()
# size=10**5
#
# dict = {}
# for s in str:
#     if s in dict:
#         dict[s]+=1
#     else:
#         dict[s]=1
#
# import operator
# sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
# sorted_dict.reverse()
#
# keyboard = [[0 for x in range(21)] for y in range(3)]
#
# j=0
# k=0
# cnt = 0
# flag=0
# for i in sorted_dict:
#     print(j,k,i[0])
#     # if flag==4:
#     #     if i == ' ':
#     #         keyboard[k][j] = '.'
#     #     else:
#     #         keyboard[k][j] = i[0]
#     #     break
#     if flag==0:
#         if i == ' ':
#             keyboard[k][j] = '.'
#         else:
#             keyboard[k][j] = i[0]
#         j+=1
#         if j==21:
#             j-=1
#             flag=1
#             k+=1
#     elif flag==1:
#         if i == ' ':
#             keyboard[k][j] = '.'
#         else:
#             keyboard[k][j] = i[0]
#         j-=1
#         if j==-1:
#             j+=1
#             flag=2
#             k-=2
#     else:
#         if i == ' ':
#             keyboard[k][j] = '.'
#         else:
#             keyboard[k][j] = i[0]
#         j+=1
#         # if j==21:
#         #     flag=4
#         #     j=1
#         #     k=0
#
# import string
#
# tank =''
# tank+=string.ascii_lowercase
# tank+=string.ascii_uppercase
# tank+=string.digits
# tank+=' '
#
# for i in tank:
#     if i not in dict:
#         # if flag == 4:
#         #     if i ==' ':
#         #         keyboard[k][j]='.'
#         #     else:
#         #         keyboard[k][j] = i
#         #     break
#         if flag == 0:
#             if i ==' ':
#                 keyboard[k][j]='.'
#             else:
#                 keyboard[k][j] = i
#             j += 1
#             if j == 21:
#                 j -= 1
#                 flag = 1
#                 k += 1
#         elif flag == 1:
#             if i ==' ':
#                 keyboard[k][j]='.'
#             else:
#                 keyboard[k][j] = i
#             j -= 1
#             if j == -1:
#                 j += 1
#                 flag = 2
#                 k -= 2
#         else:
#             if i ==' ':
#                 keyboard[k][j]='.'
#             else:
#                 keyboard[k][j] = i
#             j += 1
#             # if j == 21:
#             #     flag = 4
#             #     j = 0
#             #     k = 1
#
# print(''.join(keyboard[0]))
# print(''.join(keyboard[1]))
# print(''.join(keyboard[2]))

str=input()
size=10**5

dict = {}
for s in str:
    if s in dict:
        dict[s]+=1
    else:
        dict[s]=1

relation = {}

for i in range(str.__len__()):
    if relation[(str[i],str[i+1])] not in relation:
        relation[(str[i],str[i+1])]=1
    else:
        relation[(str[i],str[i+1])]+=1

import operator
sort_rel = sorted(dict.items(), key=operator.itemgetter(1))
sort_rel.reverse()


sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
sorted_dict.reverse()

keyboard = [[0 for x in range(21)] for y in range(3)]

j=1
k=1
cnt = 0
flag=0
for i in sort_rel:
    if flag==4:
        if ord(i[0])==32:
            keyboard[k][j] = '.'
        else:
            keyboard[k][j] = i[0]
        break
    if flag==0:
        if ord(i[0])==32:
            keyboard[k][j] = '.'
        else:
            keyboard[k][j] = i[0]
        j+=1
        if j==21:
            j-=1
            flag=1
            k+=1
    elif flag==1:
        if ord(i[0])==32:
            keyboard[k][j] = '.'
        else:
            keyboard[k][j] = i[0]
        j-=1
        if j==-1:
            j+=1
            flag=2
            k-=2
    else:
        if ord(i[0])==32:
            keyboard[k][j] = '.'
        else:
            keyboard[k][j] = i[0]
        j+=1
        if j==21:
            flag=4
            j=1
            k=0

import string

tank =''
tank+=string.ascii_lowercase
tank+=string.ascii_uppercase
tank+=string.digits
tank+=' '

for i in tank:
    if i not in dict:
        if flag == 4:
            if i ==' ':
                keyboard[k][j]='.'
            else:
                keyboard[k][j] = i
            break
        if flag == 0:
            if i ==' ':
                keyboard[k][j]='.'
            else:
                keyboard[k][j] = i
            j += 1
            if j == 21:
                j -= 1
                flag = 1
                k += 1
        elif flag == 1:
            if i ==' ':
                keyboard[k][j]='.'
            else:
                keyboard[k][j] = i
            j -= 1
            if j == -1:
                j += 1
                flag = 2
                k -= 2
        else:
            if i ==' ':
                keyboard[k][j]='.'
            else:
                keyboard[k][j] = i
            j += 1
            if j == 21:
                flag = 4
                j = 0
                k = 1

print(''.join(keyboard[0]))
print(''.join(keyboard[1]))
print(''.join(keyboard[2]))