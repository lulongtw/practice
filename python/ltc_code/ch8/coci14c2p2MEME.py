"""
有夠醜
"""

"""
第一版

n = int(input())
cl = {}
for i in range(n):
    x = input()
    if x in cl:
        cl[x] += 1
    else :
        cl[x] = 1 

rl= []
for j in range(n-1):
    rl.append(input())

for i in range(n-1):
    if rl[i] in cl:
        cl[rl[i]]-=1

idx = cl.values()
ssssss = list(idx)

for i in range(len(ssssss)):
    if ssssss[i] == 1:
        ans = i

key = list(cl.keys())



print(key[ans])
"""



"""
第二版好看 dic

n = int(input())

r = {}
for i in range(n):
    x = input()
    if x not in r:
        r[x] = 1
    else :
        r[x]+=1

f = {}
for i in range(n-1):
    x = input()
    if x not in f:
        f[x] = 1
    else:
        f[x] += 1

for key in r :
    if key not in f or r[key] > f[key] :
        print(key)
"""

n = int(input())

s = set()
for i in range(n*2-1):
    x = input()
    if x not in s:
        s.add(x)
    else :
        s.remove(x)
print(s.pop())