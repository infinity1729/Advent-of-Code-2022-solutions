read=open("inputs\D3.txt")
ans=0
while True:
    value1=read.readline()
    if value1=="":
        break
    value2=set(read.readline())
    value3=set(read.readline())
    
    for char in value2.intersection(value3).intersection(value1)-{'\n'}:
        if char.isupper():
            ans+=ord(char)-64+26
        else:
            ans+=ord(char)-96
print(ans)