def equib(a):
    sum=0
    leftSum=0
    for i in range(0,len(a)):
        sum = sum + a[i]
    for i in range(0,len(a)):
        sum = sum - a[i]
        if(sum == leftSum):
            return i
        leftSum = leftSum + a[i]
    return -1
        
a = [0,1,2,3,1,1,1];
print(equib(a))
