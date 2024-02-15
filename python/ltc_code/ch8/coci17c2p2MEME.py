x = input().split()
n = int(x[0])
m = int(x[1])

lst = []
for i in range(n) :
    lst.append(input())
lst.sort()

dic = {}
for word in lst :
    if word[0] not in dic :
        dic[word[0]] = [0,[word]]
    else :
        dic[word[0]][1].append(word)

for i in range(m) :
    q = input()
    idx = dic[q][0] % (len(dic[q][1])) 
    psbl = dic[q][1]
    print(psbl[idx])
    dic[q][0]+=1






"""
輸入最少次 如果一樣多次 輸入快字

上面是自己的慢方法 方法是
創造目標字的印出次數的字典
創造何時輪完一輪回到印出一開始的字（）的機制

下面答案給的快方訪就很簡單
直接創造母字典z:zip,zap
然後用contdic追蹤該印出母字典的哪個字

應該說慢方法她扎實具體地完成題目給的要求
但題目只要結果 
應該要簡單的看輸入到產出結果的流程  有沒有什麼因果關係
才能更簡單的完成題目

"""

x = input().split()
w = int(x[0])
l = int(x[1])

tdic = {}
words = []
dic = {}        



for i in range(w):
    x = input()
    dic[x] = 0
    words.append(x)
    if x[0] not in tdic:
        tdic[x[0]] = 1
  
words.sort()

for j in range(l):
    y = input()
    psbldic = {}
    for word in words:
        if word[0] == y:
            psbldic[word] = dic[word]
    ans = []
    c = 1
    for k in psbldic:
        ans.append(k)
        if psbldic[k] < tdic[y]:
            dic[k]+=1
            print(k)    
            break
        elif tdic[y] == psbldic[k] and c==len(psbldic):
            tdic[y]+=1
            dic[ans[0]]+=1  
            print(ans[0]) 
        c+=1
    

""""""""""""

y = input().split()
n = int(y[0])
m = int(y[1])

dic = {}
contdic = {}

for i in range(n):
    x = input()
    ltr = x[0]
    if x[0] not in dic:
        dic[x[0]] = [x]
        contdic[x[0]] = 0
    else:
        dic[x[0]].append(x)



for i in dic:
    dic[i].sort()

for i in range(m):
    z = input()
    cont = contdic[z]
    print(dic[z][cont])
    contdic[z] = (contdic[z]+1)%len(dic[z])
