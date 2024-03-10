def isPrime(x):
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False 
        d += 1
    return True
d = []

for x in range(50):
    for y in range(50):
        if x + y >= 44:
            s = "0" + x*"1" + y*"2"
            sm1 = sum(map(int,s))
            while "01" in s or "02" in s:
                s = s.replace("02", "1110", 1)
                s = s.replace("01", "220", 1)
            sm = sum(map(int,s))
            if isPrime(sm):
                d.append(sm1)

print(min(d),d)
        
        