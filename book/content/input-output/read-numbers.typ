#import "/book/utils.typ": codeblock

== Leer números

`input()` lee una línea entera como texto. `.split()` la corta por los espacios y `map(int, ...)` convierte cada trozo en entero. Cada `input()` consume exactamente una línea.

#codeblock("/content/input-output/read-numbers.py")
