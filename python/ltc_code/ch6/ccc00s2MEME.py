n = int(input())
x = []

for i in range(n):
    x.append(int(input()))

def splt(xx,indx,prcnt):
    a = xx[indx]*prcnt//100
    b = xx[indx] - a
    xx[indx] = a
    xx.insert(indx+1,b)
    return xx

def jn(xx,indx):
    xx[indx] = xx[indx] + xx[indx+1]
    xx.remove(xx[indx+1])
    return xx

while True :
    ordr = input()
    if ordr == "77":
        break
    elif ordr == "99":
        indexx = int(input())-1
        percent = int(input())
        x = splt(x,indexx,percent)
        
    elif ordr == "88":
        indexx = int(input())-1
        x = jn(x,indexx)
        
for i in range(len(x)):
    x[i] = str(x[i])

s = " ".join(x)
print(s)