p=0
i=1
fibonachi=[1,1]

def fibo(j):
    global fibonachi
    if (j==1)or(j==2):
        return 1
    else:
        k=fibonachi[j-3]+fibonachi[j-2];fibonachi.append(k);return k
       


while p==0:
    i=i+1
    print(i)
    number=fibo(i)

    q=1
    while (number//10)!=0:
        number=number//10;q=q+1
    if q==1000:
        p=1

print(i)