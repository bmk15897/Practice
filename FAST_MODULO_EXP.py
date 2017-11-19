

def fast_exp(base,exp):
    res= 1
    while exp>0:
        if exp%2==1:
            res=(res*base)%10000001
        base = (base*base)%10000001
        exp//=2
    return res

print(fast_exp(1,8))