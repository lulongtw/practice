"""
有n個電燈 一開始全亮
有4個按鈕
1按下去原本暗的亮 原本亮的暗
2改變奇數
3改變偶數
4改變3n+1數 ex 1 4 7
按鈕c紀錄所有按鈕的總案數

題目給定特定燈亮燈暗  返回符合c及亮暗的可能


https://dmoj.ca/problem/ioi98p3
幹你娘什麼鬼 已經丟進list還可以改 我又沒叫你改
改三小  ok = True下面那一堆就是過濾特定哪幾位是0還是1 幹已經過濾完了
lamps加進去前也是ok的 
但在第三次迭代時已竟在


"""

n = int(input())
c = int(input())

on = input().split()
off = input().split()

lon = []
for i in range(len(on)) :
    on[i] = int(on[i])
    if on[i] == -1 :
        break
    else :
        lon.append(on[i]-1)

loff = []
for i in range(len(off)) :
    off[i] = int(off[i])
    if off[i] == -1 :
        break
    else :
        loff.append(off[i]-1)


psbl = set()

for b1 in [0,1] :
    for b2 in [0,1] :
        for b3 in [0,1] :
            for b4 in [0,1] :
                lamps = [1]*n
                if b1 + b2 + b3 + b4 > c :######
                    continue
                if (b1 + b2 + b3 + b4) % 2 != c % 2 :######
                    continue

                if b1 == 1:
                    lamps = [0] * n

                if b2 == 1 :
                    for i in range(len(lamps)) :
                        if i % 2 == 0 :
                            lamps[i] = 1 - lamps[i] 
                if b3 == 1 :
                    for i in range(1,len(lamps),2) : #######
                        lamps[i] = 1 - lamps[i]  ######
                if b4 == 1 :
                    for i in range(len(lamps)) :
                        if i % 3 == 0 :
                            if lamps[i] == 1 :
                                    lamps[i] = 0
                            else :
                                lamps[i] = 1

                ok = True
                for ckon in lon:
                    if lamps[ckon] == 0 :
                        ok = False
                for ckoff in loff :
                    if lamps[ckoff] == 1 :
                        ok = False
                if ok : 
                    #print(lamps)#######
                    psbl.add(tuple(lamps))
                    #print(psbl)

if len(psbl) == 0 :
    print("IMPOSSIBLE")
else :
    for config in psbl :
        ans = list(config)
        for i in range(len(ans)) :
            ans[i] = str(ans[i])
        print("".join(ans))

                                
