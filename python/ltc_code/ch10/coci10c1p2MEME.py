"""
還以為想不出來
"""
n = int(input())

maxc = 0
mingrd = 99999999
dic = {}

for i in range(n) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    x = set(x)
    for key in dic :
        if key not in x :
            dic[key] = 0

    for stnt in x :
        if stnt not in dic :
            dic[stnt] = 1
        else :
            dic[stnt] +=1

        if dic[stnt] == maxc :
            if stnt < mingrd :
                mingrd = stnt

        if dic[stnt] > maxc :
            maxc = dic[stnt]
            mingrd = stnt

print(maxc,mingrd)

    

"""
2 1  2c=1 1c=1  1=1  1<2      有新答案另外處理ans: 1 1

現在紀錄1 1 2 1

3 2  檢查舊東西2和1有沒有在裡面  1沒有 去掉    2有2c=2   3c=1     有新答案另外處理ans:2 2 舊ans 11拿掉

現在 3 1  2 2

5 3  檢查舊東西  3在 3c=2  2不在去掉  5c=1


3
3 5
1 3
1 3
"""


"""
照記憶裡的標準答案解法  比標準帥
"""

n = int(input())

lst = []
for i in range(n) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    lst.append(x)


maxcnt = 0
for grd in range(1,6) :
    c = 0
    for stnts in lst :
        if grd in stnts :
            c+=1
        else :
            c = 0
        if c > maxcnt :
            maxcnt = c
            ans = grd
print(maxcnt,ans)

"""

n = int(input())
##################看答案的##########################
desks = []
for i in range(n) :
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    desks.append(x)

def check(dsk,grd) :
    cnt = 0
    maxx = 0
    for i in range(len(dsk)) :
        if grd in dsk[i] :
            cnt+=1
            if maxx < cnt :
                maxx = cnt
        else :
            cnt = 0
    return maxx


maxcombo = 0
smgrd = 99999999
for grade in range(1,6) :
    res = check(desks,grade)
    #print(res)
    if res > maxcombo:
        maxcombo = res
        smgrd = grade

print(maxcombo,smgrd)



"""

################爽拉################################
n = int(input())


dic = {}  #每次迭代的字典 計算每次新分數是否有連續
ansdic = {}  #計算每次創新高連續的分數
lngcnt = 0   #最高分
for i in range(n) :
    ke = list(dic.keys())  #取得上一次迭代的分數
    x = input().split()
    if i != 0 :    #因為第一次迭代沒有上一次迭代的資料 所以設if跳過
        for key in ke :  #如果上一次的分數不在新分數裡 就把它拿掉  
            if str(key) not in x :
                del dic[key]
    for j in range(2) :  
        x[j] = int(x[j])
        if j == 1 and x[1] == x[0] :  #防止3 3同一桌都同分的情況 這樣會重複計算cnt
            break
        if x[j] in dic :  
            dic[x[j]] += 1

        elif x[j] not in dic :
            dic[x[j]] = 1

        if dic[x[j]] >= lngcnt :  #連=也加進因為將辨認大小的工作留到最後
            lngcnt = dic[x[j]]
            ansdic[x[j]] = lngcnt

keys = []  

for key in ansdic:    #檢查那些曾經是最長連續的分數  已經確定lngcnt是最長combo了  找出最小值
    if ansdic[key] == lngcnt :
        keys.append(key)

print(lngcnt,min(keys))

