x = input()
y = input()
dic = {}
for i in range(len(x)):
    dic[y[i]] = x[i]

z = input()

ans = ""
for i in range(len(z)):
    if z[i] not in dic:
        dic[z[i]] = "."
    ans += dic[z[i]] 

print(ans)
