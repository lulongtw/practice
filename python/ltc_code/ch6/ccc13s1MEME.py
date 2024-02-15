num = int(input())
num+=1
done = False 

def repeatornot(numm) :
    digit = []
    while numm // 10 > 0 :
        digit.append(numm%10)
        numm = numm // 10
    digit.append(numm%10)

    if len(digit) == len(set(digit)) :
        return True
    else:
        return False

while not repeatornot(num) :
        num+=1

print(num)
""""""

x = int(input())

while True:
    x+=1
    y = str(x)
    z = set()
    for i in range(len(y)):
        z.add(y[i])
    if len(z) == len(y):
        break
print(x)

"""
x = int(input())

while True:
    x+=1
    y = str(x)
    z = []
    c = 0
    for i in range(len(y)):
        z.append(y[i])
    for i in range(len(z)):
        zz = z[:]
        zz.remove(z[i])
        for j in range(len(zz)):
            if z[i] == zz[j]:
                c+=1
    if c == 0:
        break
print(y)

"""

"""
x = int(input())

notfound = True

while notfound:
    x+=1
    y = x
    c = 0
    used = []
    while y>0:
        d = y%10
        if d in used:
            c+=1
        used.append(d)
        y = y//10
    if c == 0:
        notfound = False
print(x)


"""