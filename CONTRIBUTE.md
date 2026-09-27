# Contribuir a PyDossier

Guía mínima para añadir temas. Ver también [README.md](README.md).

El público son personas que **no saben programar**. Si un tema necesita más de un párrafo para explicarse (segment tree, DSU, DP avanzada...), no va aquí

## TL;DR

- [ ] `content/<categoria>/<nombre>.py` — kebab-case, código legible (nombres claros, 4 espacios), sin comentarios
- [ ] `book/content/<categoria>/<nombre>.typ` — fragmento con `#codeblock("/content/...")`, registrado con `#include` en `book/content/<categoria>.typ` (no toques `book/python.typ`)
- [ ] `tests/unit/<nombre>.py` obligatorio, `tests/stress/<nombre>.py` si aplica
- [ ] `./scripts/compile-py.sh && ./scripts/run-tests.sh && ./scripts/check-names.sh && ./scripts/compile-typst.sh all`
- [ ] PR a `main` — CI en `.github/workflows/pr-check.yml` debe pasar

## Estructura

```
content/           # un archivo = un tema
book/content/      # un .typ agregador por categoría + un fragmento .typ por tema en <categoria>/
scripts/           # compile-py.sh, run-tests.sh, check-names.sh, compile-typst.sh
tests/unit/ tests/stress/ tests/support/
```

El orden lo define el agregador `book/content/<categoria>.typ` con sus líneas `#include`.

## Añadir un tema

1. **Crear** `content/<categoria>/<nombre>.py`. Puede ser un script que lee de la entrada (`read-graph.py`) o definir funciones (`bfs.py`).
2. **Registrar**:
   - Crear `book/content/<categoria>/<nombre>.typ`:

    ```typ
    #import "/book/utils.typ": codeblock

    == BFS (camino más corto)

    `dist[v]` es el mínimo número de aristas de `s` a `v`, o $-1$ si no se puede llegar.

    #codeblock("/content/graph/bfs.py")
    ```

   El texto va en español y explica lo que un principiante necesita: qué hace, rangos, precondiciones, errores típicos.

   - Añadir `#include "<categoria>/<nombre>.typ"` en `book/content/<categoria>.typ`.

3. **Tests** — mismo stem que en `content/` (`bfs.py` → `tests/unit/bfs.py`). Cargan el snippet con `tests.support.run.run(path, stdin)`, que devuelve `(variables, salida)`:

    ```python
    from tests.support.run import run

    bfs = run("content/graph/bfs.py")[0]["bfs"]
    assert bfs([[1], [0]], 0) == [0, 1]
    ```

   - Unit: determinista + casos borde
   - Stress: aleatorio contra una implementación ingenua

## Checks locales

```bash
./scripts/compile-py.sh
./scripts/run-tests.sh [tests...]   # sin argumentos corre todos
./scripts/check-names.sh
./scripts/compile-typst.sh all      # falla si el PDF supera 25 páginas
```

## Convenciones

- **kebab-case** en todas las rutas salvo dotfiles y `README.md`, `LICENSE`, `AGENTS.md`, `CONTRIBUTE.md`.
- Los módulos de `tests/support/` deben ser una sola palabra para poder importarse (`run.py`, `graphs.py`).
- Imports absolutos desde la raíz (`from tests.support.run import run`); los tests se ejecutan con `python3 -m tests.unit.<nombre>` desde la raíz.
