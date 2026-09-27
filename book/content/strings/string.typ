#import "/book/utils.typ": codeblock

== Lo básico de los textos

Los textos (`str`) no se pueden modificar: los métodos devuelven un texto nuevo. Para cambiar caracteres, conviértelo en lista y vuelve a unirlo con `"".join`. `find` devuelve `-1` si no lo encuentra. No construyas un texto largo con `+=` en un bucle: añade a una lista y únela.

#codeblock("/content/strings/string.py")
