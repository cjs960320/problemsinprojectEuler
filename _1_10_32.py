product=[]
#2*3=4
for i in range(12,100):
    for j in range(123,1000):
        if i*j>=10000:
            continue
        else:
            digit=[]
            digit.append(i//10)
            digit.append(i%10)
            digit.append(j//100)
            digit.append((j%100)//10)
            digit.append((j%100)%10)
            digit.append((i*j)//1000)
            digit.append(((i*j)%1000)//100)
            digit.append((((i*j)%1000)%100)//10)
            digit.append((i*j)%10)
            bool=0
            for n in range(1,10):
                if n not in digit:
                    bool=1

            if (bool==0)and(i*j not in product):
                product.append(i*j)
#1*4=4
for i in range(1,10):
    for j in range(1234,9877):
        if i*j>=10000:
            continue
        else:
            digit=[]
            digit.append(i)
            digit.append(j//1000)
            digit.append((j%1000)//100)
            digit.append(((j%1000)%100)//10)
            digit.append(j%10)
            digit.append((i*j)//1000)
            digit.append(((i*j)%1000)//100)
            digit.append((((i*j)%1000)%100)//10)
            digit.append((i*j)%10)
            bool=0
            for n in range(1,10):
                if n not in digit:
                    bool=1

            if (bool==0)and(i*j not in product):
                product.append(i*j)
sum=0
for m in product:
    print(m)
    sum=sum+m

print(sum)
