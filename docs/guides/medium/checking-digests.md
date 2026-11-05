---
layout: default
title: Checking hash digests
parent: Medium
grand_parent: Guides
---

# Checking hash digests

(OpenAF version >= 20221216)

There are several hash algorithms. OpenAF through Java has functions for the most common algorithms:

````javascript
md5("hello world")    // 5eb63bbbe01eeed093cb22bb8f5acdc3
md2("hello world")    // d9cce882ee690a5c1ce70beff3a78c77
sha1("hello world")   // 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
sha256("hello world") // b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
sha384("hello world") // fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd
sha512("hello world") // 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f
````

This might be enough for most uses and the most compatible since all of the previous functions are supported even in Java 8. But there are improved hash algorithms that are only available in more recent or specific JVMs.

## Listing the supported hash algorithms

To list the algorithms that you current JVM + OpenAF support you can simply execute:

````javascript
ow.loadJava()
ow.java.getDigestAlgs()
// [ { provider: "SUN version 11", algorithm: "SHA3-512" }, ... ]
````

## Using a different hash algorithm

To use any of the algorithms listed previously you can execute something similar to:

````javascript
// Assuming we want to use SHA3-512
//
ow.java.digestAsHex("sha3-512", "hello world")
// 840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a
````

> Keep in mind that different JVM versions might not support the algorithm choosed so you will need to ensure your OpenAF code only uses an algorithm when it's available on the current provided list (with ow.java.getDigestAlgs)

## Including the algorithm with the digest

One common use given the multiple algorithms available is to include with the digest (the result of a hash function) the alogrithm use. This is usefull to later check if the result you have matches a specific input:

````javascript
ow.java.checkDigest("sha3-512:840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a", "hello world")
// true
````

## Checking files

Both the ow.java's digest functions and the base functions examplified in the first chapter support Java input streams:

````javascript
var is = io.readFileStream("afile.yaml")

sha512(is)
ow.java.digestAsHex("sha512", is)

is.close()
````
