t=0
for p in range(3,1001):
    print(p)
    array=[]
    for a in range(1,p-1):
        if a in array:
            continue
        for b in range(1,p-a):
            c=p-a-b
            if ((a*a+b*b)==(c*c))or((c*c+b*b)==(a*a))or((a*a+c*c)==(b*b)):
                array.append(a)
                array.append(b)
                array.append(c)
    if (len(array)/3)>t:
        print("p",p)
        t=len(array)/3


