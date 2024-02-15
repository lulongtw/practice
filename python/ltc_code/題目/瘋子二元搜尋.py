

def binary(lst,x) :
    hi = len(lst)
    lo = 0
    while hi > lo :
        mid = (hi + lo) // 2
        if x > lst[mid] :  #觀察 > 和 >=的差別  這個敘述下 如果 是x大 必須網右 
            lo = mid + 1   #但 要注意 如果把=放進來  在等於的情況下 也會網右找  變成 333333這情況 會找最右邊的
        else :
            hi = mid
    return lo


list = [2, 2, 3, 3, 3, 4, 4]
a = 3

print(binary(list,a))


def kk(zz,x) :
    hi = len(zz)
    lo = 0
    while lo < hi :
        mid = (hi + lo) // 2
        if x <= zz[mid] :
            hi = mid
        else :
            lo = mid + 1
    return hi


list = [2, 2, 3, 3, 3, 4, 4]
a = 3

print(kk(list,a))

"""
def binr(lst,hgt) :
    hi = len(lst)
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < hgt:
            lo = mid +1
        else:
            hi = mid 
    return lo

def fal(lst,hgt) :
    hi = len(lst)
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] >= hgt:   #一樣都是二分法 但是遇到數值一樣時 決定要往左還往右 這個在一樣的情形下決定網左是正確的
            hi = mid          #因為要找最右邊而不是最左邊的位置  
        else:
            lo = mid + 1
    return lo

#       0  1  2  3  4  5  6
list = [1, 2, 3, 4, 5, 6, 7]
a = 3

print(binr(list,a))
print(fal(list,a))
 
"""
"""        
def inr(lst,hgt) :
    hi = len(lst)#7
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2 #3
        if lst[mid] < hgt:  
            lo = mid + 1
        else:
            hi = mid
    return lo
"""
"""
下面是東漏東補西漏西捕的方法
思考邏輯是用while找idx可以讓
hgt >= lst[idx-1] and hgt <= lst[idx]
將index0,-1排除在搜尋範圍外防止出圈
然後東漏西捕變這麼長
然後過了測驗不知道錯在哪邊幹
"""

"""
def binr(lst,hgt) :
    if hgt <= lst[0] :
        return 0
    elif hgt > lst[-1] :
        return len(lst)
    elif hgt == lst[-1] :
        idx = len(lst)-1
    
    else :
        done = False
        idx = len(lst) // 2 #2
        while  not done :
            if hgt >= lst[idx-1] and hgt <= lst[idx] : #6>lst[2] and 6<=lst[3]
                done = True
            else :
                le = lst[:idx+1] #[:3] [1,3,5]
                ri = lst[idx+1:] #[3:] [7,9]
                for i in [le,ri] :
                    if hgt >= i[0] and hgt <= i[-1]:
                        if i == le :
                            if len(le)//2 < 1 :
                                len(le) == 2
                            idx = idx - len(le)//2

                        else :         
                            if len(ri)//2 < 1 :
                                len(ri) == 2
                            idx = idx + len(ri)//2
                    elif hgt >= le[-1] and hgt <= ri[0] :
                        idx+=1
                        #print("in",idx)
                        done = True
                        break
    if hgt == lst[idx-1]:
        return idx-1
    else :
        return idx
    

print(binr([1, 2, 3, 3, 3, 3, 4],99))
          # 0 1 2 3 4
#print(binr([2, 2, 3, 3, 3, 4, 4],0))
#print(binr([2, 2, 3, 3, 3, 4, 4],3))
"""