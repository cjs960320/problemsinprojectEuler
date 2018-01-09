array=[]

for a in range(2,101):
    for b in range(2,101):
        c=a**b
        if c in array:
            print("zaile")
        else:
            array.append(c)

print(len(array))