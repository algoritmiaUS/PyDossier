#import "/book/utils.typ": codeblock

== Leer un grafo

Un grafo tiene $n$ nodos y $m$ aristas. Lo guardamos como lista de adyacencia: `g[u]` es la lista de vecinos de `u`. En la entrada los nodos suelen ir de $1$ a $n$, así que restamos 1. Si el grafo es dirigido (aristas de un solo sentido), borra la última línea. Un árbol es un grafo conexo con $m = n - 1$.

#codeblock("/content/graph/read-graph.py")
