def isPrime(x):
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False 
        d += 1
    return True

def deli(n):
    d=set()
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            d.add(i)
            d.add(n//i)
    return sorted(d)

d = []
for i in range(25317, 51237):
    d = deli(i)
    d = [j for j in d if isPrime(j)]
    if len(d) >= 6:
        print(i, max(d), end="; ")

