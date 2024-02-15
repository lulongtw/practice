for data in range(10):
    x = input().split()
    for i in range(3):
        x[i] = int(x[i])
    t = x[0]
    evnt = x[1]
    day = x[2]
    y = input().split()
    for i in range(evnt):
        y[i] = int(y[i]) - 1
    y.sort()
    total = t
    l = 0
    for i in range(day): 
        if t == 0:
            l+=1
            t = total
        t-=1
        for j in range(len(y)):
            if i == y[j]:
                total+=1
                t+=1
        
    print(l)
