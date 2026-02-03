movies = []
a=input("enter first movie")
movies.append(a)
b=input("enter second movie")
movies.append(b)
c= input("enter third movie")
movies.append(c)
print(movies)
# yaha prr append isi liye use hu rha hai kyuki list pehele empty hai tph uspe koi elements bhi nhi hai
movies[2]=input("enter for replacement: ")
print(movies)
#l.sort() se numbers assending order mai lag jaenge 
#l.sort(reverse=True) is desending order mai ho jaega 
#l.reverse() original index ko reverse kr dega
movies.reverse()
print(movies)


print(movies.index("dhurandar"))
print(movies.count("push"))

#m = l.copy() se list ki copy bn jaegi , agr bna copy banae , ie m = l kr diya toh m mai koi change l mai bhi hoga 
#l.insert(2,244) ye 2nd index mai 244 rakh dega aur baaki elements ko shift kr dega 
#if we have l as a list and if we make a new list for eg m , and command l.extend(m) , toh m wali puuri list l ke end mai lag jaegi 
#ye extend wali cheej bina extend ke bhi kr skte hai by putting k = l + m 

      