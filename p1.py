#goldbach hypothesis only applies to even numbers so the problem's text isn't correct
def checkifprime(a:int):
    if a<2:
        return False
    if a==2:
        return True
    if a%2==0:
        return False
    d=3
    while d*d<=a:
        if a%d==0:
            return False
        d+=2
    return True

def findprimes(n:int):
    if checkifprime(n-2):
        return 2
    for i in range(3,int(n/2)+1,2):
        if checkifprime(i) and checkifprime(n-i):
            return i
    return 0
def userinteraction():
    print("Enter an even natural number greater than 2 or the greater member of a pair of twin primes:\n")
    aux=int(input())
    result=findprimes(aux)
    if result!=0:
        print("\nThe number",aux,"can be written as the sum of primes",result, "and", aux - result)
    else:
        print("\n",aux,"Is not an even natural number greater than 2 or the greater member of a pair of twin primes, \nso it cannot be written as the sum of 2 prime numbers.")

userinteraction()