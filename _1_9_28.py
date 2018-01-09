sum=1

for i in range(1,501):
    x=2*i
    a=x*(x-1)+1
    b=x*x+1
    c=x*(x+1)+1
    d=x*(x+2)+1
    sum=a+b+c+d+sum

print(sum)
