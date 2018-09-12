n = int(input())
f0 = 1
f1 = 1
if(n == 0):
    print(0)
elif(n == 1 or n == 2):
    print(1)
else:
    n-=2
    while n:
        f1, f0 = f0+f1, f1
        n-=1
    print(f1)