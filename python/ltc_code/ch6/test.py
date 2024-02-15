"""
d 一部電影   90mins
m keymontes  5個
h 兩種驚嚇程度  >=5   握手
l             >=50  離開
要減少握手次數  一部電影可以遮眼一次  就不會被嚇到
"""
n = int(input())
for i in range(n) :
    x = input().split()
    mnts = int(x[0])
    kmnts = int(x[1])
    holdhand = int(x[2])
    leave = int(x[3])
    lst = []
    for j in range(kmnts) :
        y = input().split()
        y[0] = int(y[0])
        y[1] = int(y[1])
        lst.append(y)

    minht = 9999999999

    for mnt in range(len(lst)) :
        
        cur = lst.copy()
        cur.pop(mnt)

        hold = False
        strthold = 0
        
        hdmnts = 0
        level = 0  

        for k in range(len(cur)) :
            time = cur[k][0]
            level+=cur[k][1]

            if hold :
                hdmnts += time - strthold
            
            if level < holdhand :
                hold = False
                if level < 0 :
                    level = 0
                    continue

            if level >= leave :   
                break

            if level >= holdhand and level < leave :
                strthold = time
                hold = True
            
            if k == len(cur) - 1 and hold:
                hdmnts += mnts - time

        print(hdmnts,minht)
        print(cur)
       # if  hdmnts < minht :
       #     minht = hdmnts 
   # print(minht)
            
