h, m = map(int, input().split())
if (m - 45) < 0:
    m = m - 45 + 60
    if (h-1 < 0):
        h = h - 1 + 24
    else:
        h = h - 1
    print(h, m)
else:
    print(h, m-45)