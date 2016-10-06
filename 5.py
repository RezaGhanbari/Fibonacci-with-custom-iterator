import re
from StringIO import StringIO

n = input()
a = raw_input()
print re.findall(r'\(.*_?\)', a)
