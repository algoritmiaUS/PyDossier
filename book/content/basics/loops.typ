#import "/book/utils.typ": codeblock

== Bucles

`for` repite para cada valor; `while` repite mientras se cumpla la condición. `range(a, b, paso)` va desde `a` hasta `b - 1`: `b` no se incluye. `range(n)` es $0, dots, n - 1$. `break` sale del bucle y `continue` salta a la siguiente vuelta.

#codeblock("/content/basics/loops.py")
