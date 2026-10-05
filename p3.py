#1,2,3,2,2,5,2,2,3,3,3,7,2,2,...
def finddiv(num:int,pos:int,a:int):
    prime=True
    if num%2==0 and num>2:
        prime=False
        pos+=2
        if pos>=a:
            return 2, pos
        while num%2==0:
            num//=2
    d=3
    while d*d<=num:
        if num % d == 0:
            prime=False
            pos += d
            if pos >= a:
                return d, pos
            while num % d == 0:
                num //= d
        d+=2
    if num>1 and not prime:
        pos += num
    if prime:
        pos+=1
    return num, pos

def count(a:int):
    i=1
    j=0
    while True:
        res,j = finddiv(i,j,a)
        if j>=a:
            return res
        i+=1

def userinteraction():
    n=int(input("The sequence 1,2,3,2,2,5,2,2,3,3,3... is obtained from the sequence of \nnatural numbers by replacing composed numbers with their prime divisors, \neach divisor d being written d times.\nInput a natural number to find the n-th element of the sequence: "))
    element=int(count(n))
    print("The ",n,"-th element is: ",element, sep="")

userinteraction()