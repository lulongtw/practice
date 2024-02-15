dis = input().split()

for i in range(len(dis)) :
    dis[i] = int(dis[i])

def func(di,ii,jj) :
    if jj > ii :
        c1 = ii
        c2 = jj
    else :
        c1 = jj
        c2 = ii
    

    total = 0
    for a in range(c1,c2) :
        total = total + di[a]
    return total



for i in range(len(dis)+1):
    ans = []
    for j in range(len(dis)+1):
        ans.append(str(func(dis,i,j)))
    print(" ".join(ans))


""""""
#新的其實一樣

dis = input().split()

for i in range(len(dis)) :
    dis[i] = int(dis[i])


for i in range(5) :
    ans = [0,0,0,0,0]
    right = ans[i+1:]
    left = ans[:i]

    idx = i
    add = 0
    for j in range(len(right)) :
        add+=dis[idx]
        right[j] = add
        idx+=1

    idx = i - 1
    add = 0
    for j in range(len(left)-1,-1,-1) :
        add+=dis[idx] 
        left[j] = add
        idx-=1

    
    ans = left+[0]+right
    for j in range(len(ans)) :
        ans[j] = str(ans[j])
    print(" ".join(ans))



""""""
x = input().split()

for i in range(len(x)):
    x[i] = int(x[i])

def rght(ii,x,r):
    for j in range(len(r)):
        if j == 0:  #其實可以不用這個if else 因為是怕else的r[j-1]out index 但起始r[-1]不會outofrange
            r[j] = x[ii]
        else:
            r[j] = r[j-1] +x[ii+j]
    return r

def lft(x,l):  #為什麼？？？？？？？？？？right要追蹤但left不用追蹤
    for j in range(len(l)-1,-1,-1):
        if j == len(l)-1:
            l[j] = x[j]
        else:
            l[j] = l[j+1] + x[j]
    return l

for i in range(5):
    ans = [0,0,0,0,0]
    ans[i] = 0
    right = rght(i,x,ans[i+1:])
    left = lft(x,ans[:i])
    ans[i+1:]=right
    ans[:i]=left
    for j in range(len(ans)):
        ans[j] = str(ans[j])
    print(" ".join(ans))