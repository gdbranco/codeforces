from bisect import bisect_left
def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    if pos != hi:
        return a[pos]
    else:
        return -1
n, q = map(int, input().split())
v = map(int, input().split())
v = sorted(v)
for i in range(q):
    k = int(input())
    print(binary_search(v, k))