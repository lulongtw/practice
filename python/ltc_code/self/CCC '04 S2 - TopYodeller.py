x = input().split()
m = int(x[0])
n = int(x[1])

lst = []
wstrank = []
for i in range(m) :
    wstrank.append(0)
    lst.append(0)

def paimin(wrnk,listt) :
    lt = listt.copy()
    for a in range(len(lt)) :
        lt[a] = [lt[a],a]
    lt.sort(reverse=True)
    for a in range(len(lt)) :
        if a == 0 :
            mintz = 1
            lt[a].append(mintz)
        elif a > 0 and lt[a][0] != lt[a-1][0] :
            mintz = a+1
            lt[a].append(mintz) 
        elif lt[a][0] != lt[a-1][0] :
            lt[a].append(mintz)
        if wrnk[lt[a][1]] < mintz :
            wrnk[lt[a][1]] = mintz
    return wrnk

ans = []
for i in range(n) :
    y = input().split()
    for j in range(m) :
        lst[j]+=int(y[j])
    wstrank = paimin(wstrank,lst)

bestscore = max(lst)
for i in range(len(lst)) :
    if lst[i] == bestscore :
        ans.append(i)

for i in range(len(ans)) :
    print(f"Yodeller {ans[i]+1} is the TopYodeller: score {bestscore}, worst rank {wstrank[ans[i]]}")
