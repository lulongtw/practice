x = input().split()
n = int(x[1])
scarf = input().split()
dic = {}
for i in range(len(scarf)) :
    scarf[i] = int(scarf[i])
    if scarf[i] not in dic :
        dic[scarf[i]] = [i]
    else :
        dic[scarf[i]].append(i)

maxx = 0 
for i in range(n) :
    rel = input().split()
    head = int(rel[0])
    tail = int(rel[1])
    if head in dic and tail in dic :
        length = dic[tail][-1] - dic[head][0] + 1
        if length > maxx :
            maxx = length
print(maxx)


"""
不要把.keys()或.values()放在回圈
想把key抓出來做成集合看會不會比較快
結果因為這樣變超慢
原本可以的程式變超慢幹
下面這是第一版
第二版是用rdic也就是
迭代到該數字第一次時  放入rdic和ldic  確定最基本的起始與結束位置都有 
如果目前迭代的數字(顏色)有第二個的話(他目前第二個的位置也比較右邊)
就放進去 每次迭代找到更右的位置都會迭代到較左的位置  而最左的位置已經放在ldic了
所以最基本的起始與結束位置都有 


"""



x = input().split()
s = int(x[0])
r = int(x[1])


ldic = {}
#rdic = {}
scarf = input().split()
for i in range(s) :
    scarf[i] = int(scarf[i])

    if scarf[i] not in ldic :########
        ldic[scarf[i]] = [i]
        ####rdic[scarf[i]] = i##########
    else :
        #rdic[scarf[i]] = i
        ldic[scarf[i]].append(i)

ans = 0
for i in range(r) :
    rela = input().split()
    head = int(rela[0])
    tail = int(rela[1])
    if head in ldic and tail in ldic :######
        hidx = ldic[head][0]
        tidx = ldic[tail][-1]

        """
        if tail in rdic : #############
            tidx = rdic[tail]  #############
        else :
            tidx = ldic[tail]
        """
        if tidx >= hidx :
            if tidx - hidx + 1 > ans :
                ans = tidx - hidx + 1

print(ans)

"""
x = input().split()
s = int(x[0])
r = int(x[1])

scarf = input().split()

for i in range(s) :
    scarf[i] = int(scarf[i])

rscarf = []
for i in range(s-1,-1,-1):
    rscarf.append(scarf[i])

ans = set()
for i in range(r) :
    rela = input().split()
    head = int(rela[0])
    tail = int(rela[1])
    if head and tail in set(scarf) :
        hidx = scarf.index(head)
        tidx = rscarf.index(tail)
        tidx = len(scarf) - tidx - 1
        if tidx >= hidx :
            ans.add(len(scarf[hidx:tidx+1]))

if len(ans) == 0 :
    print(0)
else :
    print(max(ans))
"""




"""
#慢慢慢慢慢暗慢暗慢慢

x = input().split()
n = int(x[0])
m = int(x[1])

scarf = input().split()

for i in range(n) :
    scarf[i] = int(scarf[i])

ans = []
for i in range(m) :
    rela = input().split()
    rela[0] = int(rela[0])
    rela[1] = int(rela[1])
    head = []
    tail = []
    ok = True
    for j in range(len(scarf)) :
        for k in range(2) :
            if rela[0] == scarf[j]:
                head.append(j)
            if rela[1] == scarf[j] :
                tail.append(j)
    if len(head) > 0 :
        realhead = min(head)
    else :
        ok = False
        
    if len(tail) > 0 :
        realtail = max(tail)
    else: 
        ok = False
    if ok :
        ans.append(len(scarf[realhead:realtail+1]))
print(max(ans))
"""
            




    