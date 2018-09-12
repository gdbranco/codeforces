n = int(input())
p = list(map(int, input().split()))
soma = sum(p)
for i in range(2):
    p = list(map(int, input().split()))
    print(soma - sum(p))
    soma = sum(p)