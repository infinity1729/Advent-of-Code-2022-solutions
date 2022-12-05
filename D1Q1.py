read=open("inputs\D1.txt")
maxSum=0
presentSum=0
while True:
    value=read.readline()
    if value=="":
        break
    elif value=="\n":
        maxSum=max(maxSum,presentSum)
        presentSum=0
    else:
        presentSum+=int(value)
    
print(maxSum)