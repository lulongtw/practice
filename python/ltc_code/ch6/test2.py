s = [194, 194, 200, 147, 996,194,200,996]
rank = [0,0,0,0,0,0,0,0]

pai = s.copy()
for i in range(len(pai)) :
    pai[i] = [pai[i],i]
pai.sort(reverse=True)
#print(s)
#print(pai)
rk = 1
for i in range(len(pai)) :
    if i == 0 :
        pai[i].append(1)

    elif i > 0 and pai[i][0] != pai[i-1][0] :
        pai[i].append(i+1)
        rk = i+1

        
    elif pai[i][0] == pai[i-1][0]:
        pai[i].append(rk)

for i in range(len(pai)) :
    idx = pai[i][1]
    mintz = pai[i][2]
    if mintz > rank[idx] :
        rank[idx] = mintz
print(pai)
print(s)
print(rank)




"""
s = [194, 194, 200, 147, 996]
for i in range(len(s)) :

        s[i] = [s[i],i]
print(s)
s.sort(reverse=True)
print(s)

rank = [0,0,0,0,0]
for i in range(len(s)) :
    rank[s[i][1]] = i+1
print(rank)
"""