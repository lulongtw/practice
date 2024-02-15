
cost = [12,10,7,5]

for data in range(10) :
    tar = int(input()) * 2
    per = input().split()
    for i in range(4) :
        per[i] = float(per[i])
    highidx = per.index(max(per))
    nums = int(input())
    
    res = 0
    for i in range(len(per)) :
        per[i] = per[i] * nums
        if per[i] != int(per[i]) :
            res+= (per[i] - int(per[i])) 
        per[i] = int(per[i]) * cost[i]
    per[highidx] = per[highidx] + (res * cost[highidx])
    
    if sum(per) >= tar :
        print("NO")
    else :
        print("YES")

    
    
    
