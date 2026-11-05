---
layout: default
title: ow.screen
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.screen

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.screen.js) · [Baseline](../source-snapshot.md)

### ow.screen.align

`ow.screen.align(aText, aWidth, aAlign, aFillChar, aFillStyle) : String`

````text
Aligns multi-line text ("left", "center", or "right") to aWidth visible columns per line.
````

### ow.screen.alignLine

`ow.screen.alignLine(aText, aWidth, aAlign, aFillChar, aFillStyle) : String`

````text
Aligns a single line of text ("left", "center", or "right") within aWidth visible columns, clipping if longer and padding with aFillChar (optionally styled with aFillStyle). Full UTF-8 wide characters and ANSI sequences are preserved accurately.
````

### ow.screen.borderChars

`ow.screen.borderChars(aStyle, aUnicode) : Map`

````text
Returns the box-drawing characters for aStyle ("rounded", "single", "double", "heavy", "ascii", "none"). Automatically falls back to "ascii" when aUnicode is false.
````

### ow.screen.box

`ow.screen.box(aContent, aOptions) : String`

````text
Renders a bordered box/panel around aContent (string or array of lines). Options: width, height, title, titleAlign ("left", "center", "right"), footer, footerAlign, align ("left", "center", "right"), padding (number or {top,bottom,left,right}), borderStyle ("rounded", "single", "double", "heavy", "ascii", "none"), borderColor/borderStyleSpec, titleStyle, style.
````

### ow.screen.capabilities

`ow.screen.capabilities(aOptions) : Map`

````text
Detects terminal capabilities including colorMode ("none", "16", "256", "truecolor"), colorDepth, unicode support, width, and height. Respects NO_COLOR, FORCE_COLOR, COLORTERM, and TERM.
````

### ow.screen.clip

`ow.screen.clip(aText, aWidth, aEllipsis) : String`

````text
Clips aText to at most aWidth visible columns without splitting UTF-8 grapheme clusters or ANSI escapes.
````

### ow.screen.colorSeq

`ow.screen.colorSeq(aSpec, isBackground, aColorMode) : String`

````text
Returns the SGR parameter sequence (e.g. "38;2;80;180;255" or "38;5;39" or "36") for a color specification given the target colorMode ("truecolor", "256", "16", "none").
````

### ow.screen.configure

`ow.screen.configure(aOptions) : ow.screen`

````text
Configures default screen options (theme, colorMode, unicode, borderStyle, align, spacing, padding, etc.).
````

### ow.screen.getTheme

`ow.screen.getTheme(aTheme, aColorMode, aOverrides) : Map`

````text
Returns a resolved TUI theme map for the given theme name ("default", "ocean", "light", "monochrome") or custom theme object and colorMode ("none", "16", "256", "truecolor").
````

### ow.screen.graphemes

`ow.screen.graphemes(aText) : Array`

````text
Splits a plain UTF-8 string into user-perceived grapheme clusters (handling surrogate pairs, combining marks, skin-tone modifiers, variation selectors, keycaps, regional indicator flags, and ZWJ sequences).
````

### ow.screen.hr

`ow.screen.hr(aWidth, aOptions) : String`

````text
Renders a horizontal rule / divider of aWidth columns with optional label, align ("left", "center", "right"), character, and style.
````

### ow.screen.parseColor

`ow.screen.parseColor(aSpec) : Map`

````text
Parses a color specification (named color, 0-255 number, "FG(n)", "BG(n)", "#rgb", "#rrggbb", "rgb(r,g,b)", or [r,g,b]) into a normalized descriptor with { type, r, g, b, idx256, ansi16, css }. Returns null if invalid or empty.
````

### ow.screen.parseStyle

`ow.screen.parseStyle(aStyle) : Map`

````text
Parses a style string (e.g. "BOLD,ITALIC,FG(39),BG(#1e1e2e)") or style map ({ fg, bg, bold, dim, faint, italic, underline, doubleUnderline, blink, invert, reverse, hidden, strikethrough, align }) into a normalized style map.
````

### ow.screen.progress

`ow.screen.progress(aValue, aMax, aMin, aWidth, aOptions) : String`

````text
Renders a smooth Unicode/ASCII progress bar with optional percentage/label and 16/256/truecolor styling.
````

### ow.screen.run

`ow.screen.run(aViewOrWindowOptions, aOnMessageFn, aDesktopOptions) : Object`

````text
Convenience helper to launch an interactive TUI view session using ow.desktop({ provider: "tui" }).
````

### ow.screen.sanitize

`ow.screen.sanitize(aText, allowMultiline) : String`

````text
Sanitizes untrusted application text by stripping ANSI/OSC escape sequences and C0/C1 control characters.
````

### ow.screen.sgr

`ow.screen.sgr(aStyle, aColorMode) : String`

````text
Returns the complete ANSI SGR escape sequence (e.g. "\x1b[1;3;38;5;39m") for aStyle. Returns "" if no attributes are active or colorMode is "none" (unless force is used).
````

### ow.screen.space

`ow.screen.space(aLines, aOptions) : Array`

````text
Applies padding ({ top, bottom, left, right } or number) and margins ({ top, bottom, left, right } or number) and item gap spacing to an array of lines or string.
````

### ow.screen.stripAnsi

`ow.screen.stripAnsi(aText) : String`

````text
Removes ANSI CSI and OSC escape sequences from aText.
````

### ow.screen.style

`ow.screen.style(aText, aStyle, aOptions) : String`

````text
Applies rich ANSI styling (foreground/background 16/256/truecolor, bold, dim/faint, italic, underline, doubleUnderline, blink, reverse/invert, hidden, strikethrough) to aText. Preserves nested resets by re-applying the outer SGR sequence before continuing.
````

### ow.screen.width

`ow.screen.width(aText) : Number`

````text
Returns the visible terminal column width of aText (ignoring ANSI sequences and counting wide CJK/emoji as 2 columns).
````

### ow.screen.wrap

`ow.screen.wrap(aText, aWidth) : Array`

````text
Word-wraps aText to aWidth visible columns (preserving grapheme clusters, wide characters, and ANSI codes) and returns an array of wrapped lines.
````
{% endraw %}
