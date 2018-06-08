'''see also: https://github.com/python/cpython/blob/master/Lib/test/crashers
as well as https://wiki.python.org/moin/CrashingPython'''

import sys
from utils import print_file

print('oh come on, you knew running this was a bad idea')
print_file(__file__)

def recurse(n=0):
    if n == 0:
        print("yup, that's 0 alright")
        return
    recurse(n - 1)

try:
    recurse(1000)
except RecursionError as e:
    print(e)
    print("Really? that wasn't even that big!")
    print("ok let's do this for real")

# found this from trial and error, I think print calls some built-in functions?
overhead = 5
sys.setrecursionlimit(1000 + overhead)
recurse(1000)
print("that's what I'm talking about")

print("how high can we go?")
for i in range(10):
    current = 10 ** i
    print('trying', current)
    sys.setrecursionlimit(current + overhead)
    recurse(current)
