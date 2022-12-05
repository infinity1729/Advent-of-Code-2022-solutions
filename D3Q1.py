read=open("inputs\D3.txt")
ans=0
while True:
    value=read.readline()
    if value=="":
        break
    length=len(value)
    a=set(value[:length//2])
    b=set(value[length//2:length-1])
    for char in a.intersection(b):
        if char.isupper():
            ans+=ord(char)-64+26
        else:
            ans+=ord(char)-96
print(ans)