n, m = [int(x) for x in input().split()]
t = []
for k in range(n):
    t.append([int(x) for x in input()])
savex = 0
savey = 0
found = False
for idx, k in enumerate(t):
    for cidx, c in enumerate(k):
        if(c == 1 and savex <= cidx):
            found = True
            savex = cidx
u = list(zip(*t))
for idx, k in enumerate(u):
    for cidx, c in enumerate(k):
        if(c == 1 and savey <= cidx):
            found = True
            savey = cidx
if found:
    menorx = float("inf")
    for l in t:
        if(1 in l):
            if(l.index(1) < menorx):
                menorx = l.index(1)
    menory = float("inf")
    for l in u:
        if (1 in l):
            if(l.index(1) < menory):
                menory = l.index(1)
    savex = min(savex+1, m-menorx)
    savey = min(savey+1, n-menory)
print(f'{savex}x{savey}')