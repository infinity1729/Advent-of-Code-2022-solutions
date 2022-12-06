read=open("inputs\D6.txt")
ans=0
value=read.readline()
a=[]
i=0
while len(a)<14:
    if value[i] not in a:
        a.append(value[i])
    else:
        del a[:a.index(value[i])+1]
        a.append(value[i])
    i+=1
print(i)