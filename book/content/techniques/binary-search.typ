#import "/book/utils.typ": codeblock

== Búsqueda binaria

`v` debe estar ordenada. `bisect_left(v, x)` es la primera posición con `v[i] >= x` y `bisect_right(v, x)` la primera con `v[i] > x`. $O(log n)$. `count_between` cuenta los valores en $[l o, h i]$ y necesita $l o <= h i$.

#codeblock("/content/techniques/binary-search.py")
