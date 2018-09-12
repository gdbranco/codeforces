n, k = [int(x) for x in input().split()]
soma = n
while n > k-1:
    soma += n//k
    n = n//k + n%k
print(soma)