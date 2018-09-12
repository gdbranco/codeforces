n, k = [int(x) for x in input().split()]
r = True
stack = []
for _ in range(n):
  i, o = [int(x) for x in input().split()]
  while(len(stack) > 0 and i >= stack[-1][1]):
      stack.pop()
  if(len(stack) > 0):
    if(stack[-1][1] < o):
      r = False
  if(len(stack) < k):
    stack.append((i,o))
  else:
    r = False
print("Sim" if r else "Nao")