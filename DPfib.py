'''

def fibo(num):
    if(num<=2):
        return 1
    else:
        return fibo(num-1)+fibo(num-1)

print(fibo(3))

#The above code is bad, Exponential time



#below code uses DP (memoization)


memo={}
def fiboDp(num):
    if num in memo:
        return memo[num]
    elif num <=2:
        return 1
    else:
        f = fiboDp(num-1)+fiboDp(num-2)
        memo[num]=f
        return f

print(fiboDp(3))
print(fiboDp(4))
print(fiboDp(5))

The above technique is very efficient but there's one more technique which is even more efficient





The below code uses Bottom-Up DP algorithm




'''

memo={}
memo[1]=0
memo[2]=1
def fiboBdp(num):
    for k in range(1,num+1):
        if k<=2:
            f= 1
        else:
            memo[k]=memo[k-1]+memo[k-2]
    return memo[k]

print(fiboBdp(4))
print(fiboBdp(5))