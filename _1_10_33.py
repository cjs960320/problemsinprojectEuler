for b in range(11,100):
    for a in range(10,b):
        if b%10==0:
            continue
        if (a%10)==(b//10):
            if ((a/b)==((a//10)/(b%10))):
                print(a,b)
        else:
            continue


