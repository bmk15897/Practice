import pandas as pd
import random as random
data=pd.read_csv("F:/dictionary.csv",delimiter=',')
k = random.randrange(0,data.A.count()-1)
sol = data.iat[k,0]
sol = sol.lower()
noOfLetters=len(sol)


print("No of letters(might have space in between)" ,noOfLetters)
print(" Meaning ::   ",data.iat[k,2])

chances = noOfLetters//2
result = ""
for i in range (noOfLetters):
    result+='*'

print(result)


while(1):
    print("Enter a letter ")
    temp = input()
    locarray=[]
    for loc,letter in enumerate(sol):
        if letter == temp:
            locarray.append(loc)
        if loc == noOfLetters-1:
            if(locarray.__len__()==0):
                print("Oops! Wrong guess!!!")
                chances -= 1
            else:
                if temp not in result:
                    for l in locarray:
                        result = result[:l]+temp+result[l+1:]
                else:
                    print("Do not enter same letter again!!!")
    if result.count('*') == 0:
        print("YOU WON!!!!!!!!!!!!!!!!! ")
        print("The Word :: ", sol)
        print("Meaning::", data.iat[k, 2])
        break
    else:
        if chances == 0:
            print("Missed by few letter!!!")
            print("Want to know which word it was  (y/n) ???")
            t = input()
            if t=='y' or t=='Y':
                print("Word was == ", sol)
            break
        else:
            print("You are left with ", chances, " chances")
            print("So far, you have ",result)