"""
cco96p2
神秘問題
    cnt = 0
    xword = ""
    xguess = ""
問題出在這三個變數設定的位置
要設在第一個for下面 讓每次for回圈重置
但是設在上面時  也就是如下的位置
運行程式會一直叫你輸入我也不知道為啥
然後如果把nums設為下方#字號的nums 輸出則會是空集合  這還好了解
真的不懂為啥會叫人一直輸入

而如果把ckcmincc的 函式跟    cnt = 0
    xword = ""
    xguess = ""

    變數和下方if拿掉  也比較正常 
    就是隨機set的取出
"""



#nums = {"1234","4321","2134","5214"}

nums = set()


for i in range(1000):
    i = str(i)
    if len(i) == 1:
        i = "000"+i
    elif len(i) == 2:
        i = "00"+i
    elif len(i) == 3:
        i = "0"+i
    nums.add(i)

for i in range(1000,10000):
    i = str(i)
    nums.add(i)

def ckcmincc(cmmm,xgus,xwod):
    xcnt = 0
    for xletter in xwod :
        if xletter in xgus and xletter != "X":
            xcnt+=1
    if xcnt != cmmm :
        return True
    else :
        return False

def ckcc(alnum,gus,ccc,cmm) :
    re = set()
    cnt = 0
    xword = ""
    xguess = ""
    for word in alnum :
        #cnt = 0
        #xword = ""
        #xguess = ""
        for idx in range(4) :
            if gus[idx] == word[idx] :
                cnt+=1
                xguess+="X"
                xword+="X"
            else :
                xguess+=gus[idx]
                xword+=word[idx]
        if cnt != ccc :
            re.add(word)
        if ckcmincc(cmm,xguess,xword) :
            re.add(word)
    for reword in re :
        alnum.remove(reword)
    return alnum

x = ckcc(nums,"1234",4,0)
print(x)