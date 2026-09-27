#let asset(name) = "/assets/" + name

#let themes = (
  light: (
    bg: none,
    fg: rgb("#383a42"),
    file: "/assets/one-light.tmTheme",
    stroke: luma(200) + 1pt,
    title-bg: luma(245),
  ),
  dark: (
    bg: rgb("#2B303B"),
    fg: rgb("#abb2bf"),
    file: "/assets/one-dark.tmTheme",
    stroke: rgb("#5c6370") + 1pt,
    title-bg: rgb("#1e2229"),
  ),
)

#let get-theme() = {
  let theme-name = sys.inputs.at("theme", default: "light")
  assert(theme-name in themes.keys(), message: "Unknown theme. Use 'light' or 'dark'.")
  themes.at(theme-name)
}

#let _theme = get-theme()
#let _theme-data = read(_theme.file, encoding: none)

#let frame(title: none, cfg: _theme, body) = {
  let radius = 4pt

  block(stroke: cfg.stroke, radius: radius, clip: true, width: 100%)[
    #if title != none {
      block(
        width: 100%,
        stroke: (bottom: cfg.stroke),
        inset: 0.5em,
        below: 0pt,
        sticky: true,
        fill: cfg.title-bg,
        text(fill: cfg.fg, weight: "bold", title.split("/").last(default: title)),
      )
    }
    #block(
      width: 100%,
      inset: 0.5em,
      fill: cfg.bg,
      body,
    )
  ]
}

#let codeblock(file_path, lang: "python") = {
  assert(file_path.len() > 0, message: "codeblock: empty path")
  frame(title: file_path, cfg: _theme)[
    #set text(fill: _theme.fg)
    #raw(read(file_path), lang: lang, block: true, theme: _theme-data)
  ]
}

