maxw = int(input())

n = int(input())

train = []
for i in range(n) :
    train.append(int(input()))

onbrdge = []
i = 0
while i < len(train) :
    onbrdge.append(train[i])
    if sum(onbrdge) > maxw :
        break
    else :
        if len(onbrdge) == 4 :
            onbrdge.pop(0)
        i+=1
print(i)
""""""
maxw = int(input())
n = int(input())
train = []
for i in range(n) :
    train.append(int(input()))

i = 0
ok = True
while ok and i < len(train) :
    curwg = 0
    for onbg in range(4) :
        if i+onbg < len(train):
            curwg+=train[i+onbg]
            if curwg > maxw :
                ok = False
                onbg = onbg-1
                break
    i+=1
print(i+onbg)