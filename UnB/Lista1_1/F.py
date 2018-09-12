from bisect import bisect_left
def binarySearch(a, x, lo = 0, hi=None):
    hi = hi or len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)
n,x = [int(k) for k in input().split()]
v1 = [int(k) for k in input().split()]
v2 = [int(k) for k in input().split()]
v2 = sorted(v2)
b = 0; found = False;
while not found and b < len(v1):
    search = x - v1[b]
    resp = binarySearch(v2, search)
    if(resp != -1):
        found = True
    b+=1
print("1" if found else "0")