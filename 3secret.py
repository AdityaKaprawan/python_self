#so pehele ofcourse string ko split krenge 
#then jo split krke list bne gi uss list ke hr elements ko observe krenge 
#aur code decode krke answer print kara denge
a=input("enter your string : ")
b=a.split()
#print(len(b[0]))
f=[]
for i in b:
    if(len(i)<=2):
        d=i[::-1]
        print(d,end=" ")
        f.append(d)
    else:
        g=i[3:-1]
        h=i[-1:]
        c=h+g
        print(c,end=" ")
        f.append(c)
print("")
j=" ".join(f)
print(j)

        


        
    

        