n, x = map(int, input().split())
v = list(map(int, input().split()))
found = False
if( x <= sorted(v)[-1]):
    while not found:
        if(x in v):
            found = True
        else:
            x+=1
    if found:
        idx = v.index(x)
        while idx < len(v) and x <= v[idx]:
            idx +=1
        print(idx)
else:
    print(-1)