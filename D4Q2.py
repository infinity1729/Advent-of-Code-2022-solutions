read=open("inputs\D4.txt")
ans=0
while True:
    value=read.readline()
    if value=="":
        break
    value=value.split(',')
    x1,y1=map(int,value[0].split('-'))
    x2,y2=map(int,value[1].split('-'))
    
    if (y1<=y2 and y1>=x2) or (x1<=y2 and y1>=y2):
        ans+=1
print(ans)