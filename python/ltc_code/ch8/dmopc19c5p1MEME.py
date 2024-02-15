x = input().split()
items = int(x[0])
misn = int(x[1])

eq = set()
for i in range(items) :
    eq.add(input())

ans = 0

for i in range(misn) :
    ok = True
    n = int(input()) 
    for j in range(n) :
        if input() not in eq :
            ok = False
    if ok :
        ans+=1

print(ans)

""""""
#訓訓ㄉ 
x = input().split()

it = int(x[0])
m = int(x[1])

items = set()
for i in range(it):
    items.add(input())

ans = 0
for i in range(m):
    msn = set()
    y = int(input())
    for j in range(y):
        msn.add(input())
    """
    if msn.issubset(items)
        ans+=1
    """
    c = 0
    for j in msn:
        if j in items:
            c+=1
    if c == len(msn) :
        ans+=1
print(ans)