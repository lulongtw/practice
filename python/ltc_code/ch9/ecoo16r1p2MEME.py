"""
想太多
"""

for data in range(10) :
    n = int(input())
    spin = set()
    x = input().split()
    for i in range(n) :
        x[i] = int(x[i])
        spin.add(x[i])
    target = input().split()
    for i in range(5) :
        target[i] = int(target[i])
    
    a = set()
    b = set()
    res = 0
    for i in spin : 
        for math in ["+","x"] : 
            for j in spin : 
                if math == "+" :
                    res = i + j    
                elif math == "x" :
                    res = i * j  
                a.add(res)
    res = 0
    for i in a :
        for math in ["+","x"] :
            for j in spin :
                if math == "+":
                    res = i + j
                elif math == "x":
                    res = i * j
                b.add(res)

    ans = ""
    for i in target :
        if i in b:
            ans+="T"
        else :
            ans+="F"
    print(ans)
