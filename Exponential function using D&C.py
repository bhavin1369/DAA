def power(base,exp):
    if(exp<0):
        base=1/base
        exp=-1*exp
    ans=1
    for i in range(exp):
        ans=ans*base
    return ans

def power_recursive(base,exp):
    if(exp == 0):
        return 1
    return base*power_recursive(base,exp-1)

def Power(x, n):
    if n == 0:
        return 1
    temp = Power(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp
    
# print(power(2,5))
# print(power_recursive(2,5))
print(Power(2, 5))  # Output: 32