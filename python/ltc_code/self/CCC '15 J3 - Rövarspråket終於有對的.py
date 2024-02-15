"""
a   bcd  e   fgh   i   jklmn  o    pqrst   u    vwxyz

遇到每個字母都直接上
遇到子音  接下來的兩個字母
第一個字母 是離該子音最進的母音  如果兩個母音一樣近  就是idx最小的母音
第二個字母 是該子音的下一個子音
j  oy
jikoyuz

ham
hijamon
"""
vowel = ["a","e","i","o","u"]
word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def add1(ltr) :
    distancevol = []
    smalldis = 999999999
    for volw in vowel :
        ans = abs(word.index(volw) - word.index(ltr))
        if ans < smalldis :
            smalldis = ans
        distancevol.append([ans,volw])
    
    for a in range(len(distancevol)) :
        if distancevol[a][0] == smalldis :
            return distancevol[a][1]

def add2(ltr) :
    if ltr == "z" :
        return "z"
    else :
        idx = word.index(ltr) +1
        while True :
            if word[idx] in vowel :
                idx+=1
            else :
                break
        return word[idx]  

x = input()
ans = ""
for i in range(len(x)) :
    if x[i] in vowel :
        ans+=x[i]
    else :
        ans+=x[i]
        first = add1(x[i])
        second = add2(x[i])
        ans = ans + first + second
print(ans)