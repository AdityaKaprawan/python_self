string="Hi My name is Aditya Kaprawan"
Cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vow="aeiouAEIOU"

capcount=0
vowcount=0

for a in string:
    if a in Cap:  #(comment) or use if a.isupper(): capcount = capcount+1
        capcount=capcount+1
    if a in vow:
        vowcount=vowcount+1
print("No. of capital letters is ",capcount)
print("No. of vowels is ",vowcount)

str = string.split()
for b in str:
    print(b)
