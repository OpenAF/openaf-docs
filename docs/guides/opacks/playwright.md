---
layout: default
title: playwright
parent: oPacks
grand_parent: Guides
---

{% raw %}
> Source: [openaf-opacks `87b07e97`](https://github.com/OpenAF/openaf-opacks/blob/87b07e9774902bccee8bf16632201e319dcfca0d/playwright/README.md). See [documentation baseline](../../source-snapshot.md) for availability and verification.

> Build and test commands use the package's source directory; installation and library examples use the installed oPack.

# playwright oPack

Wrapper around [Microsoft Playwright for Java](https://playwright.dev/java/) for OpenAF.

## Install

```bash
opack install playwright
```

## Library usage

```javascript
loadLib("playwright.js")

var pw = new Playwright()
var res = pw.run({
  url      : "https://example.com",
  engine   : "chromium", // chromium | firefox | webkit
  headless : true,
  timeout  : 30000
})

sprint(res)
```

### Screenshot

```javascript
var res = pw.run({
  url           : "https://example.com",
  screenshotPath: "example.png",
  fullPage      : true
})
```

### PDF

```javascript
var res = pw.run({
  url    : "https://example.com",
  pdfPath: "example.pdf"
})
```

## oafp usage

```bash
oafp libs=playwright in=playwright data="https://example.com" out=json
```

Generate a screenshot:

```bash
oafp libs=playwright in=playwright data="https://example.com" out=playwrightscreenshot playwrightscreenshot=example.png
```

## oJob wrapper and shortcuts

Use the bundled `oJobPlaywright.yaml` wrapper jobs:

```bash
ojob oJobPlaywright.yaml job="Playwright Page Info" url="https://example.com"
ojob oJobPlaywright.yaml job="Playwright Screenshot" url="https://example.com" screenshotPath=example.png
```

Shortcut forms:

```bash
ojob oJobPlaywright.yaml playwrightInfo="https://example.com"
ojob oJobPlaywright.yaml playwrightShot="https://example.com" screenshotPath=example.png
```

## Maven dependencies

This opack uses `.maven.yaml` with `com.microsoft.playwright:playwright`.
Download jars with:

```bash
ojob ojob.io/oaf/mavenGetJars folder=.
```

## Notes

On first execution Playwright may download browser binaries for the current platform.
`playwright.js` loads jars from the current folder first and then from the installed opack folder.
If `driver-bundle-<version>.jar` is not found in either location, it will try to download the matching driver bundle from Maven Central into the folder where the detected Playwright jars live.
{% endraw %}
