ques=["who is the PM of India?","whats the current year","who is the biggest animal?","how many sem are these is in b.tech?","how many players plays in basketball?"]
ans=["modi","2026","whale","8","5"]
opt=["modi,shah,yogi,nadda","2023,2024,2025,2026","shark,whale,tiger,elephant","5,6,7,8","5,6,7,8"]
n=0
m=0
for a in ques:
    print(a)
    print(opt[n])
    answer=input()
    if(answer==ans[m]):
        print("congratulations you have won",(n+1)*1000,"RS")
        n=n+1
        m=m+1
    else:
        print("wrong answer")
        break

print("game over , congratulations , you have won",(n)*1000,"RS")


    