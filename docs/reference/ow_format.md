---
layout: default
title: ow.format
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.format

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.format.js) · [Baseline](../source-snapshot.md)

### ow.format.IP2int

`ow.format.IP2int(aIP) : String`

````text
Converts an IP address into it's decimal IP address representation.
````

### ow.format.addNumberSeparator

`ow.format.addNumberSeparator(aNumber, aSeparator) : String`

````text
Returns a formatted number with decimal separators (default is comma but you can provide a custom aSeparator).
(available after ow.loadFormat())
````

### ow.format.bool

`ow.format.bool(aBoolValue, isLight, anExtra) : String`

````text
Given aBoolValue will return a green checkmark or a red cross character. If necessary anExtra ansiColor attributes can be added.
````

### ow.format.checkVersionSpec

`ow.format.checkVersionSpec(aVersion, aSpec) : Boolean`

````text
Checks whether aVersion satisfies a comma-separated version specification using >=, <=, >, <, = or bare equality. (available after ow.loadFormat())
````

### ow.format.compareVersion

`ow.format.compareVersion(aVersionA, aVersionB) : Number`

````text
Compares two versions returning 1 when aVersionA is greater, 0 when they are equal and -1 when aVersionA is lower. Supports date, numeric and semantic versions. (available after ow.loadFormat())
````

### ow.format.cron.howManyAgo

`ow.format.cron.howManyAgo(aCron, lastUpdate, aLimit) : Map`

````text
Given aCron expression and a date/unix time of a lastUpdate will return a map with a boolean isDelayed, number of  ms delayedAtLeast, if delayed howManyAgo executions missed and the corresponding missed executions dates in missedTimes. When calculating the missed times there is aLimit (defaults to 100).
````

### ow.format.cron.isCronMatch

`ow.format.cron.isCronMatch(aDate, aCronExpression) : boolean`

````text
Returns trues if the provided aDate is a match for the provided aCronExpression. Otherwise returns false.
````

### ow.format.cron.nextScheduled

`ow.format.cron.nextScheduled(expr, count, start, end) : Date`

````text
Given a cron expr returns the next Date object when it will occur. If count > 1 it will provide an array of Dates with the next n Dates. If start and end Date are defined they will limit the range on which to provide dates.
````

### ow.format.cron.parse

`ow.format.cron.parse(aCronExpression) : Map`

Parses `aCronExpression` and produces a Map with a schedules array and a exceptions array (if any error is found).
Each schedules array item map has a key with all the number possibilities for the given `aCronExpression` provided:

- `s`: seconds (0-59)
- `m`: minutes (0-59)
- `h`: hours (0-23)
- `D`: month day (1-31)
- `M`: month (1-12)
- `d`: week day (1-7)

Example:

`ow.format.cron.parse("0 5 * * *")`; // 5am

### ow.format.cron.prevScheduled

`ow.format.cron.prevScheduled(expr, count, start, end) : Date`

````text
Given a cron expr returns the previous Date object when it will occur. If count > 1 it will provide an array of Dates with the previous n Dates. If start and end Date are defined they will limit the range on which to provide dates.
````

### ow.format.cron.set2LocalTime

`ow.format.cron.set2LocalTime()`

````text
Sets the default system-wide cron expression evaluation to the local time (default is UTC).
````

### ow.format.cron.set2UTC

`ow.format.cron.set2UTC()`

````text
Sets the default system-wide cron expression evaluation to UTC (the default).
````

### ow.format.cron.sleepUntilNext

`ow.format.cron.sleepUntilNext(expr)`

````text
Sleeps until the cron expr is expected to be true.
````

### ow.format.cron.timeUntilNext

`ow.format.cron.timeUntilNext(expr) : Number`

````text
Returns a number of ms until the cron expr is expected to be true.
````

### ow.format.dateDiff.inDays

`ow.format.dateDiff.inDays(dateBefore, dateAfter, shouldRound) : Number`

````text
Difference between dateAfter and dateBefore in days. If shouldRound = true will round from the previous time unit.
````

### ow.format.dateDiff.inHours

`ow.format.dateDiff.inHours(dateBefore, dateAfter, shouldRound) : Number`

````text
Difference between dateAfter and dateBefore in hours.  If shouldRound = true will round from the previous time unit.
````

### ow.format.dateDiff.inMinutes

`ow.format.dateDiff.inMinutes(dateBefore, dateAfter, shouldRound) : Number`

````text
Difference between dateAfter and dateBefore in minutes. If shouldRound = true will round from the previous time unit.
````

### ow.format.dateDiff.inMonths

`ow.format.dateDiff.inMonths(dateBefore, dateAfter) : Number`

````text
Difference between dateAfter and dateBefore in months.
````

### ow.format.dateDiff.inSeconds

`ow.format.dateDiff.inSeconds(dateBefore, dateAfter, shouldRound) : Number`

````text
Difference between dateAfter and dateBefore in seconds. If shouldRound = true will round from the previous time unit.
````

### ow.format.dateDiff.inWeeks

`ow.format.dateDiff.inWeeks(dateBefore, dateAfter, shouldRound) : Number`

````text
Difference between dateAfter and dateBefore in weeks. If shouldRound = true will round from the previous time unit.
````

### ow.format.dateDiff.inYears

`ow.format.dateDiff.inYears(dateBefore, dateAfter) : Number`

````text
Difference between dateAfter and dateBefore in years.
````

### ow.format.dateTimeTransition

`ow.format.dateTimeTransition(aZone, aDate) : Map`

````text
Given aZone (defaults to Europe/London) and aDate (defaults to now) will return a map with the previous  and next date/time transition.
````

### ow.format.dateTimeZones

`ow.format.dateTimeZones() : Array`

````text
List all available Java zone ids.
````

### ow.format.elapsedTime

`ow.format.elapsedTime(aStartTime, aEndTime, aFormat) : String`

````text
Shortcut for ow.format.elapsedTime4ms calculating the absolute difference, in ms, between aStartTime and aEndTime.
````

### ow.format.elapsedTime4ms

`ow.format.elapsedTime4ms(aMs, aFormat) : String`

Given `aMs` (milliseconds) will convert into a string with the corresponding human-readable time and date components
up to years. This is usually helpful when comparing dates (see also `ow.format.elapsedTime`). You can control the output
format by adding options to `aFormat`:

Example:

```javascript
aFormat = {
   full : false, // when true outputs everything even if it's 0 value
   abrev: false, // when true outputs smaller "1h2m3s" instead of "1 hour, 2 minutes and 3 seconds"
   pad  : false, // when true pads values with 0 on the left
   colon: false, // when true outputs just values separated by ":"
   sep  : ", ",  // customizes the values separator, defaults to ", " or "" (in case of abrev = true)
   maxLeft : 7,  // the maximum number of time units to show counting from the left
   maxRight: 7   // the maximum number of time units to show counting from the right
}
```

### ow.format.escapeHTML

`ow.format.escapeHTML(aString) : String`

````text
Will escape, and return, aString for HTML/XML special characters.
(available after ow.loadFormat())
````

### ow.format.escapeHTML4

`ow.format.escapeHTML4(aString) : String`

````text
Uses Apache Commons Lang escape HTML4 functionality to convert aString into HTML4 entities where needed.
````

### ow.format.escapeRE

`ow.format.escapeRE(aString) : String`

````text
Tries to escape in aString all characters that make up a RegExp.
````

### ow.format.escapeString

`ow.format.escapeString(aString, aExceptString) : String`

````text
Will escape, and return, aString for RegExp special characters with the exception of any characters in aExceptString.
(available after ow.loadFormat())
````

### ow.format.fromBase16

`ow.format.fromBase16(aString) : bytes`

````text
Given a base 16 aString transforms it back to the original array of bytes.
````

### ow.format.fromBase32

`ow.format.fromBase32(aString) : bytes`

````text
Given a base 32 aString transforms it back to the original array of bytes.
````

### ow.format.fromBase36

`ow.format.fromBase36(aString) : Number`

````text
Converts a provided base36 aString into the corresponding number.
````

### ow.format.fromBinary

`ow.format.fromBinary(aString) : Number`

````text
Converts a provided binary aString into the decimal number.
````

### ow.format.fromByte

`ow.format.fromByte(aByte) : Number`

````text
Converts a byte info a decimal number.
````

### ow.format.fromBytesAbbreviation

`ow.format.fromBytesAbbreviation(aStr, useDecimal) : Number`

````text
Tries to reverse the ow.format.toBytesAbbreviation from aStr (string) back to the original value in bytes. Use useDecimal=true to interpret KB as 1000 instead of 1024 (see more in https://en.wikipedia.org/wiki/Byte#Multiple-byte_units)
(available after ow.loadFormat())
````

### ow.format.fromDate

`ow.format.fromDate(aDate, aFormat, aTimeZone) : String`

Will convert a javascript `aDate` into a String representation given `aFormat`:

- `G`: Era descriptor (AD)
- `y`: Year (1996; 96)
- `Y`: Week year (2009; 09)
- `M`: Month in year (July; Jul; 07)
- `w`: Week in year (27)
- `W`: Week in month (2)
- `D`: Day in year (189)
- `d`: Day in month (10)
- `F`: Day of week in month (2)
- `E`: Day name in week (Tuesday; Tue)
- `u`: Day number of week (1 = Monday, ..., 7 = Sunday) (1)
- `a`: Am/pm number (PM)
- `H`: Hour in day (0-23)
- `k`: Hour in day (1-24)
- `K`: Hour in am/pm (0-11)
- `h`: Hour in am/pm (1-12)
- `m`: Minute in hour (30)
- `s`: Second in minute (55)
- `S`: Millisecond (978)
- `z`: Time zone (Pacific Standard Time; PST; GMT-08:00)
- `Z`: Time zone (-0800)
- `X`: Time zone (-08; -0800; -08:00)

Optionally you can also provide `aTimeZone` (like 'America/New_York', 'Europe/London', 'UTC', ...)

(available after `ow.loadFormat()`)

### ow.format.fromHex

`ow.format.fromHex(aString) : Number`

````text
Converts a provided hexadecimal aString into the decimal number.
````

### ow.format.fromISODate

`ow.format.fromISODate(aISODate) : Date`

````text
Converts a ISO date string into a javascript Date.
````

### ow.format.fromLDAPDate

`ow.format.fromLDAPDate(aLDAPDate) : Date`

````text
Converts a numeric aLDAPDate (also known as Windows NT time format, Active Directory timestamps) into a javascript Date.
````

### ow.format.fromNumberSpacing

`ow.format.fromNumberSpacing(aNumber, aSpacer) : Number`

````text
Returns a number from a string with aSpacer as thousands separator.
(available after ow.loadFormat())
````

### ow.format.fromOctal

`ow.format.fromOctal(aString) : Number`

````text
Converts a provided octal aString into the decimal number.
````

### ow.format.fromSIAbbreviation

`ow.format.fromSIAbbreviation(aString) : Number`

````text
Converts the provided string using SI notationp prefix (do previously make the necessary conversions: 5mV -> 5m, 5cm -> 5c, 9km -> 9k) to the corresponding number. Uses the current approved SI prefix list (https://en.wikipedia.org/wiki/Metric_prefix)
````

### ow.format.fromTimeAbbreviation

`ow.format.fromTimeAbbreviation(aStr) : Number`

````text
From aStr time abbreviation (e.g. 1h2m3s (1 hour, 2 minutes and 3 seconds)) will return the corresponding amount of time in ms.
````

### ow.format.fromUnixDate

`ow.format.fromUnixDate(aUnixDate) : Date`

````text
Converts aUnixDate timestamp into a javascript Date.
````

### ow.format.fromWedoDate

`ow.format.fromWedoDate(aWedoDate, aFormat) : String`

Shortcut for `ow.format.fromDate` but using a wedo date. See `ow.format.fromDate` for more help.

(available after `ow.loadFormat()`)

### ow.format.fromWedoDateToDate

`ow.format.fromWedoDateToDate(aWedoDate) : Date`

````text
Returns a date object from a wedo date. (available after ow.loadFormat())
````

### ow.format.getActualTime

`ow.format.getActualTime(useAlternative) : Date`

````text
Retrieves the current actual time from worldtimeapi.org (through https). The current actual time will be returned in a Date. If useAlternative = true it will use worldclockapi.com (through http)
````

### ow.format.getClasspath

`ow.format.getClasspath() : String`

````text
Returns the current java classpath.
````

### ow.format.getCurrentDirectory

`ow.format.getCurrentDirectory() : String`

````text
Returns the current working directory.
````

### ow.format.getDoH

`ow.format.getDoH(aAddr, aType, aProvider) : Array`

````text
Performs a DNS over HTTPs query with aAddr. Optionally you can provide the aType of record (defaults to 'a') and the DNS over HTTPs aProvider between 'google' and 'cloudflare'.
````

### ow.format.getHostAddress

`ow.format.getHostAddress() : String`

````text
Returns the current host ip address.
````

### ow.format.getHostName

`ow.format.getHostName() : String`

````text
Returns the current hostname.
````

### ow.format.getJavaHome

`ow.format.getJavaHome() : String`

````text
Returns the current java home directory.
````

### ow.format.getJavaVersion

`ow.format.getJavaVersion() : String`

````text
Returns the current java version.
````

### ow.format.getOS

`ow.format.getOS() : String`

````text
Returns the current operating system identifier string.
````

### ow.format.getOSArch

`ow.format.getOSArch() : String`

````text
Returns the current operating system architecture string.
````

### ow.format.getOSVersion

`ow.format.getOSVersion() : String`

````text
Returns the current operating system version string.
````

### ow.format.getPublicIP

`ow.format.getPublicIP() : Map`

````text
Uses the functionality provided by http://ifconfig.co to return a map with the apparent current public ip address, public hostname and a guess of country and city. Please be aware of the request limits of the service (around 1 request per minute).
````

### ow.format.getReverseDoH

`ow.format.getReverseDoH(aIP, aProvider) : Array`

````text
Tries to retrieve the reverse DNS of aIP using DNS over HTTPs. Optionally you can choose the aProvider between 'google' and 'cloudflare'.
````

### ow.format.getTLSCertificates

`ow.format.getTLSCertificates(aHost, aPort, withJava, aPath, aPass, aSoTimeout) : Array`

````text
Tries to retreive the TLS certificates from aHost, aPort (defaults to 443). Optionally if withJava=true the original certificate Java object will also be included. If the CA certificates is in a different location you can provide aPath and the corresponding aPass. Additionally you can specificy aSoTimeout (socket timeout in ms) which defaults to 10s.
````

### ow.format.getTmpDir

`ow.format.getTmpDir() : String`

````text
Returns the current temporary directory.
````

### ow.format.getUserHome

`ow.format.getUserHome() : String`

````text
Returns the current user home path.
````

### ow.format.getUserName

`ow.format.getUserName() : String`

````text
Returns the current user name.
````

### ow.format.int2IP

`ow.format.int2IP(aIPInt) : String`

````text
Converts the decimal IP address representation aIPInt into an IP address.
````

### ow.format.isEmail

`ow.format.isEmail(aEmail) : boolean`

````text
Tries to determine if aEmail seems a syntactic valid email.
````

### ow.format.isHost

`ow.format.isHost(aHost) : boolean`

````text
Tries to determine if aHost seems a syntactic valid host.
````

### ow.format.isIPv4

`ow.format.isIPv4(aIP) : boolean`

````text
Tries to determine if aIP is a syntactic valid IPv4.
````

### ow.format.isIPv6

`ow.format.isIPv6(aIP) : boolean`

````text
Tries to determine if aIP is a syntactic valid IPv6.
````

### ow.format.isURL

`ow.format.isURL(aURL) : boolean`

````text
Tries to determine if aURL seems a syntactic valid URL.
````

### ow.format.isWedoDate

`ow.format.isWedoDate(aWedoDate) : boolean`

Determines if the `aWedoDate` object is a wedo date type (returns true if yes, false otherwise).

(available after `ow.loadFormat()`)

### ow.format.isWindows

`ow.format.isWindows() : Boolean`

````text
Returns true if the operating system is identified as Windows otherwise returns false.
````

### ow.format.logErrWithFooter

`ow.format.logErrWithFooter(aMessage, aFooter)`

````text
Equivalent to ow.format.printWithFooter (see help ow.format.printWithFooter) using the logErr function.
````

### ow.format.logErrWithProgressFooter

`ow.format.logErrWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)`

````text
Equivalent to ow.format.printWithProgressFooter (see help ow.format.printWithProgressFooter) using the logErr function.
````

### ow.format.logWarnWithFooter

`ow.format.logWarnWithFooter(aMessage, aFooter)`

````text
Equivalent to ow.format.printWithFooter (see help ow.format.printWithFooter) using the logWarn function.
````

### ow.format.logWarnWithProgressFooter

`ow.format.logWarnWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)`

````text
Equivalent to ow.format.printWithProgressFooter (see help ow.format.printWithProgressFooter) using the logWarn function.
````

### ow.format.logWithFooter

`ow.format.logWithFooter(aMessage, aFooter)`

````text
Equivalent to ow.format.printWithFooter (see help ow.format.printWithFooter) using the log function.
````

### ow.format.logWithProgressFooter

`ow.format.logWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)`

````text
Equivalent to ow.format.printWithProgressFooter (see help ow.format.printWithProgressFooter) using the log function.
````

### ow.format.logWithWaiting

`ow.format.logWithWaiting(aMainFunc, aPrefixMsg, aCompleteMsg, aErrorMsg, aWaitSpeed, aTheme)`

````text
Executes aMainFunc while log aPrefixMsg with a waiting aTheme (defaults to a sequence of chars with a rotating bar). When aMainFunc ends it will replace the log with aCompleteMsg or aErrorMsg in case an exception is thrown. Optionally you can provide a different aWaitSpeed while cycling between the aTheme sequence of chars increasing/decreasing the "animation" effect.
````

### ow.format.percProgressReport

`ow.format.percProgressReport(aMainFunc, aProgressFunc, aTimeout)`

Percentage progress report help function over a function on `aMainFunc` calling `aProgressFunc` in parallel
with a percentage function parameter (receiving target and source numbers). You can also provide an alternative
`aTimeout` between `aProgressFunc` calls (defaults to 150ms).

Example:

```javascript
ow.format.percProgressReport(() => {
   ioStreamCopy(io.writeFileStream("target.file"), io.readFileStream("source.file"));
}, (percFunc) => {
      var perc = percFunc(io.fileInfo("target.file").size, io.fileInfo("source.file").size);
   ...
});
```

### ow.format.percentile

`ow.format.percentile(aArray, aPercentile) : Number`

````text
Will return the percentile (aPercentile between 0 and 1) for the provided aArray of numbers.
````

### ow.format.printBoxplot

`ow.format.printBoxplot(values, aOptions) : String`

````text
Returns one or more compact terminal boxplots from a number array or an array of { values, label } series. aOptions: width, min, max, showOutliers (default true), palette.
````

### ow.format.printBullet

`ow.format.printBullet(values, aOptions) : String`

````text
Returns one or more bullet graphs from a map or array of maps with { value, target, min, max, ranges, label }. aOptions: width, palette, min, max, target, ranges, label, unit, showValue (default true), valueFormat ("raw", "si" or "bytes"; default "raw").
````

### ow.format.printDashboard

`ow.format.printDashboard(widgets, aOptions) : String`

Returns a multi-widget dashboard string. `widgets` is an array (or 2D array for explicit grid rows) of widget maps
with fields: type, data, title, span (proportional column width, default 1), options. Supported types: table, tree,
chart, sparkline, histogram, heatmap, bullet, scatter, boxplot, timeline, statusMatrix, progress, text, md, map, area, bar, func.

Per-widget notes:

- `chart`: data is a printChart format string
- `area`: data is consumed by `ow.format.string.chart`
- `bar`: data is a printBars format string; options can include max, min, indicator, space
- `bullet`: data is consumed by `ow.format.printBullet`; options can include min, max, target, ranges, label, unit, showValue, valueFormat
- `sparkline`: data is consumed by `ow.format.printSparkline`
- `histogram`: data is consumed by `ow.format.printHistogram`
- `heatmap`: data is consumed by `ow.format.printHeatmap` (numeric matrix, or a date/time/date-time keyed map for a time-bucketed view)
- `scatter`: data is consumed by `ow.format.printScatter`
- `boxplot`: data is consumed by `ow.format.printBoxplot`
- `timeline`: data is consumed by `ow.format.printTimeline`
- `statusMatrix`: data is consumed by `ow.format.printStatusMatrix`

`aOptions`: width, height, columns (auto if 0), border (default true), borderColor, borderStyle, palette.

### ow.format.printHeatmap

`ow.format.printHeatmap(values, aOptions) : String`

Returns a compact terminal heatmap for a numeric matrix, a map containing { `values`, xLabels, yLabels }, or
(for a time-bucketed view) a plain map keyed by date ("YYYY-MM-DD"), time ("HH:mm") or date-time
("YYYY-MM-DDTHH:mm") strings mapping to numeric `values`, e.g. { "2026-01-15": 3, "2026-01-16": 0 }.

Time-bucketed `aOptions`: xAxis/yAxis (one of "year", "month", "week", "weekday", "day", "hour"; yAxis may
be "none" to force a single row; defaults to xAxis:"week",yAxis:"weekday" for date/date-time keys - a
GitHub-style contribution calendar - or xAxis:"hour",yAxis:"none" for time-only keys; pass e.g.
xAxis:"hour",yAxis:"weekday" on date-time keys for a punch-card view), weekStart (0=Sunday, default),
from/to (bound the visible range), aggregate ("sum" default, "avg", "max" or "count", for multiple `values`
landing in the same bucket), legend (default false, renders "Less (shades) More"), empty (glyph for
buckets with no data, default "·"), dayLabels (which weekday rows/columns get a text label, default
["Mon","Wed","Fri"]), width, height, palette.

### ow.format.printHistogram

`ow.format.printHistogram(values, aOptions) : String`

````text
Returns a terminal histogram string for the numeric values array. Bucket count is auto-selected via Sturges' formula unless aOptions.buckets is set. aOptions: width, height, vertical (default false = horizontal bars), color, labels (default true), showCount (default true), palette.
````

### ow.format.printScatter

`ow.format.printScatter(points, aOptions) : String`

````text
Returns a compact terminal scatter plot from an array of [x,y] pairs or { x, y, symbol, color } points. aOptions: width, height, xMin, xMax, yMin, yMax, xLabel, yLabel, palette.
````

### ow.format.printSparkline

`ow.format.printSparkline(series, aOptions) : String`

````text
Returns a compact sparkline string for the provided numeric series or array of named series ({data, name, color}). aOptions: width (default terminal width), label, showMinMax (default false), color, palette. Degrades to ASCII characters when unicode is not available.
````

### ow.format.printStatusMatrix

`ow.format.printStatusMatrix(values, aOptions) : String`

````text
Returns a compact status matrix from a matrix or { values, xLabels, yLabels } of statuses. aOptions: width, height, xLabels, yLabels, symbols, palette.
````

### ow.format.printTimeline

`ow.format.printTimeline(events, aOptions) : String`

````text
Returns a compact terminal timeline from an array of { label, start, end, color, status } events. aOptions: width, from, to, palette, labels (default true).
````

### ow.format.printWithFooter

`ow.format.printWithFooter(aMessage, aFooter)`

````text
Prints aMessage (if defined) with a aTemplate (template compiled function or string).
````

### ow.format.printWithProgressFooter

`ow.format.printWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)`

Prints `aMessage` (if defined) with a `aTemplate` (template compiled function or string) as a footer for percentage
progress information with the percentage value `aPerc`, for a given optional `aSize` (defaults to 50), an optional
`aUnixBlock` or `aWindowsBlock` (depending on the current operating system) and `aSpace`. Example:

```javascript
ow.loadTemplate();
var fn = ow.template.execCompiled(ow.template.compile("({{percFormat}}%) progress: |{{progress}}|"));
ow.format.printWithProgressFooter("processing xyz...", fn, aPerc);
ow.format.printWithFooter("Done.", "");
```

### ow.format.printWithWaiting

`ow.format.printWithWaiting(aMainFunc, aPrefixMsg, aCompleteMsg, aErrorMsg, aWaitSpeed, aTheme, printNLFn, useAsSuffix)`

````text
Executes aMainFunc while priting aPrefixMsg with a waiting aTheme (defaults to a sequence of chars with a rotating bar). When aMainFunc ends it will replace the priting with aCompleteMsg or aErrorMsg in case an exception is thrown. Optionally you can provide a different aWaitSpeed while cycling between the aTheme sequence of chars increasing/decreasing the "animation" effect.
````

### ow.format.progressReport

`ow.format.progressReport(aMainFunc, aProgressFunc, aTimeout)`

````text
Executes aMainFunc to execute some synchronous function while aProgressFunc is called asynchronously to  keep track of progress. You can also provide an alternative aTimeout between aProgressFunc calls (defaults to 150ms).
````

### ow.format.round

`ow.format.round(aNumber, aDigits) : String`

````text
Will return aNumber rounded to 0 decimal digits or aDigits decimal digits.
(available after ow.loadFormat())
````

### ow.format.semver

`ow.format.semver(aVersion) : ow.format.semver`

Creates an `ow.format.semver` instance for `aVersion`, with the following methods:

- `nextMajor`
- `nextMinor`
- `nextPatch`
- `getMajor`
- `getMinor`
- `getPatch`
- `greater(aVersion)`
- `lower(aVersion)`
- `greaterEquals(aVersion)`
- `lowerEquals(aVersion)`
- `equals(aVersion)`

### ow.format.sortSemanticVersions

`ow.format.sortSemanticVersions(aArray) : Array`

````text
Will sort the provided aArray of semantic versions (e.g. 1.0.0, 1.0.1, 1.1.0, 2.0.0, ...)
(available after ow.loadFormat())
````

### ow.format.sqlFormat

`ow.format.sqlFormat(aSQL, aMap) : String`

Will format `aSQL` using the sql-formatter library. Optionally you can provide `aMap` with the following options:

- `indent`: the indentation string (defaults to "  ")
- `uppercase`: if true will uppercase the SQL (defaults to false)
- `linesBetweenQueries`: number of lines between queries (defaults to 1)
- `maxColumnLength`: maximum column length (defaults to 50)
- `skipWhitespaceNearBlockParentheses`: if true will whitespace near block parentheses (defaults to false)
- `language`: the SQL language dialect (defaults to "StandardSql")

The language can be one of the following:

- `Db2`
- `MariaDb`
- `MySql`
- `N1ql`
- `PlSql`
- `PostgreSql`
- `Redshift`
- `SparkSql`
- `StandardSql`
- `TSql`

### ow.format.sshProgress

`ow.format.sshProgress(aFn) : Object`

Returns a SSH Java progress monitor callback object to be use with the SSH plugin functions.
Expects callback `aFn` that will be called with state (e.g. begin, count, end) and an Info map.
The Info map is composed of:

- `source`: the reported source of the transfer
- `target`: the reported target of the transfer
- `op`: the operation being performed (get or put)
- `start`: reported unix epoch when the transfer started
- `end`: reported unix epoch when the transfer stopped
- `count`: the last reported byte count
- `speed`: the calculated speed of transfer

If the returned value is false the transfer will be cancelled.

### ow.format.streamHandle

`ow.format.streamHandle(aHandle, inHandle, errHandle, outHandle, bufferSize) : Function`

Returns a function to help automated interaction with a running process. The function `aHandle` receives: `aType` (in/err); `aTxt`,
`inHandle` (function), `errHandle` (function) and an `outHandle` (function). Optionally you can provide an alternative `inHandle` function to print
stdout text, an `errHandle` function to print stderr text, an `outHandle` function to send text to stdin and/or a non default `bufferSize`.

Example:

```javascript
var res = $sh("myProcess.sh --something")
          .cb(expect((aType, aTxt, inHandle, errHandle, outHandle) => {
             if (aType == "in") {
                inHandle(aTxt)
                if (/ name\?/.test(aTxt))                return outHandle("Scott\n")
               if (aTxt.indexOf("Anything else?") >= 0) return outHandle("nope!\n")
             }
          }))
          .get(0)
```

### ow.format.streamSH

`ow.format.streamSH(aFunction, anEncoding) : Function`

````text
To be used with sh, af.sh or ssh.exec as the callbackFunc. Returns a function that will call aFunction for each line and used the returned string with print and printErr.
````

### ow.format.streamSHLog

`ow.format.streamSHLog(aFunction) : Function`

````text
To be used with sh, af.sh or ssh.exec as the callbackFunc. Returns a function that will call aFunction for each line and used the returned string with log and logErr.
````

### ow.format.streamSHPrefix

`ow.format.streamSHPrefix(aPrefix, anEncoding, aSeparator, aTemplate, aFnHandler, infoFn, errorFn) : Function`

````text
To be used with sh, af.sh or ssh.exec as the callbackFunc. Returns a function that will prefix each line with aPrefix and used the returned string with print and printErr. Optionally you can provide aTemplate to add "prefix" (defaults to "[{{prefix}}]") and/or provide aFnHandler to chain another streaming handling function (receives a stream and a boolean to indicate if its stdout or stderr). It's also possible to provide a infoFn and errorFn to handle the output. If infoFn or errorFn are not provided they will default to print and printErr or to log and logErr if __flags.SH.prefixLog is true.
````

### ow.format.string.ansiClip

`ow.format.string.ansiClip(aStr, aWidth, aEllipsis) : String`

````text
Clips aStr to, at most, aWidth visible columns (wide emoji count as 2) without ever cutting an ANSI escape sequence. If clipped, aEllipsis (default "…") is appended and any open ANSI styling is reset.
````

### ow.format.string.ansiMoveDown

`ow.format.string.ansiMoveDown(nLines)`

````text
Moves the cursor nLines down.
````

### ow.format.string.ansiMoveLeft

`ow.format.string.ansiMoveLeft(nChars)`

````text
Moves the cursor left chars.
````

### ow.format.string.ansiMoveRight

`ow.format.string.ansiMoveRight(nChars)`

````text
Moves the cursor right chars.
````

### ow.format.string.ansiMoveUp

`ow.format.string.ansiMoveUp(nLines)`

````text
Moves the cursor nLines up.
````

### ow.format.string.ansiPad

`ow.format.string.ansiPad(aStr, aWidth) : String`

````text
Right-pads aStr with spaces up to aWidth visible columns (ANSI escape sequences and wide emoji are accounted for). Never truncates.
````

### ow.format.string.ansiScrollDown

`ow.format.string.ansiScrollDown(nLines)`

````text
Scrolls the screen down by nLines.
````

### ow.format.string.ansiScrollUp

`ow.format.string.ansiScrollUp(nLines)`

````text
Scrolls the screen up by nLines.
````

### ow.format.string.bestPrefix

`ow.format.string.bestPrefix(aString, anArrayOfStrings) : aString`

Given `anArrayOfStrings` will try to find the best prefix string on that array for the provided `aString`.
See `ow.format.string.closest` if you don't want to be based on the prefix.
Example:

```javascript
var anArrayOfStrings = [ "/user", "/use", "/username", "/u" ];
ow.format.string.bestPrefix("/user/1", anArrayOfStrings); // Returns /user
ow.format.string.bestPrefix("/u1", anArrayOfStrings); // Returns /u
ow.format.string.bestPrefix("/userna", anArrayOfStrings); // Returns /user
```

### ow.format.string.bool

`ow.format.string.bool(aBoolValue, isLight, anExtra) : String`

````text
Given aBoolValue will return a green checkmark or a red cross character. If necessary anExtra ansiColor attributes can be added.
````

### ow.format.string.chart

`ow.format.string.chart(aName, aDataPoint, aHSIze, aVSize, aMin, aMax, aTheme) : String`

````text
Given data aName will store, between calls, aDataPoint provided to plot a chart with a horizontal aHSize and a vertical aVSize. Optionally aMin value and aMax value can be provided. aTheme can optionally also be provided containing the map entries space (char), bar (char), point (char), vertical (boolean) and axis (boolean)
````

### ow.format.string.closest

`ow.format.string.closest(aString, anArrayOfStrings, aThreshold) : aString`

Given `anArrayOfStrings` will try to find the closest string on that array for the provided `aString`.
If `aThreshold` is not provided a default value of 3 will be used.
See `ow.format.string.bestPrefix` if you want to be based on the prefix.
Example:

```javascript
var anArrayOfStrings = [ "/user", "/use", "/username", "/u" ];
ow.format.string.closest("/user/1", anArrayOfStrings); // Returns /user
ow.format.string.closest("/u1", anArrayOfStrings); // Returns /u
ow.format.string.closest("/userna", anArrayOfStrings); // Returns /user
ow.format.string.closest("/usernam", anArrayOfStrings); // Returns /username
```

### ow.format.string.dataClean

`ow.format.string.dataClean(aName)`

````text
Given aName for data points entered using ow.format.string.chart and ow.format.string.dataLineChart will effectively delete all cached data. If aName is not provided it will eliminate of cached data.
````

### ow.format.string.dataLineChart

`ow.format.string.dataLineChart(aName, aDataPoint, aHSIze, aVSize, aOptions) : String`

````text
Given data aName will store, between calls, aDataPoint (number or array of numbers) provided to plot a line chart with a horizontal aHSize and a vertical aVSize. Optionally aOptions, equivalent to ow.format.string.lineChart options, can optionally also be provided.
````

### ow.format.string.distance

`ow.format.string.distance(aStringA, aStringB, maxOffset) : Number`

````text
Calculates the distance between aStringA and aStringB into the number of inserts, deletions and updates needed. If the maxOffset is not provided a value of 5 maximum characters difference will be  used. (Currently based on Sift4)
````

### ow.format.string.genPass

`ow.format.string.genPass(aSize, aSets, aExclude, aWeights) : String`

````text
Tries to generate a random password with aSize (defaults to 12) optionally given an array of aSets (between lowercase, uppercase, numbers, symbols and symbols2) and also aExclude a string of characters given an optional percentage of aWeights probability for each aSets.
````

### ow.format.string.getAstralCodePoint

`ow.format.string.getAstralCodePoint(aHighSurrogate, aLowSurrogate) : Number`

````text
Given a 8-bit aHighSurrogate code and a 8-bit aLowSurogate code returns a 16-bit unicode code
````

### ow.format.string.getSurrogatePair

`ow.format.string.getSurrogatePair(astralCodePoint) : Array`

````text
Returns an array of two 8 bit codes given an unicode astralCodePoint of 16 bits
````

### ow.format.string.grid

`ow.format.string.grid(aMatrix, aX, aY, aBgPattern, shouldReturn) : String`

Renders a live terminal grid composed of cells defined by `aMatrix` (an array of rows, each row an array of cell maps).
`aX` sets the height per row in lines (defaults to terminal height / number of rows), `aY` sets the total width in characters
(defaults to terminal width). `aBgPattern` is the background fill character (defaults to " "). If `shouldReturn` = true the
result is returned as a string instead of printed with cursor-up (for live-update loops).

Each cell is a map with the following fields:

- `obj`: the data to render (type-dependent, see below)
- `type`: rendering type — map, tree, table, chart, area, bar, func, sparkline, histogram, heatmap, bullet, scatter, boxplot, timeline, statusMatrix, progress, md or text (default: tree for maps/arrays, text otherwise)
- `title`: optional column heading rendered as "> title ────" above the cell content
- `xspan`: number of columns this cell spans horizontally (default: 1)
- `yspan`: number of rows this cell spans vertically (default: 1)

Per-type 'obj' format and extra options:

- `text/md`: obj is a string; md renders markdown
- `map`: obj is a map rendered with printMap
- `tree/table`: obj is a map or array rendered with `ow.format`
- `chart/area`: obj is a printChart format string
- `bar`: obj is a printBars format string (e.g. "int 42:red:label"); delegates to printBars and supports max, min, indicator, space
- `func`: obj is a JS function body string receiving mx (height) and my (width), must return a string
- `sparkline`: obj is a number array or multi-series array (see `ow.format.printSparkline`)
- `histogram`: obj is a number array (see `ow.format.printHistogram`)
- `heatmap`: obj is a number matrix or { values, xLabels, yLabels } (see `ow.format.printHeatmap`)
- `bullet`: obj is a map or array of maps with { value, target, min, max, ranges, label }; supports target, ranges, label, unit, showValue and valueFormat in options (see `ow.format.printBullet`)
- `scatter`: obj is an array of [x,y] or { x, y, symbol, color } points (see `ow.format.printScatter`)
- `boxplot`: obj is a number array or array of { values, label } series (see `ow.format.printBoxplot`)
- `timeline`: obj is an array of { label, start, end, color, status } events (see `ow.format.printTimeline`)
- `statusMatrix`: obj is a matrix or { values, xLabels, yLabels } of status values (see `ow.format.printStatusMatrix`)
- `progress`: obj is a number or { value, max, min } map

Each cell delegates rendering to `ow.format.printDashboard`.

### ow.format.string.leftPad

`ow.format.string.leftPad(aString, length, padExpression) : String`

````text
Using a padExpression will left pad aString for the given length.
````

### ow.format.string.lineChart

`ow.format.string.lineChart(aSeries, aOptions) : String`

Given an array of values (1 series) or an array of arrays of values (multiple series) will plot a line chart in
ascii, with the provided `aOptions`, a return the corresponding string. Available options:

- `min` (number) The minimum value to use in the chart
- `max` (number) The maximum value to use in the chart
- `height` (number) The line chart lines height to use
- `width` (number) The maximum width of the line chart
- `colors` (array) Array of color names to use for each series
- `label` (boolean) Boolean value to indicate if y labels should be included (default true)
- `format` (function) Custom functions that receives a value and returns a formatted string for labels
- `dColor` (string) The default color to use
- `offset` (number) The offset to assume (default 2)
- `padding` (string) The chart padding string (default "")
- `fixed` (number) If no custom format function is provided will be the fixed decimals to use (default 2)
- `symbols` (array) An array of 10 characters to replace the default symbols

### ow.format.string.lineChartLegend

`ow.format.string.lineChartLegend(titles, options) : Array`

````text
Given an array of titles and the options provided to ow.format.string.lineChart will return an array with each "symbol" and color used for each series and the corresponding "title".
````

### ow.format.string.lsHash

`ow.format.string.lsHash(aStringA, aStringB, dontCareDiffSize) : String`

Generates a locality sensitive hash for `aStringA`. If `aStringB` is provided it will compute the
hash difference between `aStringA` and `aStringB` returning a number (if 0 means the strings are almost
identical; if 200 or higher means the strings are very different). Optionally you can indicate that the
difference should care about differences in size `dontCareDiffSize` = true. This is based on https://github.com/trendmicro/tlsh/blob/master/js_ext.

Note: A `aStringA` and `aStringB` should be, at least, 512 characters long and have enough randomness to
generate a proper hash.

### ow.format.string.lsHashDiff

`ow.format.string.lsHashDiff(aHashA, aHashB, dontCareDiffSize) : String`

````text
From a previously created, with ow.format.string.lsHash, aHashA and aHashB will calculate  the difference between them returning a number (if 0 means the strings are almost identical; if 200 or higher means the strings are very different). Optionally you can indicate that the difference should care about differences in size dontCareDiffSize = true. This is based on https://github.com/trendmicro/tlsh/blob/master/js_ext.
````

### ow.format.string.nLinesTemplate

`ow.format.string.nLinesTemplate(aSourceTemplate, initMap, alternativeTemplate, alternativePrintFunction) : Function`

````text
Returns a function to print multiple lines at the same time (using ansi cursor up). The function accepts a map parameter since it's based on the aSourceTemplate (handlebars). The initial render is performed using initMap. If ansi support is not  available and if alternativeTemplate is defined (and different of "" otherwise it defaults to aSourceTemplate) it will use it as alternative. Optionally it's also possible to define a different print function (alternativePrintFunction) to print (like log, for example).
````

### ow.format.string.pauseString

`ow.format.string.pauseString(aString, aMsg)`

````text
Given aString starts an interactive paging of the contents of aString. PgUp/Left and PgDown/Right move by a page; Up/Down move by a line. Shift+Left/Home jumps to the top and Shift+Right/End jumps to the bottom. Shift+PgUp and Shift+PgDown are also supported as top/bottom aliases. At the bottom navigation remains available; forward paging or any ordinary key exits. Use q to quit. Press / to find literal text, Enter to search, Escape to cancel, and n/N for next/previous match. Search ignores case unless the query contains uppercase letters; matches wrap at either end. An empty search clears matches. ANSI styling is ignored when searching and preserved when highlighting. Text fitting on one screen is printed immediately without waiting for input. Optionally aMsg can be provided to be displayed with the paging percentage (use \{{percentage}} to be replaced by the percentage).
````

### ow.format.string.printable

`ow.format.string.printable(aByteArray, aDefaultChar) : String`

````text
Tries to convert aByteArray into a printable string. If aDefaultChar to replace the non-printable characters is not provided it will default to ".".
````

### ow.format.string.progress

`ow.format.string.progress(aNumericValue, aMax, aMin, aSize, aIndicator, aSpace) : String`

Outputs an in-line progress bar given `aNumericValue`, `aMax` value, `aMin` value, the `aSize` of the bar and the `aIndicator`
to use. If not provided, `aMax` defaults to `aValue`, `aMin` defaults to 0, `aSize` defaults to the current screen width (or 5 if
if can be determined), `aIndicator` defaults to "#"
and `aSpace` defaults to " ". If `aSize` is a negative value and it's possible to determine the current screen width it will
subtract to the screen width. Example:

```javascript
loadLodash(); ow.loadFormat();
var arr = [-30, -25, -10, 0, 3, 5], max = _.max(arr), min = _.min(arr);
for(let i in arr) {
   print(ow.format.string.progress(arr[i], max, min, 5, '-'));
}
```

### ow.format.string.renderLines

`ow.format.string.renderLines(aMatrix, numberOfLines, aWidth, aBgPattern, shouldReturn) : String`

````text
Tries to render a string grid (if shouldReturn = true won't print it but jsut return it) for a specific aWidth for a numberOfLines with aBgPattern background pattern (defaults to " ") with aMatrix contents (divided by "\n").
````

### ow.format.string.rightPad

`ow.format.string.rightPad(aString, length, padExpression) : String`

````text
Using a padExpression will right pad aString for the given length.
````

### ow.format.string.separatorsToUnix

`ow.format.string.separatorsToUnix(aFilenamePath) : String`

````text
Tries to convert the provided aFilenamePath into a path with unix folder separators.
````

### ow.format.string.separatorsToWindows

`ow.format.string.separatorsToWindows(aFilenamePath) : String`

````text
Tries to convert the provided aFilenamePath into a path with windows folder separators.
````

### ow.format.string.tabExpand

`ow.format.string.tabExpand(aStr, aTabSize) : String`

````text
Given an input aStr and, optionally, aTabSize will expand the tabs in the string to the provided aTabSize ( similar to the unix expand command).  If aTabSize is not provided it will default to 8.
````

### ow.format.string.toHex

`ow.format.string.toHex(aByteArray, aSeparator) : String`

````text
Tries to convert aByteArray into a string of hex values separated by aSeparator (defaults to " ").
````

### ow.format.string.toHexArray

`ow.format.string.toHexArray(aByteArray, perLine) : String`

````text
Returns an array with the ow.format.string.toHex of aByteArray and ow.format.string.printable with a maximum  of perLine (defaults to 30) characters per array element.
````

### ow.format.string.unicode

`ow.format.string.unicode(aCodeNumber) : String`

Given a unicode `aCodeNumber` (8 or 16 bits) will convert to the necessary sequence of 8 bit.
For example: `ow.format.string.unicode(0x1F37A)`.

### ow.format.string.updateLine

`ow.format.string.updateLine(aPrintNLFn) : Function`

````text
Facilitates updating a message in the same line without entering new-lines. It will use the aPrintNLFn (if not defined uses printnl). Returns an object with two functions: line(aMessage) and end(). The function line() should be called to change the current line message. On the  end calling the function end() will clean-up a return the cursor to the beginning of the line.
````

### ow.format.string.wildcardRE

`ow.format.string.wildcardRE(aPattern, caseSensitive) : RegExp`

````text
Given aPattern using '*' wildcards (to match zero or more characters) or '?' question-mark to match a single character will return the corresponding RegExp. Optionally if caseSensitive=true the RegExp will include case sensitive option.
````

### ow.format.string.wildcardTest

`ow.format.string.wildcardTest(aString, aPattern, caseSensitive) : Boolean`

````text
Given aString will try to apply aPattern using '*' wildcards (to match zero or more characters) or '?' question-mark to match a single character. Will return true if the aPattern can be applied to aString. Optionally if caseSensitive=true the pattern will be tested with case sensitive.
````

### ow.format.string.wordWrap

`ow.format.string.wordWrap(aString, maxWidth, newLineSeparator, tabDefault) : String`

````text
Given aString word wraps the text on it given the maxWidth length per line. Optionally you can provide a newLineSeparator otherwise '\n' will be used. Optionally tabDefault determines how many spaces a tab represents (default 4) (available after ow.loadFormat())
````

### ow.format.string.wordWrapArray

`ow.format.string.wordWrapArray(anArray, maxTableSize, sepLen, sepFunc, useIndex, perRowHeight) : Array`

Given `anArray` of maps will return an array suitable to use with printTable for a `maxTableSize`, a separator length
(`sepLen` (which defaults to 1)) and an optional line separator function (`sepFunc` that receives the max length of a
column). Word-wrap is achieved by creating new map array entries whenever the calculated max size of each line
with `sepLen` is achieved. The boolean flag `useIndex` changes the result to a map with lines and idx (array of the positions
on the lines array that are a new `anArray` entry). If `perRowHeight` is true, each record uses its own wrapped height and column sizes are measured per physical line.
Example of usage:

```javascript
__initializeCon()
var maxS = __con.getTerminal().getWidth()
print(printTable(ow.format.string.wordWrapArray(io.listFiles("js").files, maxS, 1, s => ansiColor("FAINT", repeat(s, "-"))), maxS))
```

### ow.format.term.getCapabilities

`ow.format.term.getCapabilities(aOptions) : Map`

````text
Returns a map with terminal capabilities, including width/height, tty/ansi availability and color depth. Results are cached unless aOptions.refresh = true.
````

### ow.format.testHost

`ow.format.testHost(aAddress, aTimeout) : Map`

````text
Uses the java implementation (e.g. usually ICMP ping) for testing reachability to an aAddress. It timeouts after aTimeout (defaults to 4000ms). Returns a map with the "time" spent trying to get an answer from aAddress and a boolean "reachable" with the result.
````

### ow.format.testPort

`ow.format.testPort(aAddress, aPort, aCustomTimeout) : boolean`

````text
Tries to connect to aPort (e.g. 1234) on aAddress (e.g. 1.2.3.4). If the connection is successfull it will disconnect and return true, otherwise it will return false. If aCustomTimeout (in ms) is defined, it will use that value as the timeout instead of the 1,5 seconds by default.
````

### ow.format.testPortLatency

`ow.format.testPortLatency(aHost, aPort, aCustomTimeout) : Number`

````text
Test establishing a TCP socket connection with aHost on aPort. Optionally aCustomTimeout can be provided (defaults to 60000 ms). The test will be timed and the time in ms will be returned. If returned a time < 0 then an error occurred or the  host:port couldn't be reached.
````

### ow.format.testPublicPort

`ow.format.testPublicPort(aPort) : Map`

````text
Uses the functionality provided by http://ifconfig.co to return a map with the result of testing if aPort is within public  reach from your apparent current public ip address. Please be aware of the request limits of the service (around 1 request per minute).
````

### ow.format.testURLLatency

`ow.format.testURLLatency(aURL, aCustomTimeout) : Number`

````text
Test sending a HTTP(s) GET to aURL. Optionally aCustomTimeout can be provided. The test will be timed and the time in ms will be returned. If returned a time < 0 then an error occurred or the host:port couldn't be reached.
````

### ow.format.timeago

`ow.format.timeago(aDate, isAbv) : String`

````text
Will output how much time ago aDate is (e.g. 2 years ago, 30 minutes ago, etc...).
Optionally isAbv = true for abbreviated output.  (available after ow.loadFormat())
````

### ow.format.toAbbreviation

`ow.format.toAbbreviation(aNumber, aDigits) : String`

````text
Returns a number abbreviation to "k", "m", "b", "t". Will round number to 2 decimals if aDigits doesn't provide a different decimal digits to round to.
(available after ow.loadFormat())
````

### ow.format.toBase16

`ow.format.toBase16(aString) : String`

````text
Given aString or array of bytes transforms the contents to base 16.
````

### ow.format.toBase32

`ow.format.toBase32(aString) : String`

````text
Given aString or array of bytes transforms the contents to base 32.
````

### ow.format.toBase36

`ow.format.toBase36(aNumber, aLength) : String`

````text
Converts a provided aNumber to the base36 representation. Optionally you can provide a length for 0 left pad.
````

### ow.format.toBinary

`ow.format.toBinary(aNumber, aLength) : String`

````text
Converts a provided aNumber to the binary representation. Optionally you can provide a length for 0 left pad.
````

### ow.format.toBytesAbbreviation

`ow.format.toBytesAbbreviation(aNumber, aDigits) : String`

````text
Returns a number abbreviation to "bytes", "KB", "MB", "GB", "TB", etc. Will round number to 3 significant digits if aDigits doesn't provide a different number of precision digits to convert to.
(available after ow.loadFormat())
````

### ow.format.toCSLON

`ow.format.toCSLON(aObj, cTheme) : String`

````text
Equivalent to ow.fornat.toSLON but includes ansi color.
````

### ow.format.toDate

`ow.format.toDate(aStringDate, aFormat, aTimeZone) : Date`

Will convert `aStringDate` into a javascript Date given `aFormat`:

- `G`: Era descriptor (AD)
- `y`: Year (1996; 96)
- `Y`: Week year (2009; 09)
- `M`: Month in year (July; Jul; 07)
- `w`: Week in year (27)
- `W`: Week in month (2)
- `D`: Day in year (189)
- `d`: Day in month (10)
- `F`: Day of week in month (2)
- `E`: Day name in week (Tuesday; Tue)
- `u`: Day number of week (1 = Monday, ..., 7 = Sunday) (1)
- `a`: Am/pm number (PM)
- `H`: Hour in day (0-23)
- `k`: Hour in day (1-24)
- `K`: Hour in am/pm (0-11)
- `h`: Hour in am/pm (1-12)
- `m`: Minute in hour (30)
- `s`: Second in minute (55)
- `S`: Millisecond (978)
- `z`: Time zone (Pacific Standard Time; PST; GMT-08:00)
- `Z`: Time zone (-0800)
- `X`: Time zone (-08; -0800; -08:00)

Optionally you can also provide the original `aTimeZone` (like 'America/New_York', 'Europe/London', 'UTC', ...)
(available after `ow.loadFormat()`)

### ow.format.toHex

`ow.format.toHex(aNumber, aLength) : String`

````text
Converts a provided aNumber to the hexadecimal representation. Optionally you can provide a length for 0 left pad.
````

### ow.format.toLDAPDate

`ow.format.toLDAPDate(aDate) : Number`

````text
Converts a javascript Date into a LDAP date (also known as Windows NT time format, Active Directory timestamps)
````

### ow.format.toNumberSpacing

`ow.format.toNumberSpacing(aNumber, aSpacer) : String`

````text
Returns a number with aSpacer as thousands separator.
(available after ow.loadFormat())
````

### ow.format.toOctal

`ow.format.toOctal(aNumber, aLength) : String`

````text
Converts a provided aNumber to the octal representation. Optionally you can provide a length for 0 left pad.
````

### ow.format.toSLON

`ow.format.toSLON(aObj, cTheme) : String`

Stringifies `aObj` into a Single Line Object Notation using a default scheme for human readability or a
custom `cTheme` map composed of:

- `startMap`: `"("`
- `sepMap`: `", "`
- `endMap`: `")"`
- `sepKV`: `": "`
- `startArr`: `"["`
- `sepArr`: `" | "`
- `endArr`: `"]"`
- `strQuote`: `"'"`

### ow.format.toUnixDate

`ow.format.toUnixDate(aDate) : Number`

````text
Returns a unix timestamp from the provided javascript aDate.
````

### ow.format.toWedoDate

`ow.format.toWedoDate(aStringDate, aFormat) : Map`

Shortcut for using `ow.format.toDate` but converting the output into a wedo date.

(available after `ow.loadFormat()`)

### ow.format.transposeArrayLines

`ow.format.transposeArrayLines(anLineArray) : Array`

````text
Given anLineArray transposes into a new array of lines.
````

### ow.format.unescapeHTML4

`ow.format.unescapeHTML4(aString) : String`

````text
Uses Apache Commons Lang unescape HTML4 functionality to unconvert aString with HTML4 entities to the original string
````

### ow.format.viz.createCanvas

`ow.format.viz.createCanvas(aOptions) : Map`

````text
Creates a 2D character canvas with aOptions.width and aOptions.height (both default to terminal size). Returns a map with: width, height, write(row, col, str, style) and render() → String.
````

### ow.format.viz.diffFrames

`ow.format.viz.diffFrames(aPreviousFrame, aNextFrame, aOptions) : Map`

````text
Produces a terminal patch for replacing aPreviousFrame with aNextFrame and returns metadata for changed lines.
````

### ow.format.viz.layout

`ow.format.viz.layout`

````text
Layout helpers: split(total, specs) splits a total dimension into sizes (numbers = fixed, "50%" = percentage, anything else = auto remainder). padLines(str, width, height, fillChar) pads/trims str to a fixed box.
````

### ow.format.withMD

`ow.format.withMD(aString, defaultAnsi, aLineWidth, aBgColor) : String`

````text
Use aString with simple markdown and convert it to ANSI. Optionally you can add a defaultAnsi string to return back after applying the ansi styles for markdown (use ansiColor function to provide the defaultAnsi), provide aLineWidth to override the detected console width when line width is needed, and provide aBgColor (an ansiColor color name, e.g. "BG_BLUE") to maintain a background color throughout the output and pass it to sub-functions where applicable. Currently supports only: bold, italic, inline code, strikethrough, tables, simple code blocks, line rule, bullets, numbered lines, links, blocks and simple LaTeX-like math symbols (e.g. "$\rightarrow$", "$\alpha$", "$\leq$") which are converted to their unicode equivalent.
````

### ow.format.withSideLine

`ow.format.withSideLine(aString, aSize, ansiLine, ansiText, aTheme, aExtra) : String`

Generates a ansi escaped line with a "left side line" to display `aString` which will be word-wrap given
`aSize` (default to the current console size). Optionally ansi colors for `ansiLine` and `ansiText` can be provided (see ansiColor for possible values)
and `aTheme` (using `ow.format.withSideLineThemes`, for example). For closed rectangle themes `aExtra` map can include a header, footer, headerAlign (
left or right or center) and footerAlign (left or right or center).

### ow.format.withSideLineThemes

`ow.format.withSideLineThemes() : Map`

Returns a map of theme name to theme definition for use as the `aTheme` argument of `ow.format.withSideLine` (and the "theme" entries of
`__colorFormat.md`). A theme is a map with the optional characters ltop, tmiddle, rtop (top border), lmiddle, rmiddle (left and right sides),
lbottom, bmiddle, rbottom (bottom border) and tab (replacement for tab characters, default 3 spaces). The top/bottom border is only drawn when
the corner entries are defined. Built-in themes: closedOneSpace, simpleOneSpace, simpleLine, doubleOneSpace, doubleLine, simpleLineWithTips,
simpleLineWithBottomTip, simpleLineWithTopTip, simpleLineWithCTips, simpleLineWithCBottomTip, simpleLineWithCTopTip, simpleLineWithRTips,
simpleLineWithRTopTip, simpleLineWithRBottomTip, doubleLineWithRTips, doubleLineBothSides, closedRect, closedDoubleRect, closedCurvedRect,
openTopRect, openBottomRect, openRect, openTopCurvedRect, openBottomCurvedRect, openCurvedRect, openCurvedSpace and blockCurvedSpace.
Custom themes can be added (built-in themes win on name clashes) by setting `__flags.sideLineCustomThemes` to a map of name to theme before calling it.

Example:

```javascript
__flags.sideLineCustomThemes = { arrow: { lmiddle: ">" } }
print(ow.format.withSideLine("hello", __, "GREEN", __, ow.format.withSideLineThemes().arrow))
```

### ow.format.xls.autoFilter

`ow.format.xls.autoFilter(aXLS, aXLSSheet, aRange)`

Applies a auto filter on the provided `aXLS` and `aXLSSheet` object (from XLS.getSheet) to `aRange`.

Example:

```javascript
ow.format.xls.autoFilter(sheet, "A1:D1");
```

### ow.format.xls.getStyle

`ow.format.xls.getStyle(aXLS, aStyleMap)`

Creates a cell styler object, for the `aXLS` object (XLS plugin object instance), given the provided `aStyleMap`.
The `aStyleMap` can have the following keys to define a style:

- `bold` (boolean)
- `italic` (boolean)
- `underline` (boolean)
- `strikeout` (boolean)
- `fontPoints` (number)
- `fontName` (string)
- `fontColor` (string)
- `wrapText` (boolean)
- `shrinkToFit` (boolean)
- `backgroundColor` (string)
- `foregroundColor` (string)
- `borderBottom` (string)
- `borderLeft` (string)
- `borderRight` (string)
- `borderTop` (string)
- `borderLeftColor` (string)
- `borderRightColor` (string)
- `borderTopColor` (string)
- `borderBottomColor` (string)
- `rotation` (number)
- `indention` (number)
- `valign` ("top", "bottom", "center", "justify")
- `align` ("center", "centerSelection", "fill", "general", "justify", "left", "right")

Color names:

`aqua`, `auto`, `black`, `blue`, `blue_grey`, `bright_green`, `brown`, `coral`, `cornflower_blue`, `dark_blue`, `dark_green`, `dark_red`, `dark_teal`, `dark_yellow`, `gold`, `green`, `grey25`, `grey40`, `grey50`, `grey80`, `indigo`, `lavender`, `lemon_chiffon`, `light_blue`, `light_cornflower_blue`, `light_green`, `light_orange`, `light_turquoise`, `light_yellow`, `lime`, `maroon`, `olive_green`, `orange`, `orchid`, `pale_blue`, `pink`, `plum`, `red`, `rose`, `royal_blue`, `sea_green`, `sky_blue`, `tan`, `teal`, `turquoise`, `violet`, `white`, `yellow`

Border names:

`dash_dot`, `dash_dot_dot`, `dashed`, `dotted`, `double`, `hair`, `medium`, `medium_dash_dot`, `medium_dash_dot_dot`, `medium_dashed`, `none`, `slanted_dash_dot`, `thick`, `thin`

Fill patterns:

`solid_foreground`

### ow.format.xls.setTable

`ow.format.xls.setTable(aXLS, aSheet, aColumn, aRow, anArray, shouldAutoFilter, headerStyle, linesStyle)`

````text
Shortcut for xls.setTable that given aXLS object, a corresponding aSheet object will try to set the contents of  anArray of maps starting in aColumn and aRow performing auto size for all columns. If shouldAutoFilter = true is will also add an autofilter to all columns. It's possible also to customize the headerStyle and linesStyle.
````
{% endraw %}
