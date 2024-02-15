"""
算柱子長度
所有平台高度加總
一個平台的頭尾柱子的x點是否有含在其他平台的頭尾range裡(由最高y的平台開始遍尋)
如果找到 該柱子長度減去遍尋到的平台長度
"""

n = int(input())

pl = 0
p = []
for i in range(n):
    x = input().split()
    for j in range(len(x)):
        x[j] = int(x[j])
    pl+=(x[0]*2)
    p.append(x)
p.sort(reverse=True)



for i in range(len(p)-1):
    head = p[i][1]+0.5
    tail = p[i][2]-0.5
    for hort in ([head,tail]):
        for j in range(i+1,len(p)):
            phead = p[j][1]
            ptail = p[j][2]
            if hort > phead and hort < ptail :
                pl-=p[j][0]
                break

print(pl)











"""
n = int(input())

pl = 0
p = []
for i in range(n):
    x = input().split()
    for j in range(len(x)):
        x[j] = int(x[j])
    pl+=(x[0]*2)
    p.append(x)
p.sort(reverse=True)



for i in range(len(p)-1):
    head = p[i][1]+0.5
    tail = p[i][2]-0.5
    for j in range(i+1,len(p)):
        phead = p[j][1]
        ptail = p[j][2]
        if head > phead and head < ptail :
            pl-=p[j][0]
            break
    for k in range(i+1,len(p)):
        phead = p[k][1]
        ptail = p[k][2]
        if tail > phead and tail < ptail :
            pl-=p[k][0]
            break
print(pl)
"""