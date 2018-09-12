n, a, b = [int(x) for x in input().split()]
s = 0
for i in range(n+1):
    k = 0
    for l in str(i):
        k += int(l)
    if(k >= a and k <= b):
        s += i
print(s)