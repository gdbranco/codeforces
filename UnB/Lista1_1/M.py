x = int(input())
x+=1
found = False
while not found:
    k = {}
    c = 0
    for v in str(x):
        if v not in k:
            k[v] = 0
        k[v]+=1
    for t in k.values():
        if t == 1:
            c +=1
    if c == len(str(x)):
        found = True
    x +=1
print(x-1)