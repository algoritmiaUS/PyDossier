#import "/book/utils.typ": codeblock

== Pila

El último en entrar es el primero en salir. Es una lista normal: `append` apila, `pop()` quita la cima, `stack[-1]` la mira y `not stack` dice si está vacía. Ejemplo: paréntesis balanceados.

#codeblock("/content/data-structures/stack.py")
