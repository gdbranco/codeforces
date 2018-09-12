from math import sqrt
n = int("".join(input().split()))
print("Nao" if (sqrt(n) - int(sqrt(n)) != 0) else "Sim")