#import "/book/utils.typ": codeblock

== BFS en una cuadrícula

Cada celda es un nodo unido a sus 4 vecinas; `'#'` es una pared. `dist[r][c]` es el mínimo número de pasos desde `(sr, sc)`, o $-1$ si no se puede llegar.

#codeblock("/content/graph/grid-bfs.py")
