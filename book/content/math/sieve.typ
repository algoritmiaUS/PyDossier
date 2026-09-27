#import "/book/utils.typ": codeblock

== Criba de Eratóstenes

`prime[i]` dice si `i` es primo para todo $0 <= i <= n$, con $n >= 1$. Úsala cuando necesites muchos primos.

#codeblock("/content/math/sieve.py")
