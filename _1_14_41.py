def function(i):
    for j in range(2,i):
        if i%j==0:
            return 0

    return 1

#n=7
bignumber=0
for a in [1,3,7]:
    for b in range(1,8):
        if b==a:
            continue
        for c in range(1,8):
            if (c==a)or(c==b):
                continue
            for d in range(1,8):
                if (d==a)or(d==b)or(d==c):
                    continue
                for e in range(1,8):
                    if (e==a)or(e==b)or(e==c)or(e==d):
                        continue
                    for f in range(1,8):
                        if (f==a)or(f==b)or(f==c)or(f==d)or(f==e):
                            continue
                        for g in range(1,8):
                            if (g==a)or(g==b)or(g==c)or(g==d)or(g==e)or(g==f):
                                continue
                            number=1000000*g+100000*f+10000*e+1000*d+100*c+10*b+a
                            if function(number)==1:
                                print(number)
                                if number>bignumber:
                                    bignumber=number

print("max",bignumber)
                        


