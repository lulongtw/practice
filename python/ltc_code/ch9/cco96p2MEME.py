 
#todel設在def內 造成只刪除最後一次迭代的東西   onans放錯位置會造成每次結果都不一樣
# taa[taa.index(numb[indx])] = "A"也考慮很久 那時在想是numb要變還是taa要變
#其實numb要變不變都沒差 因為檢查完就迭代掉了 也不會回去檢查 重點是被檢查的tar要變
#防止重複計算
#一開始沒有設計todel 直接nu.remove(number)  #說過多少遍不可以在迭代內處理被迭代物
#說過多少遍不可以在迭代內處理被迭代物
#說過多少遍不可以在迭代內處理被迭代物#說過多少遍不可以在迭代內處理被迭代物#說過多少遍不可以在迭代內處理被迭代物#說過多少遍不可以在迭代內處理被迭代物

#基本上跟標準答案是一樣的 差別在我做了整個set去檢查 把不可能加進來在去刪除
#標準答案是在一個一個生產number同時開始檢查 合格才丟叫去 少了一個存不合格的動作

nums = set()
ans = ""
for i in range(10) :
    for j in range(10) :
        for k in range(10) :
            for l in range(10) :
                ans = str(i)+str(j)+str(k)+str(l)
                nums.add(ans)

def ckon(nu,ondx,wgdx,ta,todelll) :
    for number in nu :
        onans = 0
        sameid = []
        taa = list(ta)
        numb = list(number)
        for idx in range(4) :
            if numb[idx] == taa[idx] :
                onans+=1
                sameid.append(idx)

        if onans != ondx :
            todelll.add(number)

        elif onans == ondx :
            for dx in sameid :
                taa[dx] = "A"
                numb[dx] = "A"
            wgans = 0
            for indx in range(4) :
                if numb[indx] in taa and numb[indx] != "A" :
                    wgans+=1
                    taa[taa.index(numb[indx])] = "A"
            if wgans != wgdx :
                todelll.add(number)
    return todelll


n = int(input())

for i in range(n) :
    m = int(input())
    todel = set()

    for j in range(m) :
        x = input().split()
        x[1] = x[1].split("/")
        tar = x[0]
        onidx = int(x[1][0])
        wrgidx = int(x[1][1])
        todele = ckon(nums,onidx,wrgidx,tar,todel) 
        res = nums - todele
  
    if len(res) == 1:
        for final in res :
            print(final)
    elif len(res) > 1 :
        print("indeterminate")
    elif len(res) < 1 :
        print("impossible")



""""""""""""
nums = set()

for i in range(1000,10000):
    i = str(i)
    nums.add(i)


for i in range(1000):
    i = str(i)
    if len(i) == 1:
        i = "000" + i
        nums.add(i)
    elif len(i) == 2:
        i = "00" + i
        nums.add(i)
    elif len(i) == 3:
        i = "0" + i
        nums.add(i)


def dellall(gus,alnum):

    dell = set()
    for code in alnum:
        for letter in gus:
            if letter in code:
                dell.add(code)
                continue
    for a in dell:
        alnum.remove(a)

    return alnum

def cbutm(cmm,gus,alnum):
     #如何確定idx
    re = []
    for a in alnum:
        c = 0
        for b in range(len(gus)):
            if gus[b] in a:
                c+=1
        if c != cmm:
            re.append(a)
    for b in re:
        alnum.remove(b)
    return alnum

def candc(ccc,cmm,gus,alnum):   
    re = set()
    for a in alnum: 
        gle = ""
        ale = ""
        c = 0
        for idx in range(4):            
            if gus[idx] == a[idx]:
                gle+="X"
                ale+="X"
                c+=1
            else :
                gle+=gus[idx]
                ale+=a[idx]
        if cmnum(cmm,gle,ale):
            re.add(a)

        if c != ccc:
            re.add(a)
    for b in re:
        alnum.remove(b)
    return alnum


def cmnum(cmm,glee,alee):
    cnt = 0
    for m in range(len(glee)):
        if glee[m] in alee and glee[m] != "X":
            cnt+=1
    if cnt == cmm :
        return False
    else :
        return True


def cczero(gus,alnum):
    re = []
    for a in alnum :
        for idx in range(4) :
            if gus[idx] == a[idx] :
                re.append(a)
                break
    for b in re :
        alnum.remove(b)
    return alnum


n = int(input())

for i in range(n):
    guslst = []
    allnums = nums.copy()
    m = int(input())

    for j in range(m):
        x = input().split()
        guess = x[0]
        y = x[1].split("/")
        cc = int(y[0])
        cm = int(y[1])

        if cc == 0 and cm == 0 :
            allnums = dellall(guess,allnums)
        if cm !=0 and cc == 0: 
            allnums = cbutm(cm,guess,allnums)
        if cc !=0 :
            allnums = candc(cc,cm,guess,allnums)
        if cc == 0 :
            allunms = cczero(guess,allnums)    
   
    if len(allnums) == 1:
        print(list(allnums)[0])
    elif len(allnums) == 0:
        print("impossible")
    else :
        print("indeterminate")

"""
DIGITS = "0123456789"

#n = 1
n = int(input())

def consistentnum(numb,codee,ccc,mmm):
    ccnt = 0
    mcnt = 0
    numb = list(numb)
    codee = list(codee)
    for idx in range(len(numb)):
        if numb[idx] == codee[idx] :
            ccnt+=1
            numb[idx] = "X"
            codee[idx] = "X"
    for idx in range(len(numb)) :  
        if numb[idx] != "X" and numb[idx] in codee :
            mcnt+=1
            where = codee.index(numb[idx])
            codee[where] = "A"
    if ccnt == ccc and mcnt == mmm :
        return True
    else :
        return False


def numck(coode,cc,mm):
    ans = set()
    for a in (DIGITS):
        for b in (DIGITS):
            for c in (DIGITS):
                for d in (DIGITS):
                    num = a + b + c + d
                    if consistentnum(num,coode,cc,mm):
                        ans.add(num)
    return ans

def res(guses) :
    code = guses[:4]
    c = int(guses[5])
    m = int(guses[7])
    return numck(code,c,m)

for dataset in range(n):
    m = int(input())
    answr = set()
    for i in range(m):   
        guesses = input()
        if i == 0 :
            answr = res(guesses)
        else :
            answr = answr.intersection(res(guesses))  

    if len(answr) > 1 :
        print("indeterminate")
    elif len(answr) == 0 :
        print("impossible")
    else :
        print(list(answr)[0])

"""