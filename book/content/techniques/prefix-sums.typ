#import "/book/utils.typ": codeblock

== Sumas prefijas

`p[i]` es la suma de los `i` primeros elementos. Tras preparar en $O(n)$, `range_sum(p, l, r)` da la suma de `v[l..r]` (ambos incluidos, desde 0) en $O(1)$.

#codeblock("/content/techniques/prefix-sums.py")
