n, a, b = map(int, input().split())
_a = list(map(int,input().split()))
_b = list(map(int,input().split()))
erro = [abs((_a[i] - _b[i])) for i in range(n)]
for i in range(a+b):
    erro.sort()
    erro[-1] = abs(erro[-1]-1)
print(sum([e**2 for e in erro]))