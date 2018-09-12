n = int(input())
s = [int(k) for k in input().split()]
maior = max(s)
a = 0
soma = 0
while a < len(s):
    s[a] -= maior
    soma += abs(s[a])
    a+=1
print(soma)