x = input().split()
r = int(x[0])
c = int(x[1])


m = []
for i in range(r):
    y = input() + "."
    pic = []
    for j in range(c+1):
        pic.append(y[j])
    m.append(pic)

m.append(["."]*(c+1))

ret = 0
for i in range(r) :
    for j in range(c):
        if m[i][j]=="*":
            ret+=1
            strtr = i
            strtc = j
            while m[strtr][strtc] == "*":
                strtc+=1

            strtc-=1
            while m[strtr][strtc] == "*":
                strtr+=1
            strtr-=1
            for k in range(i,strtr+1):
                for l in range(j,strtc+1):
                    m[k][l] = "."
print(ret)