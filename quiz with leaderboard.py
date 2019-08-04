from matplotlib import pyplot as plt 
import numpy as np

f=open("questions.txt","r")
g=open("answer given.txt","w+")
h=open("answer key.txt","r")
p=open("details.txt","a+")
name=input("Enter your name: ")

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
    if i.rstrip() == answer_user[index].rstrip():
        score+=1
    index+=1
print("you got",score,"out of",len(answer_key),"correct")
string="Name : "+name+"\n"+"Score : "+str(score)+"/"+str(len(answer_key))+"\n"
p.write(string)
p.seek(0)
details=p.readlines()
users=[]
for i in details:
    a,b=i.rstrip().split(" : ")
    users.append(b)
print(users)
d={}
for i in range(0,len(users),2):
    score_user=users[i+1]
    scored,total =score_user.split("/")
    d[users[i]]=int(scored)
total=int(total)
total_scored=total
leader={}
for i in range(total):
    for j in d:
        if d[j]==total_scored:
            leader[j]=d[j]
    total_scored-=1

print(d)
print(leader)
names=list(leader.keys())
scores=list(leader.values())
print("-"*5,"LEADERBOARD","-"*5)
print("SNO","NAMES","SCORE")
for i in range(len(names)):
    index=str(i+1)
    print(index.center(2),names[i].center(8),scores[i])
p.close()
g.close()
y_pos = np.arange(len(names))

plt.bar(y_pos,scores) 
plt.xticks(y_pos, names,rotation=45)
plt.subplots_adjust(bottom=0.4, top=0.99)

 
plt.show() 
