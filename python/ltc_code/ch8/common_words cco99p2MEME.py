q = int(input())

def rank(num) :
    if num[-1] == "1" and num[-2:] != "11" :
        return (num+"st")
    elif num[-1] == "2" and num[-2:] != "12" :
        return (num+"nd")
    elif num[-1] == "3" and num[-2:] != "13" :
        return (num+"rd")
    else :
        return (num+"th")
    

for data in range(q) :
    x = input().split()
    n = int(x[0])
    m = x[1]

    dic = {}
    for i in range(n) :
        y = input()
        if y not in dic :
            dic[y] = 1
        else :
            dic[y]+=1
  
    val = list(dic.values())
    val.sort(reverse=True)
    """
    出現次數 6 5 3 3 3 2 2 2 2 2 1
    實際引得 0 1 2 3 4 5 6 7 8 9 10
    程式名次 0 1 2 2 2 5 5 5 5 5 9
    最後名次 1 2 3 3 3 6 6 6 6 6 10
    可以看到 基本上名次都是跟著引得idx 但是有例外
    就是有重複的時候 如果重複就是印出空白  所以就做條件句引流
    但名次要先減1才能符合idx規則
    當名次不等於1且該名次的數量跟上一個一樣時  代表該名次不是第一個
    故跳過
    """
    idx = int(m) - 1

    if  idx >= len(val) or (idx > 0 and val[idx] == val[idx-1]) :
        print(f"{rank(m)} most common word(s):\n")
    else :
        print(f"{rank(m)} most common word(s):")
        for i in dic :
            if dic[i] == val[idx] :
                print(f"{i}")
        print()





"""
每個名次都做一個ans   跟下方不一樣
步進到目標名次後跳出回圈 印出ans
一但名次超出總體字數 ans = ""
要是名次小於等於當前字總數 ans = ""
一但名次大於當前自總數 就更新字總數 跟上目前名次
如果目前名次等於目標名次
跳出回圈
但送過去ir 我不知道哪裡錯尻杯
"""


#n = 1
n = int(input())
def suffix(nn):
    nn = str(nn)
    if nn[-1] == "1" and nn[-2:] == "11":
        return nn + "st"
    elif nn[-1] == "2" and nn[-2:] == "12":
        return nn + "nd"
    elif nn[-1] == "3" and nn[-2:] == "13":
        return nn + "rd"
    else :
        return nn + "th"
    

for i in range(n):
    x = input().split()
    m = int(x[0])
    rank = int(x[1])
    dic = {}
    for j in range(m):
        y = input()
        if y not in dic:
            dic[y] = 1
        else :
            dic[y]+=1
    va = list(set(dic.values()))
    keys = len(list(dic.values()))
    va.sort(reverse=True)
    rdic = {}
    for j in range(len(va)):
        for key in dic:
            if va[j] == dic[key]:
                if va[j] not in rdic:
                    rdic[va[j]] = [key]
                else:
                    rdic[va[j]].append(key)
  
    va.insert(0,0)
    crntrnk = 1
    c = crntrnk
    ans = rdic[va[c]]
    wrdcnt = len(ans)

    while crntrnk < rank :
        crntrnk+=1
        if crntrnk > keys:
            ans = ""
            break
        if crntrnk <= wrdcnt :
            ans = ""
        else:
            c+=1
            ans = rdic[va[c]]
            wrdcnt+=len(ans)

    print(f"{suffix(rank)} most common word(s):")
    for j in ans:
        print(j)
    print()

""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    rank 是 k
    i<len(nums)確保
    用i步進定位下一個要加入總數的字母們
    搜尋 依照出現次數大小排例的字母的總數 如果大於等於rank 代表找到了 跳出回圈
    否則 繼續找讓總數大於rank


    if wrdcnt = rank-i是用來確定 rank是否剛好落在 總數的+1位  
    而下方的else在更新完wrdcnt後將i步進1 所以下方print才是正確的
    只有這樣指定rank
    才能印出答案 而答案就是靠i步進nums去mapping  n.to w.字典的字串們
    
    課本答案while下的if是 if wrdcnt+len(rdic[va[i]])>=k
    意思是找到字數總和大於等於rank數為止 這邊就停止 讓i保持在rank附近
    接著再用下面的if過濾

    而我的wrdcnt == rank -1是直接定位 如果正確 且i沒過len(va)
    因為我這樣直接定位rank-1 會讓 i 一直跑到最後 變成說
    如果我沒有設第二個if i會跑到最後面 
    

21 2
the
the
the
the
red
red
red
red
cho
cho
cho
cho
fox
fox
apple
apple
ok
ok1
ok2
ok3
ok4

4 the red cho   2 fox appele   1 ok 1ok 2ok 3ok 4ok             [0,4,2,1]
    1     2    3	      4	     5    	   6   7      8    9    10
   
          va1              va2     		         va3
    1     1    1	      4    4            6    6      6      6     6




"""
"""

#n = 1
n = int(input())

def suffix(nn):
    nn = str(nn)
    if nn[-1] == "1" and nn[-2:] != "11":
        return nn + "st"
    elif nn[-1] == "2" and nn[-2:] != "12":
        return nn + "nd"
    elif nn[-1] == "3" and nn[-2:] != "13":
        return nn + "rd"
    else :
        return nn + "th"
    

for i in range(n):
    x = input().split()
    m = int(x[0])
    rank = int(x[1])
    dic = {}
    for j in range(m):
        y = input()
        if y not in dic:
            dic[y] = 1
        else :
            dic[y]+=1
    va = list(set(dic.values()))
    va.sort(reverse=True)
    rdic = {}
    for j in range(len(va)):
        for key in dic:
            if va[j] == dic[key]:
                if va[j] not in rdic:
                    rdic[va[j]] = [key]
                else:
                    rdic[va[j]].append(key)


    i = 0
    done = False
    wrdcnt = 0
    while i < len(va) and not done:
        if wrdcnt == rank -1 :
            done = True
        else:
            wrdcnt+=len(rdic[va[i]])
            i+=1
    if i < len(va):
        ans = rdic[va[i]]
    else :
        ans = []
    
    print(f"{suffix(rank)} most common word(s):")
    for j in ans:
        print(j)

    print()
"""