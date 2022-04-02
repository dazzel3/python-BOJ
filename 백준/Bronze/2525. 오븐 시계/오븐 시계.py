h, m = map(int, input().split())
time = int(input())
x = time // 60
time = time % 60
if (m+time) >= 60:
    m = m + time - 60
    if (h + x + 1) >= 24:
        h = h + x + 1 - 24
    else:
        h = h + x + 1
else:
    m = m + time
    if (h+x) >= 24:
        h = h + x - 24
    else:
        h = h + x
print(h, m)