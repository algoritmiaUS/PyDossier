#import "/book/utils.typ": codeblock

== Lista 2D (matriz)

Nunca la crees con `[[0] * m] * n`: todas las filas son la misma lista, y al cambiar una cambian todas.

#codeblock("/content/data-structures/list-2d.py")
