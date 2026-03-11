#use try: keyword for an expected error or errors in one or multiple line of code 
#use it if you want some other important lines of code to run but the error from only one error expected line is stoping it to run .
a=(input("enter a number of the table : "))
print(f"multiplication table of {a} is given below: ")

try:
    for i in range(1,11):
        print(f"{int(a)}X{i} = ",int(a)*i )
except Exception as e:
    print(e)
#except:
#   print("invalid input")

print("this line is improtant so it must run at any cost")
print("these lines of code are important.")
#IMPORTANT - yha pr hum int koinput ke time define nhi kr rhe hai taaki hum bina error kestring input kr paae aur baad mai multiply krte time for loop ke andr a ko int define kr reh hai kyuki ko "try:" ke andr hai 
#agr a ko start se hi int define krna hai toh shyd usse bhi "try:" ke andr rakhna hoga 

try:
    b=int(input("enter something :"))
    d = b*2
    print(d)
except:
    print("invalide input")
print("hahaha")
#ek specific tarha ke error ko bhi specify kr skte hai "expect : Value error ,index error , ect ect " se , aur different different tyoe ke errors ke liye different different statements print kara skte hai 

#"finally" humrsha execute hoga even function end hone ke baad bhi , jese agr humne khud se function bhi define kra hoga tb bhi 
#https://youtu.be/4LKo6dlku7M?si=7oQ5ZPgZHhbahDL3 - error handlining
#https://youtu.be/r_iuC-IDpPM?si=CE1os2b8m6P76nuT - finally 
