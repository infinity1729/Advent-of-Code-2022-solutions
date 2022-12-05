read=open("inputs\D2.txt")
score=0
while True:
    value=read.readline()
    if value=="":
        break
    
    opponent,me=value.split()
    opponent=ord(opponent)-64
    me=ord(me)-87
    if me==1:
        score+=(opponent-1 if opponent-1 else 3)
    elif me==2:
        score+=opponent+3
    else:
        score+=6+(opponent+1 if opponent+1!=4 else 1)
print(score)
    
    
    