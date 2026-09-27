#import "/book/utils.typ": codeblock

== Caracteres y códigos

`ord` da el número de un carácter y `chr` hace lo contrario. `ord(c) - ord("a")` es la posición de una letra minúscula (`a` $= 0$). `shift` es un cifrado César sobre minúsculas.

#codeblock("/content/strings/ord-chr.py")
