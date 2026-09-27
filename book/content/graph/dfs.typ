#import "/book/utils.typ": codeblock

== DFS (alcanzabilidad)

`seen[v]` es `True` si se puede llegar a `v` desde `s`. Usa una pila en vez de recursión para evitar `RecursionError`. $O(n + m)$.

#codeblock("/content/graph/dfs.py")
