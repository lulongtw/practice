
"""
ace,jack,queen,king 很嗨
ace  deck最少還剩4張 這4張內不嗨 則+4
king  deck最少還剩3張 這3張內不嗨 則+3
queen deck最少還剩2張 這4張內不嗨 則+2
jack  deck最少還剩1張 這4張內不嗨 則+1

"""

#this is good shit

deck = []
for i in range(1,53) :
    deck.append(input())

deck.insert(0,0)
high = {"ace","jack","queen","king"}

def pointornot(idx,deckk,curcard) :
    if (curcard == "ace" and 52-idx >= 4 and 
    len(high.intersection(set(deckk[idx+1:idx+5]))) == 0):
        return 4
    elif (curcard == "king" and 52-idx >= 3 and 
    len(high.intersection(set(deckk[idx+1:idx+4]))) == 0):
        return 3
    elif (curcard == "queen" and 52-idx >= 2 and 
    len(high.intersection(set(deckk[idx+1:idx+3]))) == 0):
        return 2
    elif (curcard == "jack" and 52-idx >= 1 and 
    len(high.intersection(set(deckk[idx+1:idx+2]))) == 0):
        return 1
    else :
        return 0
        

ap = 0
bp = 0
for i in range(1,len(deck)) :

    if deck[i] in high :
        pornot = pointornot(i,deck,deck[i])
        if pornot:
            if i % 2 == 1 :
                player = "A"
                ap+=pornot
            else :
                player = "B"
                bp+=pornot
            print(f"Player {player} scores {pornot} point(s).")
print(f"Player A: {ap} point(s).")
print(f"Player B: {bp} point(s).")







"""
下面註解部分可以用 但搞成func有問題
"""
#有問題懶得抗

x = []
high = ["ace","jack","queen","king"]
def inornot(ca) :
    if ca not in high:
        return True
    else:
        return False

for i in range(52):  
    x.append(input())  
ap = 0
bp = 0

def routine(high,ii,points,app,bpp):
    addornot = True
    for j in range(ii+1,ii+1+points):
        if j > 51:
            addornot = False
            break
        if x[j] in high:
            addornot = False
        if addornot:
            if ii%2 == 0:
                app+=points
                return[addornot,"A",app,]
            else:
                bpp+=points
                return[addornot,"B",bpp]
    
dic = {"jack":1,"queen":2,"king":3,"ace":4}

for i in range(len(x)):
    for k in dic:
        if x[i] == k:
            ans = routine(high,i,dic[k],ap,bp)
            if ans[0]:
                print(i,f"Player {ans[1]} scores {dic[k]} point(s).")


"""
以下可以用 我想弄成上面的function 但有問題

for i in range(len(x)):
    if x[i] == "ace":
        addornot = True
        for j in range(i+1,i+5):
            if j > len(x) -1:
                addornot = False
                break
            if inornot(x[j]) == False:
                addornot = False
        if addornot:
            if i%2 == 0:
                ap+=4
                print("Player A scores 4 point(s).")
            else:
                bp+=4
                print("Player B scores 4 point(s).")
    if x[i] == "jack":
        addornot = True
        for j in range(i+1,i+2):
            if j > len(x) -1:
                addornot = False
                break
            if inornot(x[j]) == False:
                addornot = False
        if addornot:
            if i%2 == 0:
                ap+=1
                print("Player A scores 1 point(s).")
            else:
                bp+=1
                print("Player B scores 1 point(s).")
    if x[i] == "queen":
        addornot = True
        for j in range(i+1,i+3):
            if j > len(x) -1:
                addornot = False
                break
            if inornot(x[j]) == False:
                addornot = False
        if addornot:
            if i%2 == 0:
                ap+=2
                print("Player A scores 2 point(s).")
            else:
                bp+=2
                print("Player B scores 2 point(s).")
    if x[i] == "king":
        addornot = True
        for j in range(i+1,i+4):
            if j > len(x) -1:
                addornot = False
                break
            if inornot(x[j]) == False:
                addornot = False
        if addornot:
            if i%2 == 0:
                ap+=3
                print("Player A scores 3 point(s).")
            else:
                bp+=3
                print("Player B scores 3 point(s).")
print(f"Player A: {ap} point(s).")
print(f"Player B: {bp} point(s).")

"""