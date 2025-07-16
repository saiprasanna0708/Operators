Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=int(input())
12
>>> b=int(input())
24
>>> print(a>=b and a<=b)
False
>>> print(a<=b or a=b)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(a<=b or a==b)
True
>>> print(a!=b)
True
