# def power(base, exponent):
#     return base ** exponent
def power(base, exponent):
    result=1
    for _ in range(exponent):
        result *= base
    return result
a=2
b=10
print(power(a,b))