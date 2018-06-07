from importlib._bootstrap_external import SourceLoader
from utils import print_file

print("hi there, let me show you what's going on real quick:")
print_file(__file__)

try:
    print(function)
except NameError as e:
    print(e, "but don't worry, we expected that")

print(type(lambda: None))
print('hold on a sec')
function = type(lambda: None)

loader = SourceLoader()

script = 'print("Hello, world!")'
code = loader.source_to_code(script, '<I just made this file up')
try:
    function(code, {})()
except NameError as e:
    print(e, "D:")

function(code, {'print': print})()
print(':D')
