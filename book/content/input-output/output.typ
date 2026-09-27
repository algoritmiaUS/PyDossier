#import "/book/utils.typ": codeblock

== Imprimir

`print` separa sus argumentos con un espacio y termina con un salto de línea; se cambia con `sep=` y `end=`. `f"{x:.2f}"` imprime 2 decimales. Para muchas líneas, guárdalas en una lista e imprímelas de una vez con `"\n".join`.

#codeblock("/content/input-output/output.py")
