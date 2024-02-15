
"""
先把鐘乳石{land}和石筍{sky}分別加進各自的list
然後針對各個高度遍尋是否會撞到各個鐘乳石和石筍
如果有最小就直接紀錄  如果一樣就記錄同樣出現次數  很屌誒
其實最屌的是一次檢查完
分開後的sky和land分別檢查
因為已經sort過  所以只要檢查目前range到的高度是在list內的位置
將不會碰到(小於)高度的數量回傳 再以總數量相減  就可以得到會碰到的數量
這邊如何檢查到正確位置是用二元搜尋法的function bisect

bisect意思是回傳第二個參數放在第一個參數裡的idx

而sky方面  bisect方法裡的高度 要把他想像成把整個天花板翻下來一樣變成石筍
然後改hight 在題目例題裡cave hight是5 假設現在要處理height=4 時 是否會撞到鐘乳石2
一樣把他想像成時筍  此時height應該要變成2才會是正確要處理sky的height 所以是5-4+1 = 2
"""
 

from bisect import bisect_left

def ck(lad,sk,hh,hight) :
    res1 = len(lad) - bisect_left(lad,hight)
    res2 = len(sk) - bisect_left(sk,hh+1-hight)
    #print(res1,res2) 
    return res1 + res2



x = input().split()
n = int(x[0])
h = int(x[1])

sky = []
land = []
c = 0

for i in range(n) :
    y = int(input())
    if c%2 == 0 :
        land.append(y)
    else :
        sky.append(y)
    c+=1
land.sort()
sky.sort()

cnt = 0
minn = 9999999999999999
for hght in range(h) :
    ans = ck(land,sky,h,hght) 
    if ans < minn :
        cnt = 1
        minn = ans
    elif ans == minn :
        cnt+=1 

print(minn,cnt)


"""
x = input().split()
n = int(x[0])
h = int(x[1])

up = []
down = []

for i in range(n) :
    if i%2 == 0 :
        down.append(int(input()))
    else :
        up.append(int(input()))
up.sort()
down.sort()

"""
"""
from bisect import bisect_left

def srch(flhgt,dwn) :
    res = bisect_left(dwn,flhgt)
    return res
"""
"""

def srch(flhgt,dwn) :
    h = 0
    t = len(dwn)
    while t > h :
        mid = (t+h)//2
        if dwn[mid] >= flhgt :
            t = mid
        elif dwn[mid] < flhgt :
            h = mid + 1 
    return h


ans = []
c = 0
minn = 99999999999999
for flyheight in range(1,h+1) :

    tohit = len(down) - srch(flyheight,down)
    upheight = h - flyheight + 1
    tohit = tohit + len(up) - srch(upheight,up)

    if tohit < minn :
        minn = tohit
        c=1
    elif tohit == minn :
        c+=1

    ans.append(tohit)

print(minn,ans.count(minn))
"""





"""
#直接檢查每次輸入的範圍
#對你說對了
#相信直覺

x = input().split()
n = int(x[0])
h = int(x[1])

dic = {}
for i in range(1,h+1) :
    dic[i] = 0

rdic = {}
for i in range(h,0,-1):
    rdic[i] = 0

c = 0

for i in range(n) :
    y = int(input())
    if c%2 == 0 :
        y = set(range(1,y+1))
        for j in dic :
            if j in y :
                dic[j]+=1
            else :
                break
    else :
        y = set(range(h,h-y,-1))
        for k in rdic :
            if k in y :
                dic[k]+=1
            else :
                break
    c+=1
minn = min(list(dic.values()))
c = 0
for i in dic :
    if dic[i] == minn :
        c+=1
print(minn,c)
"""
