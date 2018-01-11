def function(i):
    if (i==0)or(i==1):
        return 1
    x=i
    for j in range(1,i):
        x=x*j

    return x

sum=0

for k in range(3,3000000):
    print(k)
    array=[]
    sum1=0
    a=k
    while (a//10)!=0:
        array.append(a%10)
        a=a//10
    array.append(a)
    for w in array:
        sum1=sum1+function(w)
    if sum1==k:
        sum=sum+k

print(sum)
