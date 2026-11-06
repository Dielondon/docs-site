# docs-site

La documentación de Pocket Timer, un timer de línea de comandos (inventado), en Markdown. Aquí la
fábrica no produce código sino documentación: el "test" revisa que cada link y cada ancla existan.
Es el repo extra del taller "Software factories with Claude Code", para quien quiera ver el patrón
fuera del código.

## Preparar (antes del taller)

Necesitas Python 3.10 o más nuevo (`python3 --version`).

```zsh
gh repo fork sgomezahumada/docs-site --clone && cd docs-site
python3 tools/check_links.py         # "0 broken link(s)"
./doctor.sh                          # hasta que diga "doctor: all green"
```

## En el taller

```zsh
./factory.sh 1       # el ticket #1 entra, sale un PR (o un PR [REJECTED])
```

Este repo trae un gate: `gates/no-external-links.sh` detiene links fuera de `docs/`. El ticket #3
está pensado para chocar con él. Y trae sus propios prompts (`prompts/2-build.md` a `4-review.md`):
mira cómo cambian las fases cuando lo que se produce es documentación.

## Tus gates

Lee [`gates/README.md`](gates/README.md): las reglas y cuatro ejemplos para copiar y adaptar.

Idea para el Tier 1: agrega a `AGENTS.md` la regla "no links fuera de `docs/`" y mira si el ticket #3
termina distinto: ¿lo frena el agente o lo frena el gate?
