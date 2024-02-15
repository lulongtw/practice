n = int(input())
a = set()
total = []
half = 0
for i in range(n) :
    ax = int(input())
    if ax <= 1440 :
        half+=1
    a.add(ax)
    total.append(ax)

m = int(input())
b = set()
for i in range(m) :
    bx = int(input())
    if bx <= 1440 :
        half+=1
    b.add(bx)
    total.append(bx)


total.sort()
lead = ""
ans = 0
times = 0
for i in range(len(total)) :
    if times < 0 :
        lead = "b"
    elif times > 0 :
            lead = "a"
    if total[i] in a :
        times+=1
        if times == 1 and lead == "b":
            ans+=1
            lead = "a"
    elif total[i] in b :
        times-=1
        if times == -1  and lead == "a":
            ans+=1
            lead = "b"
    
print(half,ans)


"""
a = []
b = []
ap = 0
bp = 0
all = []
count = 0
total = []

x = int(input())
for i in range(x):
    app = int(input())
    if app <= 1440 :
        count += 1
    a.append(app)
    total.append(app)
    
y = int(input())
for i in range(y):
    bpp = int(input())
    if bpp <= 1440 :
        count +=1
    b.append(bpp)
    total.append(bpp)


total.sort()
lead = ""
ta = 0
for i in (total):
    if i in a:
        ap+=1
    if i in b:
        bp+=1
    if lead == "a" and bp>ap :
        ta+=1
    if lead == "b" and ap>bp :
        ta+=1
    if ap>bp :
        lead = "a"
    if bp>ap :
        lead = "b"
print(count)
print(ta)

"""