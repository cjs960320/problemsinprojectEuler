#首位只能为2,3,5,7    中间位只能为1，3,7,9  末位只能为3,7
def function(i):
    if i==2:
        return 1
    if i==1:
        return 0
    for j in range(2,i):
        if i%j==0:
            return 0     #非质数
    return 1   #质数

array=[]
array1=[2,3,5,7]
array2=[1,3,7,9]
array3=[3,7]
#2
for a in array1:
    for b in array3:
        if (function(a)+function(b)+function(10*a+b))==3:
            array.append(10*a+b)

#3
for a in array1:
    for b in array2:
        for c in array3:
            if (function(a)+function(c)+function(10*a+b)+function(10*b+c)+function(100*a+10*b+c))==5:
                array.append(100*a+10*b+c)

#4
for a in array1:
    for b in array2:
        for c in array2:
            for d in array3:
                if (function(a)+function(d)+function(10*a+b)+function(10*c+d)+function(100*a+10*b+c)+function(100*b+10*c+d)+function(1000*a+100*b+10*c+d))==7:
                    array.append(1000*a+100*b+10*c+d)
print("4 is over")
#5
for a in array1:
    for b in array2:
        for c in array2:
            for d in array2:
                for e in array3:
                    if (function(a)+function(e)+function(10*a+b)+function(10*d+e)+function(100*a+10*b+c)+function(100*c+10*d+e)+function(1000*a+100*b+10*c+d)+function(1000*b+100*c+10*d+e)+function(10000*a+1000*b+100*c+10*d+e))==9:
                        array.append(10000*a+1000*b+100*c+10*d+e)
print("5 is over")
#6
for a in array1:
    for b in array2:
        for c in array2:
            for d in array2:
                for e in array2:
                    for f in array3:
                        if (function(a)+function(f)+function(10*a+b)+function(10*e+f)+function(100*a+10*b+c)+function(100*d+10*e+f)+function(1000*a+100*b+10*c+d)+function(1000*c+100*d+10*e+f)+function(10000*a+1000*b+100*c+10*d+e)+function(10000*b+1000*c+100*d+10*e+f)+function(100000*a+10000*b+1000*c+100*d+10*e+f))==11:
                            array.append(100000*a+10000*b+1000*c+100*d+10*e+f)
sum=0
for i in array:
    sum=sum+i
    print(i)

print("sum",sum)