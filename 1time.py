import time
t = time.strftime("%H:%M:%S")
print(t)
T=int(time.strftime("%H"))
if(T>12):
    print("good evening")
elif(T<12):
    print("good morning")
