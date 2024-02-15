n = int(input())

brks = []
for i in range(n) :
    brks.append(int(input()))


def split(bks,idx,pcnt) :
    lsplt = bks[idx] * pcnt // 100
    rsplt = bks[idx] - lsplt
    bks = bks[:idx] + [lsplt,rsplt] + bks[idx+1:]
    return bks

def joinn(bks,idx) : 
    jon = bks[idx] + bks[idx+1]
    bks = bks[:idx] + [jon] + bks[idx+2:]
    return bks


done = False
while not done :
    s = int(input())
    if s == 99 :
        indx = int(input())-1
        percnt = int(input())
        brks = split(brks,indx,percnt)
    elif s == 88 :
        indx = int(input())-1
        brks = joinn(brks,indx)
    elif s == 77 :
        done = True

for i in range(len(brks)) :
    brks[i] = str(brks[i])
print(" ".join(brks))