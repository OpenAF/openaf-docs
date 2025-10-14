---
layout: default
title: ow.format
parent: Reference
grand_parent: OpenAF docs
---


## ow.format

### ow.format.addNumberSeparator

__ow.format.addNumberSeparator(aNumber, aSeparator) : String__

````
Returns a formatted number with decimal separators (default is comma but you can provide a custom aSeparator).
(available after ow.loadFormat())
````
### ow.format.bool

__ow.format.bool(aBoolValue, isLight, anExtra) : String__

````
Given aBoolValue will return a green checkmark or a red cross character. If necessary anExtra ansiColor attributes can be added.
````
### ow.format.cron.howManyAgo

__ow.format.cron.howManyAgo(aCron, lastUpdate, aLimit) : Map__

````
Given aCron expression and a date/unix time of a lastUpdate will return a map with a boolean isDelayed, number of  ms delayedAtLeast, if delayed howManyAgo executions missed and the corresponding missed executions dates in missedTimes. When calculating the missed times there is aLimit (defaults to 100).
````
### ow.format.cron.isCronMatch

__ow.format.cron.isCronMatch(aDate, aCronExpression) : boolean__

````
Returns trues if the provided aDate is a match for the provided aCronExpression. Otherwise returns false.
````
### ow.format.cron.nextScheduled

__ow.format.cron.nextScheduled(expr, count, start, end) : Date__

````
Given a cron expr returns the next Date object when it will occur. If count > 1 it will provide an array of Dates with the next n Dates. If start and end Date are defined they will limit the range on which to provide dates.
````
### ow.format.cron.parse

__ow.format.cron.parse(aCronExpression) : Map__

````
Parses aCronExpression and produces a Map with a schedules array and a exceptions array (if any error is found). Each schedules array item map has a key with all the number possibilities for the given aCronExpression provided:

s - seconds (0-59)
m - minutes (0-59)
h - hours (0-23)
D - month day (1-31)
M - month (1-12)
d - week day (1-7)

Example:

ow.format.cron.parse("0 5 * * *"); // 5am


````
### ow.format.cron.prevScheduled

__ow.format.cron.prevScheduled(expr, count, start, end) : Date__

````
Given a cron expr returns the previous Date object when it will occur. If count > 1 it will provide an array of Dates with the previous n Dates. If start and end Date are defined they will limit the range on which to provide dates.
````
### ow.format.cron.set2LocalTime

__ow.format.cron.set2LocalTime()__

````
Sets the default system-wide cron expression evaluation to the local time (default is UTC).
````
### ow.format.cron.set2UTC

__ow.format.cron.set2UTC()__

````
Sets the default system-wide cron expression evaluation to UTC (the default).
````
### ow.format.cron.sleepUntilNext

__ow.format.cron.sleepUntilNext(expr)__

````
Sleeps until the cron expr is expected to be true.
````
### ow.format.cron.timeUntilNext

__ow.format.cron.timeUntilNext(expr) : Number__

````
Returns a number of ms until the cron expr is expected to be true.
````
### ow.format.dateDiff.inDays

__ow.format.dateDiff.inDays(dateBefore, dateAfter, shouldRound) : Number__

````
Difference between dateAfter and dateBefore in days. If shouldRound = true will round from the previous time unit.
````
### ow.format.dateDiff.inHours

__ow.format.dateDiff.inHours(dateBefore, dateAfter, shouldRound) : Number__

````
Difference between dateAfter and dateBefore in hours.  If shouldRound = true will round from the previous time unit.
````
### ow.format.dateDiff.inMinutes

__ow.format.dateDiff.inMinutes(dateBefore, dateAfter, shouldRound) : Number__

````
Difference between dateAfter and dateBefore in minutes. If shouldRound = true will round from the previous time unit.
````
### ow.format.dateDiff.inMonths

__ow.format.dateDiff.inMonths(dateBefore, dateAfter) : Number__

````
Difference between dateAfter and dateBefore in months.
````
### ow.format.dateDiff.inSeconds

__ow.format.dateDiff.inSeconds(dateBefore, dateAfter, shouldRound) : Number__

````
Difference between dateAfter and dateBefore in seconds. If shouldRound = true will round from the previous time unit.
````
### ow.format.dateDiff.inWeeks

__ow.format.dateDiff.inWeeks(dateBefore, dateAfter, shouldRound) : Number__

````
Difference between dateAfter and dateBefore in weeks. If shouldRound = true will round from the previous time unit.
````
### ow.format.dateDiff.inYears

__ow.format.dateDiff.inYears(dateBefore, dateAfter) : Number__

````
Difference between dateAfter and dateBefore in years.
````
### ow.format.dateTimeTransition

__ow.format.dateTimeTransition(aZone, aDate) : Map__

````
Given aZone (defaults to Europe/London) and aDate (defaults to now) will return a map with the previous  and next date/time transition.
````
### ow.format.dateTimeZones

__ow.format.dateTimeZones() : Array__

````
List all available Java zone ids.
````
### ow.format.elapsedTime

__ow.format.elapsedTime(aStartTime, aEndTime, aFormat) : String__

````
Shortcut for ow.format.elapsedTime4ms calculating the absolute difference, in ms, between aStartTime and aEndTime.
````
### ow.format.elapsedTime4ms

__ow.format.elapsedTime4ms(aMs, aFormat) : String__

````
Given aMs (milleseconds) will convert into a string with the corresponding human-readable time and date components up to years. This is usually helpful when comparing dates (see also ow.format.elapsedTime). You can control the output format by adding options to aFormat:

Example:

aFormat = {
   full : false, // when true outputs everything even if it's 0 value
   abrev: false, // when true outputs smaller "1h2m3s" instead of "1 hour, 2 minutes and 3 seconds"
   pad  : false, // when true pads values with 0 on the left
   colon: false, // when true outputs just values separated by ":"
   sep  : ", ",  // customizes the values separator, defaults to ", " or "" (in case of abrev = true)
   maxLeft : 7,  // the maximum number of time units to show counting from the left
   maxRight: 7   // the maximum number of time units to show counting from the right
}
````
### ow.format.escapeHTML

__ow.format.escapeHTML(aString) : String__

````
Will escape, and return, aString for HTML/XML special characters.
(available after ow.loadFormat())
````
### ow.format.escapeHTML4

__ow.format.escapeHTML4(aString) : String__

````
Uses Apache Commons Lang escape HTML4 functionality to convert aString into HTML4 entities where needed.
````
### ow.format.escapeRE

__ow.format.escapeRE(aString) : String__

````
Tries to escape in aString all characters that make up a RegExp.
````
### ow.format.escapeString

__ow.format.escapeString(aString, aExceptString) : String__

````
Will escape, and return, aString for RegExp special characters with the exception of any characters in aExceptString.
(available after ow.loadFormat())
````
### ow.format.fromBase16

__ow.format.fromBase16(aString) : bytes__

````
Given a base 16 aString transforms it back to the original array of bytes.
````
### ow.format.fromBase32

__ow.format.fromBase32(aString) : bytes__

````
Given a base 32 aString transforms it back to the original array of bytes.
````
### ow.format.fromBase36

__ow.format.fromBase36(aString) : Number__

````
Converts a provided base36 aString into the corresponding number.
````
### ow.format.fromBinary

__ow.format.fromBinary(aString) : Number__

````
Converts a provided binary aString into the decimal number.
````
### ow.format.fromByte

__ow.format.fromByte(aByte) : Number__

````
Converts a byte info a decimal number.
````
### ow.format.fromBytesAbbreviation

__ow.format.fromBytesAbbreviation(aStr, useDecimal) : Number__

````
Tries to reverse the ow.format.toBytesAbbreviation from aStr (string) back to the original value in bytes. Use useDecimal=true to interpret KB as 1000 instead of 1024 (see more in https://en.wikipedia.org/wiki/Byte#Multiple-byte_units)
(available after ow.loadFormat())
````
### ow.format.fromDate

__ow.format.fromDate(aDate, aFormat, aTimeZone) : String__

````
Will convert a javascript aDate into a String representation given aFormat:

  G - Era descriptor (AD)
  y - Year (1996; 96)
  Y - Week year (2009; 09)
  M - Month in year (July; Jul; 07)
  w - Week in year (27)
  W - Week in month (2)
  D - Day in year (189)
  d - Day in month (10)
  F - Day of week in month (2)
  E - Day name in week (Tuesday; Tue)
  u - Day number of week (1 = Monday, ..., 7 = Sunday) (1)
  a - Am/pm number (PM)
  H - Hour in day (0-23)
  k - Hour in day (1-24)
  K - Hour in am/pm (0-11)
  h - Hour in am/pm (1-12)
  m - Minute in hour (30)
  s - Second in minute (55)
  S - Millisecond (978)
  z - Time zone (Pacific Standard Time; PST; GMT-08:00)
  Z - Time zone (-0800)
  X - Time zone (-08; -0800; -08:00)

Optionally you can also provide aTimeZone (like 'America/New_York', 'Europe/London', 'UTC', ...)

(available after ow.loadFormat())
````
### ow.format.fromHex

__ow.format.fromHex(aString) : Number__

````
Converts a provided hexadecimal aString into the decimal number.
````
### ow.format.fromISODate

__ow.format.fromISODate(aISODate) : Date__

````
Converts a ISO date string into a javascript Date.
````
### ow.format.fromLDAPDate

__ow.format.fromLDAPDate(aLDAPDate) : Date__

````
Converts a numeric aLDAPDate (also known as Windows NT time format, Active Directory timestamps) into a javascript Date.
````
### ow.format.fromNumberSpacing

__ow.format.fromNumberSpacing(aNumber, aSpacer) : Number__

````
Returns a number from a string with aSpacer as thousands separator.
(available after ow.loadFormat())
````
### ow.format.fromOctal

__ow.format.fromOctal(aString) : Number__

````
Converts a provided octal aString into the decimal number.
````
### ow.format.fromSIAbbreviation

__ow.format.fromSIAbbreviation(aString) : Number__

````
Converts the provided string using SI notationp prefix (do previously make the necessary conversions: 5mV -> 5m, 5cm -> 5c, 9km -> 9k) to the corresponding number. Uses the current approved SI prefix list (https://en.wikipedia.org/wiki/Metric_prefix)
````
### ow.format.fromTimeAbbreviation

__ow.format.fromTimeAbbreviation(aStr) : Number__

````
From aStr time abbreviation (e.g. 1h2m3s (1 hour, 2 minutes and 3 seconds)) will return the corresponding amount of time in ms.
````
### ow.format.fromUnixDate

__ow.format.fromUnixDate(aUnixDate) : Date__

````
Converts aUnixDate timestamp into a javascript Date.
````
### ow.format.fromWedoDate

__ow.format.fromWedoDate(aWedoDate, aFormat) : String__

````
Shortcut for ow.format.fromDate but using a wedo date. See ow.format.fromDate for more help.  
(available after ow.loadFormat())
````
### ow.format.fromWedoDateToDate

__ow.format.fromWedoDateToDate(aWedoDate) : Date__

````
Returns a date object from a wedo date. (available after ow.loadFormat())
````
### ow.format.getActualTime

__ow.format.getActualTime(useAlternative) : Date__

````
Retrieves the current actual time from worldtimeapi.org (through https). The current actual time will be returned in a Date. If useAlternative = true it will use worldclockapi.com (through http)
````
### ow.format.getClasspath

__ow.format.getClasspath() : String__

````
Returns the current java classpath.
````
### ow.format.getCurrentDirectory

__ow.format.getCurrentDirectory() : String__

````
Returns the current working directory.
````
### ow.format.getDoH

__ow.format.getDoH(aAddr, aType, aProvider) : Array__

````
Performs a DNS over HTTPs query with aAddr. Optionally you can provide the aType of record (defaults to 'a') and the DNS over HTTPs aProvider between 'google' and 'cloudflare'.
````
### ow.format.getHostAddress

__ow.format.getHostAddress() : String__

````
Returns the current host ip address.
````
### ow.format.getHostName

__ow.format.getHostName() : String__

````
Returns the current hostname.
````
### ow.format.getJavaHome

__ow.format.getJavaHome() : String__

````
Returns the current java home directory.
````
### ow.format.getJavaVersion

__ow.format.getJavaVersion() : String__

````
Returns the current java version.
````
### ow.format.getOS

__ow.format.getOS() : String__

````
Returns the current operating system identifier string.
````
### ow.format.getOSArch

__ow.format.getOSArch() : String__

````
Returns the current operating system architecture string.
````
### ow.format.getOSVersion

__ow.format.getOSVersion() : String__

````
Returns the current operating system version string.
````
### ow.format.getPublicIP

__ow.format.getPublicIP() : Map__

````
Uses the functionality provided by http://ifconfig.co to return a map with the apparent current public ip address, public hostname and a guess of country and city. Please be aware of the request limits of the service (around 1 request per minute).
````
### ow.format.getReverseDoH

__ow.format.getReverseDoH(aIP, aProvider) : Array__

````
Tries to retrieve the reverse DNS of aIP using DNS over HTTPs. Optionally you can choose the aProvider between 'google' and 'cloudflare'.
````
### ow.format.getTLSCertificates

__ow.format.getTLSCertificates(aHost, aPort, withJava, aPath, aPass, aSoTimeout) : Array__

````
Tries to retreive the TLS certificates from aHost, aPort (defaults to 443). Optionally if withJava=true the original certificate Java object will also be included. If the CA certificates is in a different location you can provide aPath and the corresponding aPass. Additionally you can specificy aSoTimeout (socket timeout in ms) which defaults to 10s.
````
### ow.format.getTmpDir

__ow.format.getTmpDir() : String__

````
Returns the current temporary directory.
````
### ow.format.getUserHome

__ow.format.getUserHome() : String__

````
Returns the current user home path.
````
### ow.format.getUserName

__ow.format.getUserName() : String__

````
Returns the current user name.
````
### ow.format.int2IP

__ow.format.int2IP(aIPInt) : String__

````
Converts the decimal IP address representation aIPInt into an IP address.
````
### ow.format.IP2int

__ow.format.IP2int(aIP) : String__

````
Converts an IP address into it's decimal IP address representation.
````
### ow.format.isEmail

__ow.format.isEmail(aEmail) : boolean__

````
Tries to determine if aEmail seems a syntactic valid email.
````
### ow.format.isHost

__ow.format.isHost(aHost) : boolean__

````
Tries to determine if aHost seems a syntactic valid host.
````
### ow.format.isIPv4

__ow.format.isIPv4(aIP) : boolean__

````
Tries to determine if aIP is a syntactic valid IPv4.
````
### ow.format.isIPv6

__ow.format.isIPv6(aIP) : boolean__

````
Tries to determine if aIP is a syntactic valid IPv6.
````
### ow.format.isURL

__ow.format.isURL(aURL) : boolean__

````
Tries to determine if aURL seems a syntactic valid URL.
````
### ow.format.isWedoDate

__ow.format.isWedoDate(aWedoDate) : boolean__

````
Determines if the aWedoDate object is a wedo date type (returns true if yes, false otherwise).  
(available after ow.loadFormat())
````
### ow.format.isWindows

__ow.format.isWindows() : Boolean__

````
Returns true if the operating system is identified as Windows otherwise returns false.
````
### ow.format.logErrWithFooter

__ow.format.logErrWithFooter(aMessage, aFooter)__

````
Equivalent to ow.format.printWithFooter (see help ow.format.printWithFooter) using the logErr function.
````
### ow.format.logErrWithProgressFooter

__ow.format.logErrWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)__

````
Equivalent to ow.format.printWithProgressFooter (see help ow.format.printWithProgressFooter) using the logErr function.
````
### ow.format.logWarnWithFooter

__ow.format.logWarnWithFooter(aMessage, aFooter)__

````
Equivalent to ow.format.printWithFooter (see help ow.format.printWithFooter) using the logWarn function.
````
### ow.format.logWarnWithProgressFooter

__ow.format.logWarnWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)__

````
Equivalent to ow.format.printWithProgressFooter (see help ow.format.printWithProgressFooter) using the logWarn function.
````
### ow.format.logWithFooter

__ow.format.logWithFooter(aMessage, aFooter)__

````
Equivalent to ow.format.printWithFooter (see help ow.format.printWithFooter) using the log function.
````
### ow.format.logWithProgressFooter

__ow.format.logWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)__

````
Equivalent to ow.format.printWithProgressFooter (see help ow.format.printWithProgressFooter) using the log function.
````
### ow.format.logWithWaiting

__ow.format.logWithWaiting(aMainFunc, aPrefixMsg, aCompleteMsg, aErrorMsg, aWaitSpeed, aTheme)__

````
Executes aMainFunc while log aPrefixMsg with a waiting aTheme (defaults to a sequence of chars with a rotating bar). When aMainFunc ends it will replace the log with aCompleteMsg or aErrorMsg in case an exception is thrown. Optionally you can provide a different aWaitSpeed while cycling between the aTheme sequence of chars increasing/decreasing the "animation" effect.
````
### ow.format.percentile

__ow.format.percentile(aArray, aPercentile) : Number__

````
Will return the percentile (aPercentile between 0 and 1) for the provided aArray of numbers.
````
### ow.format.percProgressReport

__ow.format.percProgressReport(aMainFunc, aProgressFunc, aTimeout)__

````
Percentage progress report help function over a function on aMainFunc calling aProgressFunc in parallel with a percentage function parameter (receiving target and source numbers). You can also provide an alternative aTimeout between aProgressFunc calls (defaults to 150ms).

Example:

ow.format.percProgressReport(() => {
   ioStreamCopy(io.writeFileStream("target.file"), io.readFileStream("source.file"));
}, (percFunc) => {
	  var perc = percFunc(io.fileInfo("target.file").size, io.fileInfo("source.file").size);
   ...
});


````
### ow.format.printWithFooter

__ow.format.printWithFooter(aMessage, aFooter)__

````
Prints aMessage (if defined) with a aTemplate (template compiled function or string).
````
### ow.format.printWithProgressFooter

__ow.format.printWithProgressFooter(aMessage, aTemplate, aPerc, aSize, aUnixBlock, aWindowsBlock, aSpace)__

````
Prints aMessage (if defined) with a aTemplate (template compiled function or string) as a footer for percentage  progress information with the percentage value aPerc, for a given optional aSize (defaults to 50), an optional  aUnixBlock or aWindowsBlock (depending on the current operating system) and aSpace. Example:

   ow.loadTemplate();
   var fn = ow.template.execCompiled(ow.template.compile("({{percFormat}}%) progress: |{{progress}}|"));
   ow.format.printWithProgressFooter("processing xyz...", fn, aPerc);
   ow.format.printWithFooter("Done.", "");

````
### ow.format.printWithWaiting

__ow.format.printWithWaiting(aMainFunc, aPrefixMsg, aCompleteMsg, aErrorMsg, aWaitSpeed, aTheme, printNLFn, useAsSuffix)__

````
Executes aMainFunc while priting aPrefixMsg with a waiting aTheme (defaults to a sequence of chars with a rotating bar). When aMainFunc ends it will replace the priting with aCompleteMsg or aErrorMsg in case an exception is thrown. Optionally you can provide a different aWaitSpeed while cycling between the aTheme sequence of chars increasing/decreasing the "animation" effect.
````
### ow.format.progressReport

__ow.format.progressReport(aMainFunc, aProgressFunc, aTimeout)__

````
Executes aMainFunc to execute some synchronous function while aProgressFunc is called asynchronously to  keep track of progress. You can also provide an alternative aTimeout between aProgressFunc calls (defaults to 150ms).
````
### ow.format.round

__ow.format.round(aNumber, aDigits) : String__

````
Will return aNumber rounded to 0 decimal digits or aDigits decimal digits.
(available after ow.loadFormat())
````
### ow.format.semver

__ow.format.semver(aVersion) : ow.format.semver__

````
Creates a new instance of ow.format.semver for the provided aVersion:
  - nextMajor
  - nextMinor
  - nextPatch
  - getMajor
  - getMinor
  - getPatch
  - greater(aVersion)
  - lower(aVersion)
  - greaterEquals(aVersion)
  - lowerEquals(aVersion)
  - equals(aVersion)
````
### ow.format.sortSemanticVersions

__ow.format.sortSemanticVersions(aArray) : Array__

````
Will sort the provided aArray of semantic versions (e.g. 1.0.0, 1.0.1, 1.1.0, 2.0.0, ...)
(available after ow.loadFormat())
````
### ow.format.sqlFormat

__ow.format.sqlFormat(aSQL, aMap) : String__

````
Will format aSQL using the sql-formatter library. Optionally you can provide aMap with the following options:

  - indent: the indentation string (defaults to "  ")
  - uppercase: if true will uppercase the SQL (defaults to false)
  - linesBetweenQueries: number of lines between queries (defaults to 1)
  - maxColumnLength: maximum column length (defaults to 50)
  - skipWhitespaceNearBlockParentheses: if true will whitespace near block parentheses (defaults to false)
  - language: the SQL language dialect (defaults to "StandardSql")

The language can be one of the following:

  - Db2
  - MariaDb
  - MySql
  - N1ql
  - PlSql
  - PostgreSql
  - Redshift
  - SparkSql
  - StandardSql
  - TSql


````
### ow.format.sshProgress

__ow.format.sshProgress(aFn) : Object__

````
Returns a SSH Java progress monitor callback object to be use with the SSH plugin functions. Expects callback aFn that will be called with state (e.g. begin, count, end) and an Info map. The Info map is composed of:    source - the reported source of the transfer
   target - the reported target of the transfer
   op     - the operation being performed (get or put)
   start  - reported unix epoch when the transfer started
   end    - reported unix epoch when the transfer stopped
   count  - the last reported byte count
   speed  - the calculated speed of transfer

If the returned value is false the transfer will be cancelled.
````
### ow.format.streamHandle

__ow.format.streamHandle(aHandle, inHandle, errHandle, outHandle, bufferSize) : Function__

````
Returns a function to help automated interaction with a running process. The function aHandle receives: aType (in/err); aTxt,  inHandle (function), errHandle (function) and an outHandle (function). Optionally you can provide an alternative inHandle function to print stdout text, an errHandle function to print stderr text, an outHandle function to send text to stdin and/or a non default bufferSize.

Example:

var res = $sh("myProcess.sh --something")
          .cb(expect((aType, aTxt, inHandle, errHandle, outHandle) => {
             if (aType == "in") {
                inHandle(aTxt)
                if (/ name\?/.test(aTxt))                return outHandle("Scott\n")
               if (aTxt.indexOf("Anything else?") >= 0) return outHandle("nope!\n")
             }
          }))
          .get(0)


````
### ow.format.streamSH

__ow.format.streamSH(aFunction, anEncoding) : Function__

````
To be used with sh, af.sh or ssh.exec as the callbackFunc. Returns a function that will call aFunction for each line and used the returned string with print and printErr.
````
### ow.format.streamSHLog

__ow.format.streamSHLog(aFunction) : Function__

````
To be used with sh, af.sh or ssh.exec as the callbackFunc. Returns a function that will call aFunction for each line and used the returned string with log and logErr.
````
### ow.format.streamSHPrefix

__ow.format.streamSHPrefix(aPrefix, anEncoding, aSeparator, aTemplate, aFnHandler, infoFn, errorFn) : Function__

````
To be used with sh, af.sh or ssh.exec as the callbackFunc. Returns a function that will prefix each line with aPrefix and used the returned string with print and printErr. Optionally you can provide aTemplate to add "prefix" (defaults to "[{{prefix}}]") and/or provide aFnHandler to chain another streaming handling function (receives a stream and a boolean to indicate if its stdout or stderr). It's also possible to provide a infoFn and errorFn to handle the output. If infoFn or errorFn are not provided they will default to print and printErr or to log and logErr if __flags.SH.prefixLog is true.
````
### ow.format.string.ansiMoveDown

__ow.format.string.ansiMoveDown(nLines)__

````
Moves the cursor nLines down.
````
### ow.format.string.ansiMoveLeft

__ow.format.string.ansiMoveLeft(nChars)__

````
Moves the cursor left chars.
````
### ow.format.string.ansiMoveRight

__ow.format.string.ansiMoveRight(nChars)__

````
Moves the cursor right chars.
````
### ow.format.string.ansiMoveUp

__ow.format.string.ansiMoveUp(nLines)__

````
Moves the cursor nLines up.
````
### ow.format.string.ansiScrollDown

__ow.format.string.ansiScrollDown(nLines)__

````
Scrolls the screen down by nLines.
````
### ow.format.string.ansiScrollUp

__ow.format.string.ansiScrollUp(nLines)__

````
Scrolls the screen up by nLines.
````
### ow.format.string.bestPrefix

__ow.format.string.bestPrefix(aString, anArrayOfStrings) : aString__

````
Given anArrayOfStrings will try to find the best prefix string on that array for the provided aString. See ow.format.string.closest if you don't want to be based on the prefix.
Example:
var anArrayOfStrings = [ "/user", "/use", "/username", "/u" ];
ow.format.string.bestPrefix("/user/1", anArrayOfStrings); // Returns /user
ow.format.string.bestPrefix("/u1", anArrayOfStrings); // Returns /u
ow.format.string.bestPrefix("/userna", anArrayOfStrings); // Returns /user


````
### ow.format.string.bool

__ow.format.string.bool(aBoolValue, isLight, anExtra) : String__

````
Given aBoolValue will return a green checkmark or a red cross character. If necessary anExtra ansiColor attributes can be added.
````
### ow.format.string.chart

__ow.format.string.chart(aName, aDataPoint, aHSIze, aVSize, aMin, aMax, aTheme) : String__

````
Given data aName will store, between calls, aDataPoint provided to plot a chart with a horizontal aHSize and a vertical aVSize. Optionally aMin value and aMax value can be provided. aTheme can optionally also be provided containing the map entries space (char), bar (char), point (char), vertical (boolean) and axis (boolean)
````
### ow.format.string.closest

__ow.format.string.closest(aString, anArrayOfStrings, aThreshold) : aString__

````
Given anArrayOfStrings will try to find the closest string on that array for the provided aString. If aThreshold is not provided a default value of 3 will be used. See ow.format.string.bestPrefix if you want to be based on the prefix.
Example:
var anArrayOfStrings = [ "/user", "/use", "/username", "/u" ];
ow.format.string.closest("/user/1", anArrayOfStrings); // Returns /user
ow.format.string.closest("/u1", anArrayOfStrings); // Returns /u
ow.format.string.closest("/userna", anArrayOfStrings); // Returns /user
ow.format.string.closest("/usernam", anArrayOfStrings); // Returns /username
````
### ow.format.string.dataClean

__ow.format.string.dataClean(aName)__

````
Given aName for data points entered using ow.format.string.chart and ow.format.string.dataLineChart will effectively delete all cached data. If aName is not provided it will eliminate of cached data.
````
### ow.format.string.dataLineChart

__ow.format.string.dataLineChart(aName, aDataPoint, aHSIze, aVSize, aOptions) : String__

````
Given data aName will store, between calls, aDataPoint (number or array of numbers) provided to plot a line chart with a horizontal aHSize and a vertical aVSize. Optionally aOptions, equivalent to ow.format.string.lineChart options, can optionally also be provided.
````
### ow.format.string.distance

__ow.format.string.distance(aStringA, aStringB, maxOffset) : Number__

````
Calculates the distance between aStringA and aStringB into the number of inserts, deletions and updates needed. If the maxOffset is not provided a value of 5 maximum characters difference will be  used. (Currently based on Sift4)
````
### ow.format.string.genPass

__ow.format.string.genPass(aSize, aSets, aExclude, aWeights) : String__

````
Tries to generate a random password with aSize (defaults to 12) optionally given an array of aSets (between lowercase, uppercase, numbers, symbols and symbols2) and also aExclude a string of characters given an optional percentage of aWeights probability for each aSets.
````
### ow.format.string.getAstralCodePoint

__ow.format.string.getAstralCodePoint(aHighSurrogate, aLowSurrogate) : Number__

````
Given a 8-bit aHighSurrogate code and a 8-bit aLowSurogate code returns a 16-bit unicode code
````
### ow.format.string.getSurrogatePair

__ow.format.string.getSurrogatePair(astralCodePoint) : Array__

````
Returns an array of two 8 bit codes given an unicode astralCodePoint of 16 bits
````
### ow.format.string.grid

__ow.format.string.grid(aMatrix, aX, aY, aBgPattern, shouldReturn) : String__

````
Will generate a aX per aY grid to be displayed with aBgPattern (defaults to " "). Each grid cell with use the contents on aMatrix array of an array. Each cell content can be a map with obj (a Map), a xspan/yspan for in cell spacing, a type (either map, table, chart, area, bar, func or string)  and a title. If shouldReturn = true it will just return the string content instead of trying to print it.
Extra options per type:

 chart: the 'obj' check printChart format string
 bar  : the 'obj' check printBar format stirng; 'max'; 'min'; 'indicator'; 'space'


````
### ow.format.string.leftPad

__ow.format.string.leftPad(aString, length, padExpression) : String__

````
Using a padExpression will left pad aString for the given length.
````
### ow.format.string.lineChart

__ow.format.string.lineChart(aSeries, aOptions) : String__

````
Given an array of values (1 series) or an array of arrays of values (multiple series) will plot a line chart in  ascii, with the provided aOptions, a return the corresponding string. Available options:

  min     (number)   The minimum value to use in the chart
  max     (number)   The maximum value to use in the chart
  height  (number)   The line chart lines height to use
  width   (number)   The maxium width of the line chart
  colors  (array)    Array of color names to use for each series
  label   (boolean)  Boolean value to indicate if y labels should be included (default true)
  format  (function) Custom functions that receives a value and returns a formatted string for labels
  dColor  (string)   The default color to use
  offset  (number)   The offset to assume (default 2)
  padding (string)   The chart padding string (default "")
  fixed   (number)   If no custom format function is provided will be the fixed decimals to use (default 2)
  symbols (array)    An array of 10 characters to replace the default symbols

````
### ow.format.string.lineChartLegend

__ow.format.string.lineChartLegend(titles, options) : Array__

````
Given an array of titles and the options provided to ow.format.string.lineChart will return an array with each "symbol" and color used for each series and the corresponding "title".
````
### ow.format.string.lsHash

__ow.format.string.lsHash(aStringA, aStringB, dontCareDiffSize) : String__

````
Generates a locality sensitive hash for aStringA. If aStringB is provided it will compute the  hash difference between aStringA and aStringB returning a number (if 0 means the strings are almost identical; if 200 or higher means the strings are very different). Optionally you can indicate that the difference should care about differences in size dontCareDiffSize = true. This is based on https://github.com/trendmicro/tlsh/blob/master/js_ext.

Note: A aStringA and aStringB should be, at least, 512 characters long and have enough randomness to  generate a proper hash.
````
### ow.format.string.lsHashDiff

__ow.format.string.lsHashDiff(aHashA, aHashB, dontCareDiffSize) : String__

````
From a previously created, with ow.format.string.lsHash, aHashA and aHashB will calculate  the difference between them returning a number (if 0 means the strings are almost identical; if 200 or higher means the strings are very different). Optionally you can indicate that the difference should care about differences in size dontCareDiffSize = true. This is based on https://github.com/trendmicro/tlsh/blob/master/js_ext.
````
### ow.format.string.nLinesTemplate

__ow.format.string.nLinesTemplate(aSourceTemplate, initMap, alternativeTemplate, alternativePrintFunction) : Function__

````
Returns a function to print multiple lines at the same time (using ansi cursor up). The function accepts a map parameter since it's based on the aSourceTemplate (handlebars). The initial render is performed using initMap. If ansi support is not  available and if alternativeTemplate is defined (and different of "" otherwise it defaults to aSourceTemplate) it will use it as alternative. Optionally it's also possible to define a different print function (alternativePrintFunction) to print (like log, for example).
````
### ow.format.string.pauseString

__ow.format.string.pauseString(aString, aMsg)__

````
Given aString starts an interactive paging of the contents of aString.  Optionally aMsg can be provided to be displayed with the paging percentage (use \{{percentage}} to be replaced by the percentage).
````
### ow.format.string.printable

__ow.format.string.printable(aByteArray, aDefaultChar) : String__

````
Tries to convert aByteArray into a printable string. If aDefaultChar to replace the non-printable characters is not provided it will default to ".".
````
### ow.format.string.progress

__ow.format.string.progress(aNumericValue, aMax, aMin, aSize, aIndicator, aSpace) : String__

````
Outputs an in-line progress bar given aNumericValue, aMax value, aMin value, the aSize of the bar and the aIndicator to use. If not provided, aMax defaults to aValue, aMin defaults to 0, aSize defaults to the current screen width (or 5 if  if can be determined), aIndicator defaults to "#"  and aSpace defaults to " ". If aSize is a negative value and it's possible to determine the current screen width it will subtract to the screen width. Example:

loadLodash(); ow.loadFormat();
var arr = [-30, -25, -10, 0, 3, 5], max = _.max(arr), min = _.min(arr);
for(let i in arr) {
   print(ow.format.string.progress(arr[i], max, min, 5, '-'));
}


````
### ow.format.string.renderLines

__ow.format.string.renderLines(aMatrix, numberOfLines, aWidth, aBgPattern, shouldReturn) : String__

````
Tries to render a string grid (if shouldReturn = true won't print it but jsut return it) for a specific aWidth for a numberOfLines with aBgPattern background pattern (defaults to " ") with aMatrix contents (divided by "\n").
````
### ow.format.string.rightPad

__ow.format.string.rightPad(aString, length, padExpression) : String__

````
Using a padExpression will right pad aString for the given length.
````
### ow.format.string.separatorsToUnix

__ow.format.string.separatorsToUnix(aFilenamePath) : String__

````
Tries to convert the provided aFilenamePath into a path with unix folder separators.
````
### ow.format.string.separatorsToWindows

__ow.format.string.separatorsToWindows(aFilenamePath) : String__

````
Tries to convert the provided aFilenamePath into a path with windows folder separators.
````
### ow.format.string.tabExpand

__ow.format.string.tabExpand(aStr, aTabSize) : String__

````
Given an input aStr and, optionally, aTabSize will expand the tabs in the string to the provided aTabSize ( similar to the unix expand command).  If aTabSize is not provided it will default to 8.
````
### ow.format.string.toHex

__ow.format.string.toHex(aByteArray, aSeparator) : String__

````
Tries to convert aByteArray into a string of hex values separated by aSeparator (defaults to " ").
````
### ow.format.string.toHexArray

__ow.format.string.toHexArray(aByteArray, perLine) : String__

````
Returns an array with the ow.format.string.toHex of aByteArray and ow.format.string.printable with a maximum  of perLine (defaults to 30) characters per array element.
````
### ow.format.string.unicode

__ow.format.string.unicode(aCodeNumber) : String__

````
Given a unicode aCodeNumber (8 or 16 bits) will convert to the necessary sequence of 8 bit. For example: ow.format.string.unicode(0x1F37A)
````
### ow.format.string.updateLine

__ow.format.string.updateLine(aPrintNLFn) : Function__

````
Facilitates updating a message in the same line without entering new-lines. It will use the aPrintNLFn (if not defined uses printnl). Returns an object with two functions: line(aMessage) and end(). The function line() should be called to change the current line message. On the  end calling the function end() will clean-up a return the cursor to the beginning of the line.
````
### ow.format.string.wildcardRE

__ow.format.string.wildcardRE(aPattern, caseSensitive) : RegExp__

````
Given aPattern using '*' wildcards (to match zero or more characters) or '?' question-mark to match a single character will return the corresponding RegExp. Optionally if caseSensitive=true the RegExp will include case sensitive option.
````
### ow.format.string.wildcardTest

__ow.format.string.wildcardTest(aString, aPattern, caseSensitive) : Boolean__

````
Given aString will try to apply aPattern using '*' wildcards (to match zero or more characters) or '?' question-mark to match a single character. Will return true if the aPattern can be applied to aString. Optionally if caseSensitive=true the pattern will be tested with case sensitive.
````
### ow.format.string.wordWrap

__ow.format.string.wordWrap(aString, maxWidth, newLineSeparator, tabDefault) : String__

````
Given aString word wraps the text on it given the maxWidth length per line. Optionally you can provide a newLineSeparator otherwise '\n' will be used. Optionally tabDefault determines how many spaces a tab represents (default 4) (available after ow.loadFormat())
````
### ow.format.string.wordWrapArray

__ow.format.string.wordWrapArray(anArray, maxTableSize, sepLen, sepFunc, useIndex) : Array__

````
Given anArray of maps will return an array suitable to use with printTable for a maxTableSize, a separator length (sepLen (which defaults to 1)) and an optional line separator function (sepFunc that receives the max length of a  column). Word-wrap is achieved by creating new map array entries whenever the calculated max size of each line  with sepLen is achieved. The boolean flag useIndex changes the result to a map with lines and idx (array of the positions on the lines array that are a new anArray entry). Example of usage:

  __initializeCon()
  var maxS = __con.getTerminal().getWidth()
  print(printTable(ow.format.string.wordWrapArray(io.listFiles("js").files, maxS, 1, s => ansiColor("FAINT", repeat(s, "-"))), maxS))

````
### ow.format.testHost

__ow.format.testHost(aAddress, aTimeout) : Map__

````
Uses the java implementation (e.g. usually ICMP ping) for testing reachability to an aAddress. It timeouts after aTimeout (defaults to 4000ms). Returns a map with the "time" spent trying to get an answer from aAddress and a boolean "reachable" with the result.
````
### ow.format.testPort

__ow.format.testPort(aAddress, aPort, aCustomTimeout) : boolean__

````
Tries to connect to aPort (e.g. 1234) on aAddress (e.g. 1.2.3.4). If the connection is successfull it will disconnect and return true, otherwise it will return false. If aCustomTimeout (in ms) is defined, it will use that value as the timeout instead of the 1,5 seconds by default.
````
### ow.format.testPortLatency

__ow.format.testPortLatency(aHost, aPort, aCustomTimeout) : Number__

````
Test establishing a TCP socket connection with aHost on aPort. Optionally aCustomTimeout can be provided (defaults to 60000 ms). The test will be timed and the time in ms will be returned. If returned a time < 0 then an error occurred or the  host:port couldn't be reached.
````
### ow.format.testPublicPort

__ow.format.testPublicPort(aPort) : Map__

````
Uses the functionality provided by http://ifconfig.co to return a map with the result of testing if aPort is within public  reach from your apparent current public ip address. Please be aware of the request limits of the service (around 1 request per minute).
````
### ow.format.testURLLatency

__ow.format.testURLLatency(aURL, aCustomTimeout) : Number__

````
Test sending a HTTP(s) GET to aURL. Optionally aCustomTimeout can be provided. The test will be timed and the time in ms will be returned. If returned a time < 0 then an error occurred or the host:port couldn't be reached.
````
### ow.format.timeago

__ow.format.timeago(aDate, isAbv) : String__

````
Will output how much time ago aDate is (e.g. 2 years ago, 30 minutes ago, etc...).
Optionally isAbv = true for abbreviated output.  (available after ow.loadFormat())
````
### ow.format.toAbbreviation

__ow.format.toAbbreviation(aNumber, aDigits) : String__

````
Returns a number abbreviation to "k", "m", "b", "t". Will round number to 2 decimals if aDigits doesn't provide a different decimal digits to round to.
(available after ow.loadFormat())
````
### ow.format.toBase16

__ow.format.toBase16(aString) : String__

````
Given aString or array of bytes transforms the contents to base 16.
````
### ow.format.toBase32

__ow.format.toBase32(aString) : String__

````
Given aString or array of bytes transforms the contents to base 32.
````
### ow.format.toBase36

__ow.format.toBase36(aNumber, aLength) : String__

````
Converts a provided aNumber to the base36 representation. Optionally you can provide a length for 0 left pad.
````
### ow.format.toBinary

__ow.format.toBinary(aNumber, aLength) : String__

````
Converts a provided aNumber to the binary representation. Optionally you can provide a length for 0 left pad.
````
### ow.format.toBytesAbbreviation

__ow.format.toBytesAbbreviation(aNumber, aDigits) : String__

````
Returns a number abbreviation to "bytes", "KB", "MB", "GB", "TB", etc. Will round number to 3 significant digits if aDigits doesn't provide a different number of precision digits to convert to.
(available after ow.loadFormat())
````
### ow.format.toCSLON

__ow.format.toCSLON(aObj, cTheme) : String__

````
Equivalent to ow.fornat.toSLON but includes ansi color.
````
### ow.format.toDate

__ow.format.toDate(aStringDate, aFormat, aTimeZone) : Date__

````
Will convert aStringDate into a javascript Date given aFormat:

  G - Era descriptor (AD)
  y - Year (1996; 96)
  Y - Week year (2009; 09)
  M - Month in year (July; Jul; 07)
  w - Week in year (27)
  W - Week in month (2)
  D - Day in year (189)
  d - Day in month (10)
  F - Day of week in month (2)
  E - Day name in week (Tuesday; Tue)
  u - Day number of week (1 = Monday, ..., 7 = Sunday) (1)
  a - Am/pm number (PM)
  H - Hour in day (0-23)
  k - Hour in day (1-24)
  K - Hour in am/pm (0-11)
  h - Hour in am/pm (1-12)
  m - Minute in hour (30)
  s - Second in minute (55)
  S - Millisecond (978)
  z - Time zone (Pacific Standard Time; PST; GMT-08:00)
  Z - Time zone (-0800)
  X - Time zone (-08; -0800; -08:00)

Optionally you can also provide the original aTimeZone (like 'America/New_York', 'Europe/London', 'UTC', ...)
(available after ow.loadFormat())
````
### ow.format.toHex

__ow.format.toHex(aNumber, aLength) : String__

````
Converts a provided aNumber to the hexadecimal representation. Optionally you can provide a length for 0 left pad.
````
### ow.format.toLDAPDate

__ow.format.toLDAPDate(aDate) : Number__

````
Converts a javascript Date into a LDAP date (also known as Windows NT time format, Active Directory timestamps)
````
### ow.format.toNumberSpacing

__ow.format.toNumberSpacing(aNumber, aSpacer) : String__

````
Returns a number with aSpacer as thousands separator.
(available after ow.loadFormat())
````
### ow.format.toOctal

__ow.format.toOctal(aNumber, aLength) : String__

````
Converts a provided aNumber to the octal representation. Optionally you can provide a length for 0 left pad.
````
### ow.format.toSLON

__ow.format.toSLON(aObj, cTheme) : String__

````
Stringifies aObj into a Single Line Object Notation using a default scheme for human readability or a  custom cTheme map composed of:

   startMap "("
   sepMap   ", "
   endMap   ")"
   sepKV    ": "
   startArr "["
   sepArr   " | "
   endArr   "]"
   strQuote "'"


````
### ow.format.toUnixDate

__ow.format.toUnixDate(aDate) : Number__

````
Returns a unix timestamp from the provided javascript aDate.
````
### ow.format.toWedoDate

__ow.format.toWedoDate(aStringDate, aFormat) : Map__

````
Shortcut for using ow.format.toDate but converting the output into a wedo date.  
(available after ow.loadFormat())
````
### ow.format.transposeArrayLines

__ow.format.transposeArrayLines(anLineArray) : Array__

````
Given anLineArray transposes into a new array of lines.
````
### ow.format.unescapeHTML4

__ow.format.unescapeHTML4(aString) : String__

````
Uses Apache Commons Lang unescape HTML4 functionality to unconvert aString with HTML4 entities to the original string
````
### ow.format.withMD

__ow.format.withMD(aString, defaultAnsi) : String__

````
Use aString with simple markdown and convert it to ANSI. Optionally you can add a defaultAnsi string to return back  after applying the ansi styles for markdown (use ansiColor function to provide the defaultAnsi). Currently supports only: bold, italic, tables, simple code blocks, line rule, bullets, numbered lines, links and blocks.
````
### ow.format.withSideLine

__ow.format.withSideLine(aString, aSize, ansiLine, ansiText, aTheme, aExtra) : String__

````
Generates a ansi escaped line with a "left side line" to display aString which will be word-wrap given  aSize (default to the current console size). Optionally ansi colors for ansiLine and ansiText can be provided (see ansiColor for possible values) and aTheme (using ow.format.withSideLineThemes, for example). For closed rectangle themes aExtra map can include a header, footer, headerAlign ( left or right or center) and footerAlign (left or right or center).
````
### ow.format.xls.autoFilter

__ow.format.xls.autoFilter(aXLS, aXLSSheet, aRange)__

````
Applies a auto filter on the provided aXLS and aXLSSheet object (from XLS.getSheet) to aRange.

Example:

   ow.format.xls.autoFilter(sheet, "A1:D1");


````
### ow.format.xls.getStyle

__ow.format.xls.getStyle(aXLS, aStyleMap)__

````
Creates a cell styler object, for the aXLS object (XLS plugin object instance), given the provided aStyleMap. The aStyleMap can have the following keys to define a style:

  - bold (boolean)
  - italic (boolean)
  - underline (boolean)
  - strikeout (boolean)
  - fontPoints (number)
  - fontName (string)
  - fontColor (string)
  - wrapText (boolean)
  - shrinkToFit (boolean)
  - backgroundColor (string)
  - foregroundColor (string)
  - borderBottom (string)
  - borderLeft (string)
  - borderRight (string)
  - borderTop (string)
  - borderBottom (string)
  - borderLeftColor (string)
  - borderRightColor (string)
  - borderTopColor (string)
  - borderBottomColor (string)
  - rotation (number)
  - indention (number)
  - valign ("top", "bottom", "center", "justify")
  - align ("center", "centerSelection", "fill", "general", "justify", "left", "right")

Color names:\  
  aqua,auto,black,blue,blue_grey,bright_green,brown,coral,cornflower_blue,dark_blue,dark_green,dark_red,dark_teal, dark_yellow,gold,green,grey25,grey40,grey50,grey80,indigo,lavender,lemon_chiffon,light_blue,light_cornflower_blue, light_green,light_orange,light_turquoise,light_yellow,lime,maroon,olive_green,orange,orchid,pale_blue,pink,plum, red,rose,royal_blue,sea_green,sky_blue,tan,teal,turquoise,violet,white,yellow

Border names:

  dash_dot,dash_dot_dot,dashed,dotted,double,hair,medium,medium_dash_dot,medium_dash_dot_dot,medium_dashed,none, slanted_dash_dot,thick,thin

Fill patterns:

  solid_foreground


````
### ow.format.xls.setTable

__ow.format.xls.setTable(aXLS, aSheet, aColumn, aRow, anArray, shouldAutoFilter, headerStyle, linesStyle)__

````
Shortcut for xls.setTable that given aXLS object, a corresponding aSheet object will try to set the contents of  anArray of maps starting in aColumn and aRow performing auto size for all columns. If shouldAutoFilter = true is will also add an autofilter to all columns. It's possible also to customize the headerStyle and linesStyle.
````
