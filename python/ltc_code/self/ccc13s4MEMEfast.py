from sys import stdin
input = stdin.readline

x = input().split()
c = int(x[0])
m = int(x[1])

dic = {}

for i in range(m) :
    y = input().split()
    t = y[0]
    s = y[1]
    if t not in dic :
        dic[t] = set()
    if s not in dic :
        dic[s] = set()
    dic[t].add(s)

q = input().split()
p1 = q[0]
p2 = q[1]

def check(garph,tal,sho) :
    visted = set()  #放訪問過的
    stack = [tal]   #放準備要訪問的一堆
    

    while stack :  #當還有要訪問時
        cur = stack.pop()  #從屁股擠出目前要訪問的人
        visted.add(cur) #把該人放在訪問過的名單內

        if cur == sho :  #如果目前訪人就是矮子
            return True  #當然就跳出啊不然要幹嘛
        
        for neibor in garph[cur] :   #如果沒有就來看dic  看看有誰比目前訪人還矮
            if neibor not in visted :  #如果比目前訪人矮的沒訪問過
                stack.append(neibor)  #就把他丟進準備要訪的一堆裡面

    return False


if p1 in dic and p1 in dic :
    if check(dic,p1,p2) :
        print("yes")
    elif check(dic,p2,p1) :
        print("no")
    else :
        print("unknown")
else :
    print("unknown")