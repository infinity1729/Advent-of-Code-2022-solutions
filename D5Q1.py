read=open("inputs\D5.txt")
d={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
for _ in range(8):
    value=read.readline()
    value=[value[i+1] for i in range(0,len(value),4)]
    for i in range(1,10):
        if value[i-1]!=" ":
            d[i].insert(0,value[i-1])
read.readline()
read.readline()
while True:
    value=read.readline()
    if value=="":
        break
    value=value.split(" ")
    num=min(int(value[1]),len(d[int(value[3])]))
    for _ in range(num):
        d[int(value[5])].append(d[int(value[3])].pop())
ans=""
for i in d:
    if d[i]!=[]:
        ans+=d[i][-1]
print(ans)
