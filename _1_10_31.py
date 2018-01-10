n=0
sum=200

for a in range(0,2):
    if a==1:
        n=n+1
        continue
    for b in range(0,3):
        if b==2:
            n=n+1
            continue
        for c in range(0,5):
            if (200-100*b-c*50)<0:
                continue
            for d in range(0,11):
                if (200-100*b-50*c-20*d)<0:
                    continue
                for e in range(0,21):
                    if (200-100*b-50*c-20*d-10*e)<0:
                        continue
                    for f in range(0,41):
                        if (200-100*b-50*c-20*d-10*e-5*f)<0:
                            continue
                        for g in range(0,101):
                            now=sum-(200*a+100*b+50*c+20*d+10*e+5*f+2*g)
                            if now>=0:
                                n=n+1

print(n)
