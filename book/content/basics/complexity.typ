== Complejidad según $n$

Python hace unas $10^7$ operaciones simples por segundo (PyPy unas 10 veces más):

#table(
  columns: 3,
  [*$n$ máximo*], [*Complejidad*], [*Idea típica*],
  [$n <= 10$], [$O(n!)$], [Todas las permutaciones],
  [$n <= 20$], [$O(2^n)$], [Todos los subconjuntos],
  [$n <= 200$], [$O(n^3)$], [Tres bucles anidados],
  [$n <= 3 dot 10^3$], [$O(n^2)$], [Dos bucles anidados],
  [$n <= 2 dot 10^5$], [$O(n log n)$], [Ordenar, búsqueda binaria],
  [$n <= 10^6$], [$O(n)$], [Un bucle, sumas prefijas],
  [$n <= 10^12$], [$O(sqrt(n))$], [Divisores, primalidad],
  [$n > 10^12$], [$O(log n)$ o $O(1)$], [Fórmula matemática],
)
