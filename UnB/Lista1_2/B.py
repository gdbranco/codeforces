from collections import deque
n, t, c = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
s = deque([])
cont = 0
for i in range(n):
    if(len(s) == c):
        s.popleft()
        cont += 1
    if(p[i] > t):
        while(len(s)):
            s.pop()
        continue
    s.append(p[i])
print(cont+1 if len(s) == c else cont)