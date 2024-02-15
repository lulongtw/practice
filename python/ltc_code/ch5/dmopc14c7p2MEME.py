"""
最大跟最小之間是遞增
"""

x = int(input())
t = input().split()

for i in range(x):
    t[i] = int(t[i])

mx = t.index(max(t))
mn = t.index(min(t))



if mx > mn:
    t = t[mn:mx+1]
    s = t[:]
    s.sort()
    if s == t:
        print(max(t)-min(t))
    else:
        print("unknown")
else:

    print("unknown")




"""
n = int(input())
x = input().split()

mn = 9999999
mx = 0

ck = n-1
pas = True
for i in range(n) :
    x[i] = int(x[i])
    if x[i] < mn :
        mn = x[i]
        nidx = i
    if x[i] > mx :
        mx = x[i]
        midx = i

    if i !=0 and x[i] <= x[i-1] and nidx < i and pas  :  #如果”第一次“發生遞減 且 發生在 最小值之後 將該index紀錄  必須有發生一次就不能在進入這項if所以要射pas
        ck = i
        pas = False

if ck < midx or nidx > midx:  #如果第一次發生遞減的所在在最大值前  烙賽  如果 最大值比最小值前面 挫賽  ex:10 2 3 4 5 1  ex:12543
    print("unknown")
else :
    print(mx-mn)
    
"""

"""
x = int(input())
t = input().split()

for i in range(x):
    t[i] = int(t[i])

mx = t.index(max(t))
mn = t.index(min(t))


ans = t[mx]-t[mn]
ok = True
t = t[mn:mx+1]

if mx > mn :
    for i in range(len(t)) :
        if i !=0 and t[i] <= t[i-1] :
            ok = False
            #print(i)
            print("unknown")
            break

    if ok :
        print(ans)
else :
    print("unknown")
"""