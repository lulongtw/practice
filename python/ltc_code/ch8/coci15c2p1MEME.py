
n = int(input())

lst = []
for i in range(n) :
    lst.append(input())

keyin = input()

dic = {'2': {'c', 'a', 'b'}, 
       '3': {'e', 'd', 'f'},
       '4': {'g', 'h', 'i'},
       '5': {'l', 'k', 'j'}, 
       '6': {'m', 'o', 'n'}, 
       '7': {'s', 'q', 'r', 'p'}, 
       '8': {'u', 't', 'v'}, 
       '9': {'x', 'z', 'w', 'y'}}

for i in range(len(keyin)) :
    for word in lst :
        if word[i] not in dic[keyin[i]] :
            lst.remove(word)

print(len(lst))
  
"""
for i in range(9) :
    done = False
    key = input()
    dic[key] = []
    y = input()
    if y == "@@" :
        continue
    for i in range(len(y)) :
        dic[key].append(y[i])
print(dic)
"""



"""

dic = {'a': '2', 'b': '2', 'c': '2',
                   'd': '3', 'e': '3', 'f': '3',
                   'g': '4', 'h': '4', 'i': '4',
                   'j': '5', 'k': '5', 'l': '5',
                   'm': '6', 'n': '6', 'o': '6',
                   'p': '7', 'q': '7', 'r': '7', 's': '7',
                   't': '8', 'u': '8', 'v': '8',
                   'w': '9', 'x': '9', 'y': '9', 'z': '9'}


n = int(input())
lst = []
for i in range(n):
    lst.append(input())

tar = input()

ans = 0
for l in lst:
    res = ""
    for c in l:
        res += dic[c]
    if res == tar:
        ans+=1
print(ans)
"""

#範例過關 無法過測試 indexerror不知道哪裡有問題  結果是j < len(prs) 沒有設
#題目沒有規定key數字arrey的長度跟給定的n個字串長度是一樣  沒社會outof index

dic = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

x = input()
prs = []
for i in range(len(x)):
    prs.append(int(x[i]))


res = 0
for i in range(len(lst)):
    ans=0
    for j in range(len(lst[i])):       
        if j < len(prs) and lst[i][j] in dic[prs[j]]:
            ans += 1
            #print(lst[i][j],dic[prs[j]])
    if ans == len(lst[i]):
        res+=1
        #print(lst[i])
print(res)

