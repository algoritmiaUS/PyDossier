== Errores comunes

#table(
  columns: 2,
  [*Error*], [*Causa habitual*],
  [`IndentationError`], [Espacios mal puestos, falta sangría tras `:`],
  [`NameError`], [Nombre mal escrito, o usado antes de asignarlo],
  [`TypeError`], [`"a" + 1`: usa `str(1)` o un f-string],
  [`ValueError`], [`int("3 4")`: falta el `.split()`],
  [`IndexError`], [`v[len(v)]`: los índices válidos son $0..n-1$],
  [`KeyError`], [Clave que no está en el dict: usa `d.get(k, 0)`],
  [`ZeroDivisionError`], [Dividir o hacer `%` entre cero],
  [`RecursionError`], [Recursión demasiado profunda: usa un bucle],
  [`EOFError`], [Más `input()` que líneas tiene la entrada],
  [Time limit], [Lectura lenta o demasiadas operaciones],
  [Wrong answer], [Formato de salida, espacios, casos límite],
)
