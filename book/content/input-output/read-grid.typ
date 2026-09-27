#import "/book/utils.typ": codeblock

== Leer una cuadrícula de caracteres

`grid[r][c]` es la fila `r`, columna `c`, empezando ambas en 0. Los textos no se pueden modificar: usa `[list(input().strip()) for _ in range(n)]` si necesitas cambiar celdas.

#codeblock("/content/input-output/read-grid.py")
