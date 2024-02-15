
"""
不知道為啥沒過真的要瘋了
"""

x = input().split()
n = int(x[0])
length = int(x[1])
times = int(x[2])
hacknum = int(x[3])

def hack(spd) :
    spd = (100-hacknum)/100*spd
    return spd

def run(spd,lngh) :
    return (lngh/spd)


oppn = []
for i in range(n) :
    oppn.append(int(input()))

speed = (int(input()))


for i in oppn :
    if i <= speed :
        oppn.remove(i)
oppn.sort(reverse=True)
#tar = oppn[0]

while times > 0 and len(oppn) > 0 :
    tar = oppn.pop(0)
    while run(tar) > run(speed) :
        tar = hack(tar)
        #print(tar)
        times-=1
        if times == 0 :
            break

if len(oppn) > 0 :#or tar > speed:
   
    print("NO")
else :
    print("YES")
"""
if times > 0 or tar <= speed:
    print("YES")
else :
    print("NO")
"""
""""""

x = input().split()
n = int(x[0]) #opponent
d = int(x[1]) #length
k = int(x[2]) #times
cheat = int(x[3]) #cheat

oppo = []
for i in range(n) :
    oppo.append(int(input()))
oppo.sort(reverse=True)

p = int(input())

def hack(spd,cht) :
    spd = spd * (100-cht) / 100 
    return spd

def run(spd,lngth) :
    ans = lngth/spd
    return ans

i = 0
while k > 0 and i < n:
    while run(p,d) > run(oppo[i],d) :
        oppo[i] = hack(oppo[i],cheat)
        k-=1
        if k == 0 :
            break
    i+=1

oppo.append(p)
oppo.sort(reverse=True)
print(oppo)

if run(oppo[0],d) == run(p,d) :
    print("YES")
else :
    print("NO")





