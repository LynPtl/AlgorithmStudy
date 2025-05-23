#----------------------------------------------------#
#双索引遍历找最大子串
#该题有一个特殊要求，如果有重复相邻数字只记一次
#----------------------------------------------------#
L = [3,8,2,5,7,1,0,7,4,8,3,3,7,8,8]
#L = [1,4,4,1,2,4,3,5,4,0]
result = [[3,8],[2,5,7],[1],[0,7],[4,8],[3,7,8]]

r = []
if not L:
    r = []

current = L[0]
curarr = [current]

for i in range(1,len(L)): 
    if L[i] < current:
        r.append(curarr)
        curarr = [L[i]]
    elif L[i]==current:
        pass
    else:
        curarr.append(L[i])
    current = L[i]
r.append(curarr)
'''
pre = L[0]
sublist = [pre]
for cur in L[1:]:
    if pre > cur:
        r.append(sublist)
        sublist = [cur]
    elif pre == cur:
        pass
    else:
        sublist.append(cur)
    pre = cur
r.append(sublist)
'''
print(r)
