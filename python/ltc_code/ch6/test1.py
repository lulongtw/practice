cur = [[12, 8], [14, -4], [40, 6], [45, 11]]
hdmnts = 0
holdhand = 5
leave = 50
hold = False
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
            #continue

    if level >= leave :   
        break

    if level >= holdhand and level < leave :
        strthold = time
        hold = True
        
    print(hdmnts)
#print(cur)