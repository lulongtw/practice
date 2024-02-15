dic = {1:100,2:500,3:1000,4:5000,5:10000,
       6:25000,7:50000,8:100000,9:500000,10:1000000}

x = int(input())
for i in range(x):
    del dic[int(input())]    


val = sum(list(dic.values()))

ss = int(input())
if val/len(dic) < ss:
    print("deal")
else :
    print("no deal")
