def check(mail) :
    mail = mail.lower()
    midx = mail.index("@")
    ans = ""

    for letter in mail[:midx]:
        if letter not in [".","+"] :
            ans+=letter
        else :
            if letter == "+" :
                break
    return (ans+mail[midx:])

for data in range(10) :
    n = int(input())
    dfnmail = set()
    for i in range(n) :
        dfnmail.add(check(input()))
    print(len(dfnmail))




""""""

def unique(x):
    x = x.lower()
    atidx = x.index("@")
    new = ""
    for i in range(atidx):
        if x[i] == "+":
            break
        if x[i] != ".":
            new += x[i]

    x = new + x[atidx:]
    return x


for data in range(10):
    unkmail = set()
    n = int(input())
    for i in range(n):
        unkmail.add(unique(input()))
    print(len(unkmail))
