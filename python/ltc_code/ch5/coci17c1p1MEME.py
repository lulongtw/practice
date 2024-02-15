"""
ace     11
10 j q k   10
2~9     2~9
"""

card = [0,0,4,4,4,4,4,4,4,4,16,4]
x = int(input())
summ = 0
for i in range(x):
    y = int(input())
    summ+=y
    card[y] = card[y] - 1

ans = 21-summ

if sum(card[:ans+1]) <= sum(card[ans+1:]) :
    print("DOSTA")
else :
    print("VUCI")

"""
#上面是之前的 下面是新的 結果就的筆芯的好= =

dic = {0:0,1:0,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:16,11:4}

inhand=0
n = int(input())
for i in range(n) :
    x = int(input())
    inhand+=x
    dic[x]-=1

y = 21-inhand
a=0
b=0

for i in dic :
    if i<=y :
        a+=dic[i]
    if i>y :
        b+=dic[i]
    

if a>b :
    print("VUCI")
    
else :
    print("DOSTA")

"""