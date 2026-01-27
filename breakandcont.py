for i in range(14):
    print("5 X",i+1,"=",5*(i+1))
    if(i==9):
        break

print("now output for cont ")

for i in range(14):
    if(i==9):
        print("we skipped the iteration at i = 9")
        continue
    print("5 X",i+1,"=",5*(i+1))


     