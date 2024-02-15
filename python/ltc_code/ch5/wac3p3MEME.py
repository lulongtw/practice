"""
對sequenceS每個字做遍訪
先拿最長的combo比較 再往短的找
找到的話找跳到字的那行
"""
x = input() 
w = len(x) 
n = int(input())
cmd=[]
for i in range(n):
    y = input().split()
    cmd.append([len(y[0]),[y[0],int(y[1])]])

cmd.sort(reverse=True)

p = 0
i = 0
while i<w:
    for j in range(len(cmd)):
        if cmd[j][1][0] == x[i:i+cmd[j][0]] :
            p+=cmd[j][1][1]
            i+=cmd[j][0]-1
            break
    i+=1
print(p+w)



"""
這部分可以通過範例 但無法通過測試 
因為下面直接改變x 但i沒有跟著一起連動
會跟蹤到錯誤的字母
p = 0
for i in range(len(x)):
    for j in range(len(cmd)):
        if cmd[j][1][0] == x[i:i+cmd[j][0]] :
            p+=cmd[j][1][1]
            x = x[i+cmd[j][0]:]
            break
print(p+w)

"""

