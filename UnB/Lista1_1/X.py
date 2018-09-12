n = input()
v = [int(x) for x in input().split()]
done = False
c = 0
while not done:
    k = 0
    for idx, i in enumerate(v):
        if(i%2==0):
            v[idx] = v[idx]/2
            k+=1
    if(k != len(v)):
        done = True
    else:
        c+=1
print(c)