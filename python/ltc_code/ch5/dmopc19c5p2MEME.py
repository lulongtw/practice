x = input().split()
n = int(x[0])
h = int(x[1])

a = []
both = []
for i in range(n*2) :
    y = input().split()
    y[1] = int(y[1])
    a.append(y)
  
i=0
for c in range(n*2) :
    if c%2 == 0 :
        both.append(a[i])
    else :
        both.append(a[n+i])
        i+=1

ch = h
rh = h
turn = 0
while ch>0 and rh>0 and turn < len(both):

    dmg = 0

    if both[turn][0] == "A" and (both[turn-1][0] != "D" or turn == 0) :#
        dmg = both[turn][1]
        self = False

    elif both[turn][0] == "D" and (turn == len(both)-1 or both[turn+1][0] != "A" ) :#
        dmg = both[turn][1]   
        self = True

    if turn%2 == 0 and dmg:
        if self :
            ch-=dmg
        else :
            rh-=dmg

    elif turn%2 == 1 and dmg:
        if self :
            rh-=dmg          
        else :
            ch-=dmg
  
    turn+=1

if rh <= 0 :
    print("VICTORY")
elif ch <= 0 :
    print("DEFEAT")
else :
    print("TIE")



"""
#old

x = input().split()
m = int(x[0])
h = int(x[1])

cm = []
for i in range(m):
    x = input().split()
    x[1] = int(x[1])
    cm.append(x)

om = []
for i in range(m):
    x = input().split()
    x[1] = int(x[1])
    om.append(x)

totalm=[]
cc = 0
oc = 0
for i in range(m*2):
    if i%2 == 0:       
        totalm.append(cm[cc])
        cc+=1
    else:      
        totalm.append(om[oc])
        oc+=1

totalm.append(["no"])
totalm.insert(0,["no"])

ch = h
oh = h

def moveresult(tm,cc,myhp,enhp):
    if tm[cc][0] == "A" and tm[cc-1][0] != "D":
        enhp = enhp - tm[cc][1]
    elif tm[cc][0] == "D" and tm[cc+1][0] !="A":
        myhp = myhp - tm[cc][1]
    return[myhp,enhp]
    

c = 1
while ch >0 and oh > 0 and c!=m*2+1:
    if c%2 == 1:

        res = moveresult(totalm,c,ch,oh)
        ch = res[0]
        oh = res[1]
        #print(c,ch,oh)
    else :
        res = moveresult(totalm,c,oh,ch)
        oh = res[0]
        ch = res[1]
        #print(c,ch,oh)
    c+=1
#print(c,ch,oh)


if ch <= 0 :
    print("DEFEAT")
elif oh <= 0 :
    print("VICTORY")
else:
    print("TIE")

"""
