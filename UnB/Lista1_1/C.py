n = int(input())
p = list(map(int, input().split()))
maior = p[0] - p[1]
for i in range(1, n-1):
    teste = max([p[i] - p[i+1], p[i] - p[i-1]])
    if(teste > maior):
        maior = teste
teste = p[-1] - p[-2]
if(teste > maior):
    maior = teste
print(maior)