---
layout: default
title: Prefer IPv6 over IPv4
parent: Beginner
grand_parent: Guides
---

# Prefer IPv6 over IPv4

OpenAF runs on Java (>= 8) which enables network connections both in IPv4 or IPv6. It's able to automatically use one or the other. But there will situations where both options are possible, would it be possible to force one of them over the other?

Yes, you just need to start OpenAF with a different Java option.

Let's take a simple example:

````bash
$ oaf -c "sprint(ow.loadNet().getPublicIP('dns.google').query)"
"8.8.8.8"
````

The name _dns.google_ was solved to IPv4 _8.8.8.8_.

Now let's set IPv6 as the prefered network stack:

````bash
$ export JDK_JAVA_OPTIONS="-Djava.net.preferIPv6Addresses=true"
$ oaf -c "sprint(ow.loadNet().getPublicIP('dns.google').query)"
Picked up JDK_JAVA_OPTIONS: -Djava.net.preferIPv6Addresses=true
"2001:4860:4860::8888"
````

The name dns.google now was solved to IPv6 _2001:4860:4860::8888_.

The reverse preference can also be acheived with:

````bash
$ export JDK_JAVA_OPTIONS="-Djava.net.preferIPv6Addresses=false"
````
