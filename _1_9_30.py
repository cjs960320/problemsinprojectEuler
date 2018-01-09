sum=0

def function(a):
    sum1=0
    while a//10!=0:
        sum1=(a%10)**5+sum1
        a=a//10

    sum1=sum1+a**5
    return sum1

for i in range(2,1000000):
    if i==function(i):
        sum=sum+i
        print(i)

print(sum)