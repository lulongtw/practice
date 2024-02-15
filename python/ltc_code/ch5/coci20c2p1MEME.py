n = int(input())
x =input()

grid = []
for i in range(n*2) :
    grid.append(["."]*n)

"""
如果上一個是+且目前不是- 就往上
如果上一個不是＋且目前是-  就往下
"""

r = n
for i in range(n) :

    if i != 0 and x[i-1] == "+" and x[i] != "-" :
        r-=1
    elif i != 0 and x[i-1] != "+" and x[i] == "-" :
        r+=1

    if x[i] == "+" :
        grid[r][i] = "/"
    elif x[i] == "-" :
        grid[r][i] = "\\"
    elif x[i] == "=" :
        grid[r][i] = "_"
 

for i in range(len(grid)) :
    if grid[i] != ["."] * n :
        print("".join(grid[i]))



"""
#舊!醜！還沒改條件 所以還是錯的
x = int(input())
y = input()

m = []
mm = []
for i in range(x*2):
    m.append(["."]*x)

def upornotto():
    uon = []
    pic = []
    for i in range(x):
        if y[i] == "+":
            pic.append("/")
        elif y[i] == "=":
            pic.append("_")
        else:
            pic.append("\\")
        if i == 0:
            uon.append(0)
        else :
            if (y[i]=="+"or y[i]=="=") and y[i-1]== "+":
                uon.append(1)              
            elif y[i]=="-" and y[i-1]=="-":
                uon.append(-1)
            else:
                uon.append(0) 
    return [uon,pic]


uodandpic = upornotto()

uon = uodandpic[0]
pic = uodandpic[1]

s=x-1
for i in range(x):    
    s=s-uon[i]
    m[s][i]=pic[i]

for i in range(len(m)):
    if m[i]!=["."]*x:
        ans = "".join(m[i])
        print(ans)
"""

