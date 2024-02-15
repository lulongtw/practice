n = int(input())

vlgrlst = [set()]
for i in range(n) :
    vlgrlst.append(set())

m = int(input())

songnum = 0
for i in range(m) :
    x = input().split()
    x = x[1:]
    for j in range(len(x)) :
        x[j] = int(x[j])
    
    today = set(x)
    
    if 1 in today :
        for vlgr in today :
            vlgrlst[vlgr].add(songnum)
        songnum+=1
    else :
        songs = set()
        for vlgr in today :
            songs.update(vlgrlst[vlgr])
        for vlgr in today :
            vlgrlst[vlgr].update(songs)
        
for i in range(len(vlgrlst)) :
    if vlgrlst[i] == vlgrlst[1] :
        print(i)

"""
這也是錯的只是比較好看

下面兩個範例無法通過
4
3
2 1 3
2 2 4
2 1 4

4
4
2 1 2
2 1 4
2 4 3
2 2 3

vnum = int(input())
e = int(input())

old = set()
first = True
for i in range(e):
    x = input().split()
    x.pop(0)
    x = set(x)
    if "1" in x and first:
        old = x
        first = False
        continue
    if "1" in x :
        old = old.intersection(x)       
    elif "1" not in x :
        #if len(old.intersection(x)) > 0 :
            old.update(x)

ans = list(old)
for i in range(len(ans)) :
    ans[i] = int(ans[i])
ans.sort()
for i in ans :
    print(i)
"""

"""
這是錯的
n = int(input())
e = int(input())

c = 0
olds = set()

for i in range(e):
    x = input().split()

    nows = set()
    first = False

    for j in range(1,len(x)):
        if "1" == x[j] and c == 0 :
            first = True
            c+=1
        nows.add(int(x[j]))
        
    if first :
        olds = nows
    else:
        if 1 not in nows:
            #if len(olds.intersection(nows)) > 0 :
                olds = olds.union(nows)
        elif 1 in nows:
            olds = olds.intersection(nows)

olds = list(olds)
olds.sort()
for i in olds:
    print(i)

"""
"""
有1出現 加所有人進old set
如果沒1 繼續加進oldset
1在出線  加當次所有人進new set 檢查oldset裡所有人是否有在newset 
        把不在newset的人移出old set
"""



"""
#dic法 不知道為啥錯

vnum = int(input())
e = int(input())


dic = {}
for a in range(e):
    x = input().split()
    x = x[1:]
    x = set(x)
 

    if "1" in x :
        for j in x :
            if j not in dic :
                dic[j] = 1
            else :
                dic[j] +=1
        #print(dic)
    elif "1" not in x :
        keys = set(list(dic.keys()))
        instkeys = keys.intersection(x)
        if len(instkeys) > 0 :
            maxx = 0
            for k in instkeys :
                if dic[k] > maxx :
                    maxx = dic[k]
            for k in x :
                if k not in dic :
                    dic[k] = maxx
        #print(dic)

#print(dic)

ans =[]
tar = dic["1"]
for i in dic :
    if dic[i] == tar :
        ans.append(int(i))
ans.sort()
for i in ans :
    print(i)

"""






"""
v = int(input())

allvs = [set()]

for i in range(v):
    allvs.append(set())

n = int(input())
songname = 0

for i in range(n):
    x = input().split()
    x.pop(0)
    for j in range(len(x)) :
        x[j] = int(x[j])

    if 1 in x:
        for j in x :
            allvs[j].add(songname)
        songname+=1
    else :
        y = set()
        for j in x:
            y.update(allvs[j])
        for j in x :
            allvs[j].update(y)

ans = [1]
for i in range(2,len(allvs)) :
    if allvs[i] == allvs[1] :
        ans.append(i)

for i in ans:
    print(i)

"""