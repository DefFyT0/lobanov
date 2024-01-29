f  = open("27_B.txt")
k = 3
n14 = n1 = n7 = n2 = kol = 0
n = int(f.readline())
buf = [0]*k
for i in range(k):
    buf[i] = int(f.readline())
for i in range(k,n):
    out = buf[i%k]
    if out%14==0:
        n14+=1
    if out%2==0:
        n2+=1
    if out%7==0:
        n7+=1
    n1+=1
    elem = int(f.readline())
    if not elem%14:
        kol+=n1
    elif elem%7==0:
        kol+=n2
    elif elem%2==0:
        kol+=n7
    else:
        kol+=n14
    buf[i%k] = elem
print(kol)