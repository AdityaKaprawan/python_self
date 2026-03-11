#so pehele ofcourse string ko split krenge 
#then jo split krke list bne gi uss list ke hr elements ko observe krenge 
#aur code decode krke answer print kara denge
a=input("enter your string : ")
b=a.split()
#print(len(b[0]))
for i in b:
    if(len(i)<=2):
        