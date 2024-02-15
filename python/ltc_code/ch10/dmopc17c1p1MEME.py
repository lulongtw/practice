import sys
input = sys.stdin.readline

x = input().split()
r = int(x[0])
c = int(x[1])

ghostrow = set()
ghostcol = set()
for row in range(r) :
    y = input().strip()
    while y != "." * c :
        col = y.index("X")
        ghostrow.add(row+1)
        ghostcol.add(col+1)
        y = y[:col] + "." + y[col+1:]

n = int(input())
for i in range(n):
    y = input().split()
    sr = int(y[1])
    sc = int(y[0])
    #for j in [sr,sc] :
    if sr in ghostrow or sc in ghostcol :
        print("Y")
    else:
        print("N")


        
"""
for row in range(r) :
    y = input()
    while y != "." * c :
        col = y.index("X")
        ghostrow.add(row+1)
        ghostcol.add(col+1)
        y = y[:col] + "." + y[col+1:]
"""
