def function(i):
    a='%d'%i
    b=a[::-1]
    if a==b:
        c=bin(i)
        d=c+'b0'
        if d==(d[::-1]):
            return 1  #符合

    return 0  #不符合

sum=0

for j in range(1,1000000):
    print(j)
    if function(j)==1:
        sum=sum+j

print(sum)
