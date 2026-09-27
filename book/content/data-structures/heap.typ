#import "/book/utils.typ": codeblock

== Montículo (cola de prioridad)

Da el menor elemento rápido: `h[0]` lo mira y `heappop` lo saca. Para el mayor, mete los valores en negativo. Las tuplas se comparan por el primer elemento y, si empatan, por el segundo.

#codeblock("/content/data-structures/heap.py")
