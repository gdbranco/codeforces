n = input()
n = list(reversed([int(x) for x in input().split()]))
p = n[:]
v = {}
while len(n) > 1:
    p1,p2 = n.pop(), n.pop()
    if(p1 > p2):
        n.append(p1)
        if(p1 not in v):
            v[p1] = 0
        v[p1] += 1
    else:
        n.append(p2)
        if(p2 not in v):
            v[p2] = 0
        v[p2] += 1
for idx, el in enumerate(reversed(p)):
    if idx < len(p):
        end = " "
    else:
        end = ""
    if(el not in v):
        print(0, end = end)
    else:
        print(v[el], end= end)