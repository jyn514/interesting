print("hi there, only using builtins today.")
import builtins

print("whoops, nearly forgot to show you the source")
from utils import print_file
print_file(__file__)

def metastring(message):
    global str  # this is necessary; try it without and see what happens
    class str(str):  # wait, what?
        def __call__(self):  # this runs when an *instance* of a class is called
            print(message, end=' ')
            return type(self).__bases__[0]()  # this is an instance, not a type
    return str  # the class we just created

str = metastring('\n')
for s in "Isn't this crazy? (more like crazy bad; I'd get killed if I did it in production)".split()[::-1]:
    str = metastring(s)

while hasattr(str, '__call__'):
    str = str()
