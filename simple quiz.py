f=open("questions.txt","r")
g=open("answer given.txt","w+")
h=open("answer key.txt","r")
questions=f.readlines()

for i in questions:
    if i.rstrip()=="ans":
        answer_user=input("Enter your option")
        g.write(answer_user+"\n")
    else:
        print(i)
g.seek(0)
index=0
score=0
answer_key=h.readlines()
answer_user=g.readlines()
for i in answer_key:
    if i==answer_user[index]:
        score+=1
print(score)
g.close()
