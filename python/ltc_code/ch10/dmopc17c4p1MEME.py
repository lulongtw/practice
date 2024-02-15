x = input().split()
r = int(x[0])
n = int(x[1])

blue = []
for i in range(n) :
    y = input().split()
    y[0] = int(y[0])
    y[1] = int(y[1])
    blue.append(y)

blue.sort()

ans = 0
rmost = 0
for i in range(len(blue)) :
    head = blue[i][0]
    tail = blue[i][1]

    if head > rmost :
        ans += tail - head
        rmost = tail

    if head <= rmost and tail > rmost :
        ans+=tail-rmost
        rmost = tail

print(r-ans,ans)



"""
在每次迭代時就把答案處理起來
能簡單就簡單不需要加入太多資料


答案用很簡單的r變數追蹤藍色的最右邊的idx:r
blue已經sort過 所以只要專心在新迭代的頭h是否小於等於藍色的最右邊
如果小於最右邊做代表新迭代是在舊有藍色內
再繼續檢查尾巴t是否小於r  如果小於代表頭在舊藍色內
尾巴在外面 就將多餘的部分(新藍色t-r)加進ans舊藍色內
如果連t也等於r   代表全部都在舊藍色內就不去理他
如果頭h大於舊藍色r 則直接計算新藍色t-h 加進舊藍色內
每次有加入都要更新舊藍色r


我的舊方法其實也有點像
只是在發現新藍色時 嘗試用set(range)去處理
用set蓋掉重複的部分  
如果是舊藍色就用union 跟上一個set融合
如果發現新藍色就把它做成set 加進ans 然後用c來步進現在這個剛加入的set
最後再算ans的總len

但錯了

就是下面那個  我也看不出來哪邊有錯

還有一個是用minus 嘗試在每次迭代找出重複的 把它加進minus內 最後再一次檢調 = =
"""
x = input().split()
n = int(x[0])
q = int(x[1])

blue = []
for i in range(q) :
    y = input().split()
    y[0] = int(y[0])
    y[1] = int(y[1])
    blue.append(y)

blue.sort()

ans = 0
r = 0

for bl in blue :
    h = bl[0]
    t = bl[1]
    if h <= r :
        if t > r:
            ans = ans + t - r 
            r = t
    else :
        ans = ans + t - h 
        r = t

print(n-ans,ans)


"""

x = input().split()
n = int(x[0])
q = int(x[1])

blue = []
for i in range(q) :
    y = input().split()
    y[0] = int(y[0])
    y[1] = int(y[1])
    blue.append(y)

blue.sort()

s = set()
ans = [s]
c = 0
for i in range(1,q) :
    if blue[i][0] <= blue[i-1][1] :
        k = set(range(blue[i-1][0],blue[i][1]+1))
        ans[c] = ans[c].union(k)
        
        #print("aa",ans)
    else :
        ans.append(set(range(blue[i][0],blue[i][1]+1)))
        c+=1

res = 0
for i in ans :
    res += (len(i)-1)
print(n-res,res)
"""
###############################################################
#############################################

"""
minus = 0
for i in range(1,q) :
    if blue[i][0] <= blue[i-1][1] :
        if blue[i][1] <= blue[i-1][1] :
            minus += (blue[i][1] - blue[i][0])
        else :
            minus += (blue[i-1][1] - blue[i][0] + 1)
"""


"""
x = input().split()
n = int(x[0])
q = int(x[1])

blue = []
for i in range(q) :
    y = input().split()
    head = int(y[0])
    tail = int(y[1])
    for i in range(len(blue)) :
        if head in blue[i] and tail in blue[i] :
            break
        elif head in blue[i] or tail in blue[i] :
            addblue = set(range(head,tail+1))
            blue[i] = blue[i].union(addblue)
            break
    else :
        blue.append(set(range(head,tail+1)))

#print(blue)
ans = set()
ck = blue[0] 
for i in range(1,len(blue)) :

    if len(ck.intersection(blue[i])) != 0:
        blue[i-1] = blue[i-1].union(blue[i])


for i in range(len(blue)-1) :
    if len(blue[i].intersection(blue[i+1])) != 0 :
        ans.add

print(ans)
"""