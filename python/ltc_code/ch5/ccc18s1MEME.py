n = int(input())
lst = []
for i in range(n) :
    lst.append(int(input()))
lst.sort()


minn = 9999999999999

for i in range(1,len(lst)) :
    if i > 1 :
        r = l

    l = (lst[i] + lst[i-1]) / 2
    
    if i > 1 :
        ans = l - r 
        if ans < minn :
            minn = ans
print(minn)