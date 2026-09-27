# 🐍 Dossier Python

Dossier para competiciones de programación pensado para gente que **empieza desde cero**. Todo en Python, sin estructuras avanzadas: cómo leer la entrada, cómo imprimir, listas, diccionarios, ordenar, leer un grafo, BFS...

Hecho por **Fernando Giráldez**.

## 📦 Requisitos

| Herramienta | Versión | Para qué |
| ----------- | ------- | -------- |
| `python3` | 3.9+ | Ejecutar snippets y tests (`./scripts/run-tests.sh`) |
| `typst` | 0.15+ | Generar `main.pdf` / `main-dark.pdf` |

## 🚀 Cómo generar el PDF

Sitúate en la raíz del proyecto y ejecuta:

```bash
./scripts/compile-typst.sh light # Tema claro (por defecto, ahorra tóner) -> main.pdf
./scripts/compile-typst.sh dark  # Tema oscuro -> main-dark.pdf
./scripts/compile-typst.sh all   # Ambos
```

## Contribuir

Lee [CONTRIBUTE.md](CONTRIBUTE.md) para la checklist, convenciones y guía paso a paso.

## 📜 Licencia

Al contribuir a este proyecto, aceptas que tus aportes sean publicados bajo los términos de la [Licencia MIT](LICENSE).
