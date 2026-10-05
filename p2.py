def finddivisors(a:int):
    p=1
    d=2
    while d*d<a:
        if a%d==0:
            p*=d
            p*=int(a/d)
        d+=1
    if d*d==a:
        p*=d
    return p
def userinteraction():
    n=int(input("Input a natural number to find the product of all of its proper divisors: "))
    product=finddivisors(n)
    if product==1:
        print(n,"has no proper divisor")
    else:
        print("The product of all proper divisors of",n,"is",product)

userinteraction()