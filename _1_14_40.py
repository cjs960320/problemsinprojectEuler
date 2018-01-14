t=0
n=0
array=[1,10,100,1000,10000,100000,1000000]
while t<1000000:
    n=n+1
    print(n)
    m=n
    while m//10!=0:
        m=m//10
        t=t+1
    t=t+1
    print(t)

    
