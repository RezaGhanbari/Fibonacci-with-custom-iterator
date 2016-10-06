n = int(raw_input())
a, b = map(int, raw_input().split(':'))
while b > 59:
    b -= 10
if 12 == n:
    while a <= 0:
        a += 10
    while a > 12:
        a -= 10
if 24 == n:
    while a >= 24:
        a -= 10
print '%02d:%02d' % (a, b)
