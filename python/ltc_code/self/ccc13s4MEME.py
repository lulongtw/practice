"""
班上有Ｎ人 會做Ｍ次檢查
每個人身高都不一樣
頭高於尾
檢查最後一行是否頭高於尾
pq可能都沒出現在測量內

10 4
2 4
3 4
4 9
4 10


10 5
2 4
4 6
4 3
3 9
9 6

10 8
7 9
2 9
9 5
4 8
3 2
3 4
3 7
1 3

10 7
2 4
4 9
9 11
1 3
3 5
5 4
4 10

以上為測試用例  但都沒有加上最後的提出問題的那一行
主要是看土炮能不能解決這個問題

方法是把所有可能做出來再做判斷  所以一定超時
是以確定以某數字為基準，只要該數字是在目前資料的頭或是尾巴
就開始找資料內有沒有該數字  
如果現在是尾  把另一資料該數字以後的資料放在目前資料的後面
如果是頭  就把它放在前面
但這個方法會遇到一個困難
他無法跨lst比較
例如
10 7
2 4
4 9
9 11
1 3
3 5
5 4
4 10 
他最後會形成兩個集團
但集團間無法互相比較
所以要靠最後ok=false下面那邊去比較
好累我不想打了
打了這麼多還是超時我的天

"""
x = input().split()

n = int(x[0])
t = int(x[1])

lst = []
c = 0

for i in range(t) :
    y = input().split()
    inn = False
    if c == 0 :
        lst.append(y)
    else :
        for k in range(len(lst)) :
            if y[0] == lst[k][-1] :  
                lst[k].append(y[1])
                inn = True
                #print(lst)
                break
            elif y[1] == lst[k][0] :
                lst[k].insert(0,y[0])
                inn = True
                #print(lst)
                break
        if not inn  :
            lst.append(y)  
    c+=1
#print(lst)
for i in range(len(lst)) :
    for j in range(len(lst)) :
        if lst[i][-1] in lst[j] and lst[j].index(lst[i][-1]) != -1 :
            #print("ab",lst)
            for k in range(lst[j].index(lst[i][-1])+1,len(lst[j])) :
                lst[i].append(lst[j][k])
                #print("af",lst)



        if lst[i][0] in lst[j] and lst[j].index(lst[i][0]) != 0 :
            #print("bb",lst)
            for l in range(lst[j].index(lst[i][0])-1,-1,-1) :
                lst[i].insert(0,lst[j][l])
                #print("ba",lst)
#print(lst)


inn = False
q = input().split()

for i in range(len(lst)) :
    if q[0] in lst[i] and q[1] in lst[i] :
        if lst[i].index(q[0]) < lst[i].index(q[1]) :
            print("yes")
            inn = True
            break
        elif lst[i].index(q[0]) > lst[i].index(q[1]) :
            print("no")
            inn = True
            break

ok = False
for i in range(len(lst)) :
    for j in range(len(lst[i])) :
        fs = set()
        es = set()
        for k in range(len(lst)) :
            if k == i :
                continue
            else :
                if lst[i][j] in lst[k] :       
                    ft = lst[i][:lst[i].index(lst[i][j])] + lst[k][:lst[k].index(lst[i][j])]
                    et = lst[i][lst[i].index(lst[i][j])+1:] + lst[k][lst[k].index(lst[i][j])+1:]
                    if q[0] in set(ft) and q[1] in set(et) :
                        if not ok :
                            print("yes")
                            inn = True
                            ok = True
                            break
                    elif q[1] in set(ft) and q[0] in set(et) :
                        if not ok :
                            print("no")
                            inn = True
                            ok = True
                            break

if not inn :
    print("unknown")

