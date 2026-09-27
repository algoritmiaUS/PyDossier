#import "/book/utils.typ": codeblock

== Operadores

`/` siempre devuelve un `float`; usa `//` para la división entera (redondea hacia abajo, también con negativos). `%` es el resto. Los enteros nunca se desbordan. `pow(a, b, m)` calcula $a^b mod m$ rápido (típico `m = 10**9 + 7`). `round` redondea los .5 al par: `round(2.5) == 2`. La lógica usa `and` (y), `or` (o), `not` (no).

#codeblock("/content/basics/operators.py")
