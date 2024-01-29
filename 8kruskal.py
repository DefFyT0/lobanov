f = open("krusk_V3.txt")
n,m = map(int, f.readline().split())
a = []
col = [i for i in range(n)]
for i in range(m):
    b,c,d = map(int,f.readline().split())
    a.append((d,b-1,c-1))
a.sort()
ost = []
res = 0
for i in range(m):
    if col[a[i][1]] != col[a[i][2]]:
        res += a[i][0]
        c1 = col[a[i][1]]
        c2 = col[a[i][2]]
        ost.append((a[i][1]+1, a[i][2]+1))
        for t in range(n):
            if col[t] == c2:
                col[t] = c1

print(res,end=" ")
ost.sort()
for r in ost:
    print("(" + str(r[0]) + " " + str(r[1]) + ")", end="")
