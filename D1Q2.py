read=open("inputs\D1.txt")
maxSum=[0,0,0]
presentSum=0
while True:
    value=read.readline()
    if value=="":
        break
    elif value=="\n":
        if presentSum>maxSum[0]:
            maxSum[2]=maxSum[1]
            maxSum[1]=maxSum[0]
            maxSum[0]=presentSum
        elif presentSum>maxSum[1]:
            maxSum[2]=maxSum[1]
            maxSum[1]=presentSum
        elif presentSum>maxSum[2]:
            maxSum[2]=presentSum
        presentSum=0
    else:
        presentSum+=int(value)
    
print(sum(maxSum))