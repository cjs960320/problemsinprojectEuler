def function(i):
    for j in range(2,i):
        if i%j==0:
            return 0  #非质数

    return 1    #质数

sum=4
array=[1,3,7,9]
#2位数
for a in array:
    for b in array:
        if (function(10*a+b)==1)and(function(10*b+a)==1):
            sum=sum+1
print("2 is over")
#3
for a in array:
    for b in array:
        for c in array:
            if (function(100*a+10*b+c)==1)and(function(100*c+10*a+b)==1)and(function(100*b+10*c+a)==1):
                sum=sum+1
print("3 is over")
#4
for a in array:
    for b in array:
        for c in array:
            for d in array:
                if (function(1000*a+100*b+10*c+d)==1)and(function(1000*d+100*a+10*b+c)==1)and(function(1000*c+100*d+10*a+b)==1)and(function(1000*b+100*c+10*d+a)==1):
                    sum=sum+1
print("4 is over")
#5
for a in array:
    for b in array:
        for c in array:
            for d in array:
                for e in array:
                    if (function(10000*a+1000*b+100*c+10*d+e)==1)and(function(10000*e+1000*a+100*b+10*c+d)==1)and(function(10000*d+1000*e+100*a+10*b+c)==1)and(function(10000*c+1000*d+100*e+10*a+b)==1)and(function(10000*b+1000*c+100*d+10*e+a)==1):
                        sum=sum+1
print("5 is over")
#6
for a in array:
    for b in array:
        for c in array:
            for d in array:
                for e in array:
                    for f in array:
                        if (function(100000*a+10000*b+1000*c+100*d+10*e+f)==1)and(function(100000*f+10000*a+1000*b+100*c+10*d+e)==1)and(function(100000*e+10000*f+1000*a+100*b+10*c+d)==1)and(function(100000*d+10000*e+1000*f+100*a+10*b+c)==1)and(function(100000*c+10000*d+1000*e+100*f+10*a+b)==1)and(function(100000*b+10000*c+1000*d+100*e+10*f+a)==1):
                            sum=sum+1

print(sum)
