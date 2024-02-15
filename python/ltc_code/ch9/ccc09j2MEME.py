dic = {}
#比較優雅
dic["Brown Trout"] = int(input())
dic["Northern Pike"] = int(input())
dic["Yellow Pickerel"] = int(input())
tar = int(input())

ans = 0
a = tar//dic["Brown Trout"]
b = tar//dic["Northern Pike"]
c = tar//dic["Yellow Pickerel"]


for i in range(a+1) :
    for j in range(b+1) :
        for k in range(c+1) :
            if (dic["Brown Trout"] * i + 
                dic["Northern Pike"] * j +
                dic["Yellow Pickerel"] * k) <= tar and (i+j+k)>0:
                print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
                ans+=1
print(f"Number of ways to catch fish: {ans}")



""""""

dic = {"Brown Trout":0,"Northern Pike":0,"Yellow Pickerel":0,}
lst = []
for i in dic:
    x = int(input())
    dic[i] = x
    lst.append(x)
ta = int(input())

a = ta//lst[0]
b = ta//lst[1]
c = ta//lst[2]

ans = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            
            if  i+j+k != 0 and dic["Brown Trout"] * i + dic["Northern Pike"] * j + dic["Yellow Pickerel"] * k <= ta:
                ans+=1
                print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")

print(f"Number of ways to catch fish: {ans}")

"""
################
下面在搞笑   上面根本不用dic  我的比標準答案屌  因為我先把range設在最大可能商數  
而答案直接用limit 雖然下方三個數相加的if可以過濾掉  但用limit會太多無用的數字
###################


0,1     
0,1,2
if 有人是0  不要理他

for i in range(2):c點數最大的先
    for j in range(3)
        if dic["c點數的魚"]*j + dic[b點數的魚]*i<=ta
            ans +=1

"""


"""
用最大的魚勁量塞滿limit
在用第二大的塞滿limit
在用最小的塞

塞到不能在塞以後
開始算魚總數

3 2 1
15

3x5
3x4      2x1 1x1 / 2x1 1x0  /  2x0 1x3/  2x0 1x2/  2x0 1x1/  2x0 1x0 

ta = 3  (2,1)
ans = 0
while ans <= ta
    a = ta//2   1
    b = ta//1   3
    for i in range(a)1 (0,1)
        for j in range(b)3  (0,1,2)


ta = 2  (1,2)
2x1  
2x0 1x2/ 1x1 / 1x0
####
10
02 01 00
#####

ta = 3  (1,1,3)
3x1
2x1 1x1/ 1x0 
2x0 1x3/ 1x2/ 1x1 / 1x0
#####
100
11 10
03 02 01 00
#####


ta = 5  (1,2,5)

3x1 2x1 / 2x0 1x2 / 1x1 / 1x0
3x0 2x2 1x1/ 1x0 / 2x1 1x3 /1x2 / 1x1 / 1x0/ 2x0 1x5/1x4/1x3/1x2/1x1/1x0

110 
102 101 100
021 020 
013 012 011 010 
005 004 003 002 001 000

用最大數塞 再來第2大 值到不能再塞 (while?)
塞爆後 最大樹商數-1 再來第二大....(while)
值到最大傷==0 換第二大開塞.....
值到3個商數都變0

while (a+b+c) != 0
                                                a =ta//3      b=ta//2  c=ta//3 
    for num in [3,2,1]
    x = ta // num

    if x == 0
        continue
    else:
        while x != 0 
            newta = ta - num*x
            ###開始重複#####
            for numa in [2,1]
                y = newta // numa
                if y == 0:
                    


            x-=1
        
        







3x3 2x3 
3x2 2x4 1x1
3x1 2x6
3x0 2x7 1x1 
"""