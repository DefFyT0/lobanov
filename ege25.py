from fnmatch import fnmatch
for n in range(10**8 + 1):
    if n % 161 == 0 and fnmatch(str(n), "12*4?65"):
        print(n, n//161)