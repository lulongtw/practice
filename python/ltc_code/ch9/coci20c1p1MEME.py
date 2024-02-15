x = input().split()
row = int(x[0])
col = int(x[1])


map = []
for i in range(row) :
    m = []
    x = input()
    for j in range(col) :
        m.append(x[j])
        if x[j] == "o" :
            strt = [i,j]
    map.append(m)

n = [strt[0]-1,strt[1]]
e = [strt[0],strt[1]+1]
w = [strt[0],strt[1]-1]
s = [strt[0]+1,strt[1]]

def voyage(derction,mapp) :
    r = derction[0]
    c = derction[1]
    route = 0

    while mapp[r][c] != "o" and mapp[r][c] != "x" and mapp[r][c] != "." :
        if mapp[r][c] == ">" :          
            c+=1
        elif mapp[r][c] == "<" :      
            c-=1
        elif mapp[r][c] == "^" :
            r-=1
        elif mapp[r][c] == "v" :
            r+=1
        route+=1

    if mapp[r][c] == "o" or mapp[r][c] == ".":
        return -1
    elif mapp[r][c] == "x" :
        return route


res = []
minn = 999999999999999999999999
for derc in [e,n,s,w] :
    x = voyage(derc,map)
    if x != -1 and derc == n:
        res.append([x,"N"])
    elif x != -1 and derc == e:
        res.append([x,"E"])
    elif x != -1 and derc == w:
        res.append([x,"W"])
    elif x != -1 and derc == s:
        res.append([x,"S"])
    if x != -1 and x < minn :
        minn = x

if minn == 999999999999999999999999:
    print(":(")
else :
    for i in range(len(res)) :
        if res[i][0] == minn :
            print(":)")
            print(res[i][1])
            break

"""
比較醜一點
"""
def voyage(cur,mapp) :
    rr = cur[0]
    cc = cur[1]
    cnt = 1
    while mapp[rr][cc] != "." and mapp[rr][cc] != "x" and mapp[rr][cc] != "o" :
        if mapp[rr][cc] == ">" :
            cc+=1
        elif mapp[rr][cc] == "<" :
            cc-=1
        elif mapp[rr][cc] == "^" :
            rr-=1
        elif mapp[rr][cc] == "v" :
            rr+=1
        cnt+=1

    
    if mapp[rr][cc] == "x" :
        return cnt
    else :
        return 0


x = input().split()
r = int(x[0])

map = []

for i in range(r) :
    y = list(input())
    if "o" in y :
        strt = [i,y.index("o")]
    map.append(y)

ans = []
minn = 999999
for dirc in ['e', 'n', 's', 'w'] :
    crnt = strt.copy()
    if dirc == "e" :
        crnt[1]+=1
    elif dirc == "n" :
        crnt[0]-=1
    elif dirc == "s" :
        crnt[0]+=1
    elif dirc == "w" :
        crnt[1]-=1
    
    res = voyage(crnt,map)
    if res :
        if res < minn :
            minn = res
        ans.append([dirc,res])

if len(ans) == 0 :
    print(":(")
else :
    for i in range(len(ans)) :
        if ans[i][1] == minn :
            break
    print(":)")
    print(ans[i][0].upper())