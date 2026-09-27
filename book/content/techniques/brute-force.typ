#import "/book/utils.typ": codeblock

== Fuerza bruta

Si $n$ es pequeño, prueba todas las opciones. `permutations` da los $n!$ órdenes, `combinations(v, k)` las formas de elegir `k` elementos y `product(..., repeat=n)` las $2^n$ elecciones de coger o no cada uno.

#codeblock("/content/techniques/brute-force.py")
