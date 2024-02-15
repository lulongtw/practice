x = input().split()
rr = int(x[0])
cc = int(x[1])

mirko = []
grid = []
for i in range(rr) :
    y = input()
    z = []
    for j in range(len(y)) :
        z.append(y[j])
        if y[j] == "." :
            mirko.append([i,j])
    grid.append(z)

def shakehand(grd,r,c) :
    shake = 0
    for a in range(len(grd)) :
        for b in range(len(grd[a])) :
            if grd[a][b] == "o" :
                if a!=0 and b!= 0 and grd[a-1][b-1] == "o" :
                    shake+=1

                if a!=0 and grd[a-1][b] == "o" :
                    shake+=1

                if a!=0 and b!=c-1 and grd[a-1][b+1] == "o" :
                    shake+=1

                if b!=0 and grd[a][b-1] == "o":
                    shake+=1

                if b!=c-1 and grd[a][b+1] == "o" :
                    shake+=1

                if a!=r-1 and b!=0 and grd[a+1][b-1] == "o" :
                    shake+=1

                if a!=r-1 and grd[a+1][b] == "o" :
                    shake+=1

                if a!=r-1 and b!=c-1 and grd[a+1][b+1] == "o" :
                    shake+=1

    return shake//2

if len(mirko) > 0 :
    maxx = 0
    for i in range(len(mirko)) :
        grid[mirko[i][0]][mirko[i][1]] = "o"

        ans = shakehand(grid,rr,cc) 
        #print(ans)
        if ans > maxx:
            maxx = ans
        grid[mirko[i][0]][mirko[i][1]] = "."
    print(maxx)
else :
    print(shakehand(grid,rr,cc))





"""
沒有mirko
檢查所有點與所有點之間如果他們之間的r,s相減的絕對值都<=1  如果兩點不在握過手集合 就是可以握手
加進握過手集合add[{1,2}]  

有mirko
遍尋所有控衛 
檢查所有點與所有點之間如果他們之間的r,s相減的絕對值都<=1 且不在握過手集合 就是可以握手
加進握過手集合add{} 把每個點的握手數相加 抓最大值 
"""

x = input().split()
r = int(x[0])
c = int(x[1])

s = []
plan = ""
mkseat = []
otseat = []
for i in range(r):
    x = input()
    ss = []
    for j in range(c):
        if x[j] == ".":
            plan = "mirko"
            mkseat.append([i,j])
        elif x[j] == "o":
            otseat.append([i,j])
        ss.append(x[j])
    s.append(ss)


def shk(sit,rr,cc,otseat):
    shake = 0
    shklst = []
    for i in range(rr):
        for j in range(cc):
            if sit[i][j] == "o":
                for k in range(len(otseat)):
                    row = otseat[k][0]
                    col = otseat[k][1]
                    if abs(row-i) <= 1 and abs(col-j) <= 1 and {(i,j),(row,col)} not in shklst:
                        shake+=1
                        shklst.append({(i,j),(row,col)})
                shake-=1
    return shake
                

if plan == "mirko":
    shakeres = []
    for i in range(len(mkseat)):
        x = mkseat[i][0]
        y = mkseat[i][1]
        s[x][y] = "o"
        otseat.append([x,y])
        shake = shk(s,r,c,otseat)
        shakeres.append(shake)
        s[x][y] = "."
        otseat.remove([x,y])
    print(max(shakeres))
else:
    print(shk(s,r,c,otseat))
