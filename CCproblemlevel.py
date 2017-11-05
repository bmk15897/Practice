# easy
# medium
# medium-hard
# simple
# cakewalk

t = int(input())
setU1a = ["easy","medium-hard","simple","cakewalk","hard","easy-medium"]
setU1a = set(setU1a)
setU1b = ["easy", "medium", "medium-hard", "simple", "cakewalk", "hard"]
setU1b = set(setU1b)
setU2a = ["easy", "medium",  "simple", "cakewalk", "hard", "easy-medium"]
setU2a = set(setU2a)
setU2b = ["easy", "medium", "medium-hard", "simple", "cakewalk", "easy-medium"]
setU2b = set(setU2b)
for i in range(t):
    k = int(input())
    seta=set([x for x in input().split()])
    print(seta)
    if(setU1a==seta or setU1b==seta or setU2a==seta or setU2b==seta):
        print("Yes")
    else:
        print("No")
