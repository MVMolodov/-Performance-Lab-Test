n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
nrow = []
mrow = []
for i in range(n):
    nrow.insert(len(nrow),i + 1)
c = 0
for i in range(m):
    mrow.insert(len(mrow),nrow[c])
    c += 1
    if c == n:
        c = c - n
#print(mrow)
res = [1]
k = 1
c = m
while mrow[m-1] != 1:
    c = c - 1
    for j in range(m):
        if c < n:
             mrow[j] = nrow[c]
             c += 1
        else:
            c = c - n
            mrow[j] = nrow[c]
            c += 1
    #print(mrow)
    res.insert(k,mrow[0])
    k += 1
resstr = "".join(map(str, res))
print(resstr)