#import "/book/template.typ": dossier
#import "/book/utils.typ": asset

#show: dossier.with(
  university: "Universidad de Sevilla",
  team_name: "SQLito",
  logos: (asset("us.png"), asset("caus.png")),
  author: "Fernando Giráldez",
  date: datetime.today(),
  flipped: true,
  title: "Dossier Python",
)

#show raw.where(block: true): set text(
  font: "JetBrains Mono",
  ligatures: false,
  features: (calt: 0),
  size: 10pt,
)

#include "/book/python.typ"

#context [#metadata(counter(page).get().first()) <end>]
