for data in range(10) :
    min = 99999999999
    y = []
    ans = []
    n = int(input())

    for i in range(n) :
        x = input().split()
        for j in range(2,len(x)) :
            x[j] = int(x[j])
            if x[j] < min :
                min = x[j]
        s = [int(x[0]),set(x[2:len(x)])]
        y.append(s)
  
    
    for j in range(len(y)) :
        if min in y[j][1] :
            ans.append(y[j][0])
    ans.sort()
    for j in range(len(ans)) :
        ans[j] = str(ans[j])
    ans = "{" + ",".join(ans) + "}"

    print(min,ans)