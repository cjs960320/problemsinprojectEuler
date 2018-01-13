bignumber=0

#4
for integer in range(5000,10000):
    digit=[]
    digit.append(integer//1000)
    digit.append((integer%1000)//100)
    digit.append((integer%100)//10)
    digit.append(integer%10)
    integer1=integer*2
    digit.append(integer1//10000)
    digit.append((integer1%10000)//1000)
    digit.append((integer1%1000)//100)
    digit.append((integer1%100)//10)
    digit.append(integer1%10)
    bool=1
    for i in range(1,10):
        if i in digit:
            bool=1
        else:
            bool=0
            break

    if (bool==1)and((integer*100000+integer1)>bignumber):
        bignumber=integer*100000+integer1

#3
for integer in range(100,333):
    digit=[]
    digit.append(integer//100)
    digit.append((integer%100)//10)
    digit.append(integer%10)
    integer1=integer*2
    digit.append(integer1//100)
    digit.append((integer1%100)//10)
    digit.append(integer1%10)
    integer2=integer*3
    digit.append(integer2//100)
    digit.append((integer2%100)//10)
    digit.append(integer2%10)
    bool=1
    for i in range(1,10):
        if i in digit:
            bool=1
        else:
            bool=0
            break

    if (bool==1)and((integer*1000000+integer1*1000+integer2)>bignumber):
        bignumber=integer*1000000+integer1*1000+integer2

#2
for integer in range(25,33):
    digit=[]
    digit.append(integer//10)
    digit.append(integer%10)
    integer1=integer*2
    digit.append(integer1//10)
    digit.append(integer1%10)
    integer2=integer*3
    digit.append(integer2//10)
    digit.append(integer2%10)
    integer3=integer*4
    digit.append(integer3//100)
    digit.append(integer3%10)
    digit.append((integer3%100)//10)
    bool=1
    for i in range(1,10):
        if i in digit:
            bool=1
        else:
            bool=0
            break

    if (bool==1)and((integer*10000000+integer1*100000+integer2*1000+integer3)>bignumber):
        bignumber=integer*10000000+integer1*100000+integer2*1000+integer3

#1
number=918273645
if number>bignumber:
    bignumber=number

print(bignumber)
