def ansrev(string):
    dic = {"A":"U","T":"A","C":"G","G":"C"}
    ans = ""
    for a in string :
        ans+=dic[a]
    return ans

def rev(string) :
    dic = {"A":"T","T":"A","C":"G","G":"C"}
    ans = ""
    for a in range(len(string)-1,-1,-1) :
        ans+=dic[string[a]]
    return ans

for data in range(5) :
    x = input()
    for j in range(len(x)) :
        if x[j:j+6] == "TATAAT" :
            srch = x[j+10:]
            break


    for i in range(1,len(srch)) :
        end = srch[i:i+6]
        if rev(end) in srch[i+6:]:
            trans = srch[:i]
            break

    print(f"{data+1}: {ansrev(trans)}")


