x = input().split()
n = int(x[0])
target = int(x[1])

y = input().split()
for i in range(n) :
    y[i] = int(y[i])

y.sort(reverse=True)
trees = y

tocut = 1
cutted = 1

hrvst = 0
while hrvst < target and tocut < len(trees):
    hrvst = hrvst + (trees[tocut-1] - trees[tocut]) * cutted
    tocut+=1
    cutted+=1
   
tocut-=1
cutted-=1

if hrvst == target :
    print(trees[tocut])
else :
    add = 0
    print(((hrvst-target)//cutted)+(trees[tocut]))



""""""

x = input().split()
n = int(x[0])
t = int(x[1])

y = input().split()
for i in range(n) :
    y[i] = int(y[i])

y.sort(reverse=True)

cut = 0
for s in range(1,len(y)) :
    cut += y[s-1]
    h = cut - y[s] * (s)
    if h >= t :
        break

back = 0
if h > t :
    superfluous = h - t
    back = superfluous//s
    print(back+y[s])
else :
    print(back+y[s]+back)

"""
用sum太慢
for s in range(1,len(y)) :
    h = 0
    h = sum(y[:s]) - y[s] * (s)
    if h >= t :
        break
"""

