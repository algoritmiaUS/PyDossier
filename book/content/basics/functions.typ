#import "/book/utils.typ": codeblock

== Funciones

Defínelas con `def` antes de llamarlas. `return` puede devolver varios valores a la vez (una tupla). La recursión está limitada a unos 1000 niveles: mejor usa bucles, o añade `sys.setrecursionlimit(10**6)` después de `import sys`.

#codeblock("/content/basics/functions.py")
