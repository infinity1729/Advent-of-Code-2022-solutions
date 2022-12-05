read=open("inputs\D2.txt")
score=0
while True:
    value=read.readline()
    if value=="":
        break
    
    opponent,me=value.split()
    opponent=ord(opponent)-64
    me=ord(me)-87
    
    if me==opponent:
        score+=me+3
    elif (opponent+1)%3==me or (opponent+1==3 and me==3):
        score+=me+6
    else:
        score+=me
print(score)
    
    
    