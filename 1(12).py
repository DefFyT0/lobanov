'''
f=open("27_A.txt")
n = int(f.readline())
ms = 0
m = [10**20]*61
s = 0
k = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s%61 == 0:
        ms = max(ms,s)
    s1 = s - m[s%61]
    ms = max(ms,s1)
    m[s%61] = min(m[s%61],s)
print(ms)
'''       
def divisor(x):
    dlt=set()
    for d in range(2, int(x**0.5)+1):
        if x%d==0:
            dlt.add(d)
            dlt.add(x//d)
    return sorted(dlt)