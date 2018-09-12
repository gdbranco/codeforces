buracos = {"0": 1, "6": 1, "9": 1, "8": 2}
a, b = [int(x) for x in input().split()]
maiorb = 0
maiord = float('inf')
for i in range(a, b+1):
    b = 0
    for k in str(i):
        if(k in buracos):
            b += buracos[k]
    if(b > maiorb):
        maiorb = b
        maiord = i
print(maiord if maiord != float("inf") else a)