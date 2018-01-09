def function(i):
    if (i==2):
        return 1
    else:
        if (i==0)or(i==1):
            return 0
        for j in range(2,i):
            if i%j==0:
                return 0
    return 1

sum=0
nn=0
for a in range(-999,1000):
    print(a)
    for b in range(2,1000):
    #    print(b)
        if (b%2==0)or(b<(-a-1))or(b<(-4-2*a)):
            continue
        p=0
        s=0
        while p==0:

            
      #      print(s)
            k=s*s+s*a+b
            if k<0:
                break
            if function(k)==0:
                p=1
                if s>nn:
                    nn=s
                    sum=a*b
            else:
                s=s+1
print(nn)
print(sum)
