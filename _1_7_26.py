from decimal import Decimal,getcontext
getcontext().prec=10000

def function(i):
    x=Decimal(1)/Decimal(i)
    n=0
    while (x*10)<0:
        x=x*10

    p=[]
    p.append((x*10000000000)//1)

    while n==0:
        x=(x*10)%1
        if ((x*10000000000)//1) in p:
            for j in range(0,len(p)):
                if ((x*10000000000)//1)==p[j]:
                    n=len(p)-j
        else:
            p.append((x*10000000000)//1)

    return n


l=0
u=0
for k in range(2,1000):
    print(k)
    if function(k)>l:
        l=function(k)
        u=k

print(u)
