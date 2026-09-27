#import "/book/utils.typ": asset

#let dossier(
  university: "",
  team_name: "",
  author: "",
  logos: (),
  date: datetime.today(),
  flipped: false,
  title: "Dossier",
  outline-columns: 3,
  body,
) = {
  set document(title: title, author: author)

  set page(
    margin: 1cm,
    numbering: "1",
    number-align: start,
    flipped: flipped,
  )

  set text(lang: "es", size: 10pt)

  align(center)[
    #v(1fr)
    #grid(
      columns: logos.len(),
      gutter: 4em,
      align: center + horizon,
      ..logos.map(l => image(l, height: 140pt))
    )
    #v(3em)
    #block(text(2em, university))
    #block(text(2.5em, strong(team_name)))
    #v(2em)
    #block(text(1.8em, [Hecho por #author]))
    #v(1fr)
    #let months = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    #block(text(1.5em, [#date.day() de #months.at(date.month() - 1) de #date.year()]))
  ]
  pagebreak()

  set heading(numbering: "1.")
  show math.equation: set text(10pt)

  columns(outline-columns, gutter: 1em)[
    #v(0.5em)
    #outline(title: "Índice", depth: 3, indent: auto)
  ]
  pagebreak()

  body
}
