t = input()
a = []
ans = []
for i in range(t):
    a.append(map(int, raw_input().split()))
    a[i] = ", ".join(repr(e) for e in a[i])

for x in range(t):
    if (360. / (180 - int(a[x]))) % 1 == 0:
        ans.append("YES")
    else:
        ans.append("NO")

res = [r for r in ans]
for i in range(t):
    print ''.join(res[i])
