'''Ever wonder what *all* the imports are? Look no further.
(I suggest using a pager)'''
import gc
from utils import print_file

print("if you're sure . . . ")
print_file(__file__)

r = gc.get_referrers("")
print('the python interpreter has', len(r), 'builtin names '
      '(including those imported by gc and the print_file function '
      'I just imported). they are:')
for i in r:
    print(i, '\n')
