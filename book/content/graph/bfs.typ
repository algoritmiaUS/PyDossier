#import "/book/utils.typ": codeblock

== BFS (camino más corto)

Visita los nodos por orden de distancia desde `s`. `dist[v]` es el mínimo número de aristas de `s` a `v`, o $-1$ si no se puede llegar. Solo para grafos sin pesos. $O(n + m)$.

#codeblock("/content/graph/bfs.py")
