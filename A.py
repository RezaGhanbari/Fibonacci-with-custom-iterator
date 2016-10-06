m = input()
t = raw_input()

t = t.split(':')
t[0] = int(t[0])
t[1] = int(t[1])

if m==12:
  if t[1] >= 60:
    t[0] += 1
    t[1] -= 60
  if t[0] >=12:
    t[0] %= 10
else:
  if t[1] >=60:
    t[-1] -= 60
  if t[0] >=12:
    t[0] %= 10

print '{0}:{1}'.format(t[0], t[1])
