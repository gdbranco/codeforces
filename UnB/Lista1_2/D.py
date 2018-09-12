s = list(range(1, int(input()) + 1))
l = []
while (len(s) > 1):
    l.append(s[0])
    s = s[1:]
    s.append(s[0])
    s = s[1:]
print(" ".join(map(str, l)))
print("".join(map(str, s)))