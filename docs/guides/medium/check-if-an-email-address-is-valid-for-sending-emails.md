---
layout: default
title: Check if an email address is valid for sending emails
parent: Medium
grand_parent: Guides
---

# Check if an email address is valid for sending emails

A DNS lookup can report mail-related records for an email address's domain. It cannot prove that a mailbox exists or that a message will be delivered. This example reports DNS evidence without claiming address validity.

The [Google Public DNS JSON API](https://developers.google.com/speed/public-dns/docs/doh/json) accepts a domain name and record type. Request `MX` directly: an `ANY` query need not return every record type. The JSON `Status` field is the DNS response code, separate from the HTTP response status.

```javascript
function checkEmail(email) {
  _$(email, "email").check(v => isString(v) && /^[^\s@]+@[^\s@]+$/.test(v)).$_();
  var domain = email.substring(email.lastIndexOf("@") + 1);
  var response = $rest({ uriQuery: true, throwExceptions: true, timeout: 5000 })
    .get("https://dns.google/resolve", { name: domain, type: "MX" });
  var records = (response.Answer || []).filter(record => record.type === 15);
  return {
    domain: domain,
    dnsStatus: response.Status,
    mxRecords: records.map(record => record.data)
  };
}
```

Call `checkEmail("person@example.org")` with the address you want to inspect. Results depend on current DNS data; transport errors throw. An empty record list alone is not proof that the domain is nonexistent or that all mail delivery is impossible. The syntax check is deliberately basic and is not a complete email-address parser.

For direct DNS queries through OpenAF, see [`ow.net.getDNS`](../../reference/ow_net.md#ownetgetdns).
