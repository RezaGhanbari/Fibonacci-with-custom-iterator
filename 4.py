a = map(int, raw_input().split(' '))
a.sort()
print abs(a[0]-a[1])+abs(a[2]-a[1])

