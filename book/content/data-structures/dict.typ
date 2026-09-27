#import "/book/utils.typ": codeblock

== Diccionario

Asocia claves con valores y las busca rápido. Leer una clave que no existe con `d[k]` da `KeyError`; usa `d.get(k, por_defecto)`. Las claves deben ser inmutables (números, textos, tuplas).

#codeblock("/content/data-structures/dict.py")
