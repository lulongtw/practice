n = int(input())
x = input().split()
dic = {}

max = 1
for i in range(n):
    if x[i] not in dic:
        dic[x[i]] = 1
    else :
        dic[x[i]]+=1
        if dic[x[i]] > max:
            max = dic[x[i]]



ans = []
for i in dic :
    if dic[i] == max:
        ans.append(int(i))
ans.sort()
for i in range(len(ans)):
    ans[i] = str(ans[i])
print(" ".join(ans))