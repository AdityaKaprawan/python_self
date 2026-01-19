a=int(input())
b=int(input())
c=int(input())
if(a>b):
    if(a>c):
        print(a,"is the greatest number.")
    else:
        print(c,"is the greatest number.")
elif(b>c):
    print(b,"is the greatest number.")
else:
    print(c,"is the greatest number.")