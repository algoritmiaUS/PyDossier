#import "/book/utils.typ": codeblock

== Palíndromo

`s[::-1]` es `s` al revés. Distingue mayúsculas: usa antes `s.lower()` si hace falta.

#codeblock("/content/strings/palindrome.py")
