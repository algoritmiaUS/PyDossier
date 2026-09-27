#import "/book/utils.typ": codeblock

== Cola

El primero en entrar es el primero en salir. Usa `deque`: `popleft` es rápido, mientras que `list.pop(0)` es lento.

#codeblock("/content/data-structures/queue.py")
