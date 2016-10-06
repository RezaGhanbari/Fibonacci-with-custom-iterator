I = raw_input
I()
s = map(int, I().split())
a, b, c, d = map(s.count, range(1, 5))
print d + c + (2 * b + max(a - c, 0) + 3) / 4
