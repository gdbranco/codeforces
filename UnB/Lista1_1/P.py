N, A = map(int, input().split())
N = N%500
print("Sim" if A > N else "Nao")