"""
有n個燈
有些亮有些暗
最後要全暗
每個燈都有對應的開關
每秒最多可以按一次開關

登在接下來的M秒鐘會更換狀態

想知道最快幾秒可以全暗


靠北差在
    if ok == stats :
        done = True
多這個東西超起我真的看不懂
這個if是看到問題敘述說如果一開始就是全暗
就輸出地0秒 但其實是多餘的 因為有最終lon
會檢查到

下面有三個城市 第一個沒寫完 23ok
差別在第一個嘗試把c也就是地幾秒用成1
好複雜弄到崩潰

2是自己寫的  3跟課本幾乎一樣

23就是用第0秒開始計算
回圈先檢查目前可關數量是否可以把亮著的燈全部按掉

如果無法就在燈toggle數量小於目前可關數量的情況下
去作動燈亮燈暗 因為c代表可關數量也代表燈toggle的迭代idx

如果超出t就跳出回圈

所以23是差在把跳出回圈的機制放在裡面貨外面的差別


"""
"""
x = input().split()
l = int(x[0])
t = int(x[1])

stats = input().split()
for i in range(l) :
    stats[i] = int(stats[i])

chngs = input().split()
for i in range(t) :
    chngs[i] = int(chngs[i])-1
chngs.insert(0,0)
#print(chngs)

done = False
c = 1
while not done :
    
    if 1 not in stats :
        c-=2
        done = True
"""

################################
"""


x = input().split()
l = int(x[0])
t = int(x[1])

lon = 0
stats = input().split()
for i in range(l) :
    stats[i] = int(stats[i])
    if stats[i] == 1 :
        lon+=1


chngs = input().split()
for i in range(t) :
    chngs[i] = int(chngs[i])-1

done = False
c = 0
ok = [0]*l

while not done :
    if c  >= lon :
        done = True
    else :
        if c < t :
            stats[chngs[c]] = 1 - stats[chngs[c]]
            if stats[chngs[c]] == 1 :
                lon+=1
            else :
                lon-=1
        else :
            c = lon
            done = True 
    c+=1
print(c-1)

"""



################################


x = input().split()
l = int(x[0])
t = int(x[1])

lon = 0
stats = input().split()
for i in range(l) :
    stats[i] = int(stats[i])
    if stats[i] == 1 :
        lon+=1

chngs = input().split()
for i in range(t) :
    chngs[i] = int(chngs[i])-1

done = False
c = 0
ok = [0]*l

while c < lon and c < t :
    stats[chngs[c]] = 1 - stats[chngs[c]]
    if stats[chngs[c]] == 1 :
        lon+=1
    else :
        lon-=1
    c+=1

if c < lon :
    print(lon)
else :
    print(c)