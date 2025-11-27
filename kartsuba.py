def kartsuba(x,y):
    if x<10 and y<10:
        return x*y
    #len of the max number
    m=max(len(str(x)),len(str(y)))
    if m%2!=0:
        m-=1
    a,b=divmod(x,10**int(m//2))
    c,d=divmod(y,10**int(m//2))
    ac=kartsuba(a,c)
    bd=kartsuba(b,d)
    abcd=kartsuba((a+b),(c+d))-ac-bd    
    return ((ac*(10**m))+bd+(abcd*(10**int(m//2))))

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(kartsuba(x,y))