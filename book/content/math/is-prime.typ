#import "/book/utils.typ": codeblock

== ¿Es primo?

Solo prueba divisores hasta $sqrt(n)$: $O(sqrt(n))$. `0` y `1` no son primos.

#codeblock("/content/math/is-prime.py")
