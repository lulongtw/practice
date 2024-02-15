import sys 
input = sys.stdin.readline

x = input().split()
n = int(x[0])
d = int(x[1])

y = input().split()
for i in range(n) :
    y[i] = int(y[i])


for i in range(d) :
    idx = int(input().strip()) 
    a = y[:idx]
    b = y[idx:]
    if sum(a) >= sum(b) :
        y = b
        print(sum(a))
    else :
        y = a
        print(sum(b))
