#factorial
def fact(n):
    if(n==0):
        return 1
    f = n * fact(n-1)
    return f

p=fact(4)
print(p)
#fibonacci series
def fib(n):
    if((n-1)==0):
        return 0
    if((n-1)==1):
        return 1
    f= fib(n-1) + fib(n-2)
    return f

print(fib(8))