s = input().lower()
c = input().lower()
import string
a = list(string.ascii_lowercase)
c = list(c)
for _s in s:
    p = a.index(_s)
    print(c[p],end="")