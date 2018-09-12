n = int(input())
v = map(int, input().split())
v = set(sorted(v, reverse=True))
print(len(v))