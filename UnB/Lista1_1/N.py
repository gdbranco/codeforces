n = int(input())
nomes = []
d = {}
for i in range(n):
    nomes.append(input())
for idx, nome in enumerate(sorted(nomes)):
    d[nome] = idx
for idx, nome in enumerate(nomes):
    if(idx < len(nomes) - 1):
        print(d[nome], end=" ")
    else:
        print(d[nome])