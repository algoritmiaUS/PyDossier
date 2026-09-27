#import "/book/utils.typ": codeblock

== Lista

Secuencia ordenada, con índices de `0` a `len(v) - 1`; `v[-1]` es el último. `v[a:b]` es un trozo de `a` a `b - 1`. `append` y `pop()` son rápidos; `insert(0, x)`, `pop(0)`, `remove`, `in` e `index` recorren toda la lista.

#codeblock("/content/data-structures/list.py")
