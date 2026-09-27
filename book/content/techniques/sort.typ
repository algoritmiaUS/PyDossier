#import "/book/utils.typ": codeblock

== Ordenar

`v.sort()` cambia `v`; `sorted(v)` devuelve una lista nueva. $O(n log n)$. Las tuplas se ordenan por el primer elemento y, si empatan, por el segundo. `key` dice qué comparar; pon un número en negativo para ordenarlo de mayor a menor.

#codeblock("/content/techniques/sort.py")
