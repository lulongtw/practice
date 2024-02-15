for data in range(10) :    
    x = input().split()
    r = int(x[1])
    c = int(x[0])

    ans = 0
    grid = []
    for i in range(r) :
        y = input().split()
        for j in range(c) :
            y[j] = int(y[j])
        if sum(y) % 13 == 0 :
            ans += sum(y) // 13
        grid.append(y)



    for i in range(c) :
        summ = 0
        for j in range(r) :
            summ+=grid[j][i]
        if summ % 13 == 0 :
            ans+= summ//13
    print(ans)

