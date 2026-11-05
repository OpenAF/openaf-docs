---
layout: default
title: email
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## email

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/Email.java) · [Baseline](../source-snapshot.md)

### Email.addAttachment

`Email.addAttachment(aPath, isInline, noDisposition, aName) : Email`

````text
Adds aPath file as an attachment for the current email. Optionally you can specify if it's an inline (isInline) attachment; noDisposition = true to not set it as inline or attachment (ignores isInline); an internal aName.
````

### Email.addBcc

`Email.addBcc(aBccOrList) : Email`

````text
Sets the current email bcc email address or an array of bcc email addresses.
````

### Email.addCc

`Email.addCc(aCcOrList) : Email`

````text
Sets the current email cc email address or an array of cc email addresses.
````

### Email.addExternalImage

`Email.addExternalImage(aURL) : Email`

````text
Retrieves an external image from aURL and set's everything for that URL to be used in HTML.  Only available if the Email object was initialized with isHtml = true.
````

### Email.addHTMLHeader

`Email.addHTMLHeader() : Email`

````text
(deprecation) Please use the option in the constructor and the setHTML function. Adds the necessary headers to support HTML contents.  To be deprecated in the future. Please use new Email with isHTML = true and the setHTML function.
````

### Email.addHeader

`Email.addHeader(aKey, aValue) : Email`

````text
Add a SMTP header with aKey and the corresponding aValue.
````

### Email.addTo

`Email.addTo(aToOrList) : Email`

````text
Sets the current email "To" email address or an array of "To" email addresses.
````

### Email.email

`Email.email(aServer, aSenderAddress, shouldSecure, useTLS, isHTML)`

````text
Creates a Email object instance using the aServer SMTP server to send email with the from field set to aSenderAddress. Optionally you can specify if a secure protocol (SSL) should be used with shouldSecure = true, to TLS add shouldSecure = true and useTLS = true and isHTML to use the setHTML function later.
````

### Email.embedFile

`Email.embedFile(aFilePath, aName) : Email`

````text
Tries to embed aFilePath with aName and returns the cid to be used in HTML (e.g. img src="cid:xxx").  Only available if the Email object was initialized with isHtml = true.
````

### Email.embedURL

`Email.embedURL(aURL, aName) : Email`

````text
Tries to embed aURL with aName and returns the cid to be used in HTML (e.g. img src="cid:xxx").  Only available if the Email object was initialized with isHtml = true.
````

### Email.getEmailObj

`Email.getEmailObj() : JavaObject`

````text
Returns the internal Java object used to composed the email message for advance usage. See more in https://commons.apache.org/proper/commons-email/apidocs/org/apache/commons/mail/Email.html.
````

### Email.login

`Email.login(aLogin, aPassword)`

````text
Sets the credentials to use when using a SMTP server which activates the use of a secure protocol (TLS/SSL) if available.
````

### Email.send

`Email.send(aSubject, aMessage, aToList, aCCList, aBCCList, aSender) : String`

````text
Sends an email with aSubject and aMessage to the provided array of aToList, aCCList and aBCCList. Optionally you can specify a from address in aSender, otherwise the default for this object instance will be used. Returns the id of the message sent.
````

### Email.setCharset

`Email.setCharset(aCharset) : Email`

````text
Sets the current email aCharset to use.
````

### Email.setContent

`Email.setContent(aContent, aContentType) : Email`

````text
Sets the current email body message to send with aContent string. Specifies also that the corresponding  content type is aContentType.
````

### Email.setCredentials

`Email.setCredentials(aLogin, aPassword)`

````text
Sets the credentials to use when using a SMTP server which activates the use of a secure protocol (TLS/SSL) if available.
````

### Email.setFrom

`Email.setFrom(aFrom) : Email`

````text
Sets the current email aFrom email address.
````

### Email.setHTML

`Email.setHTML(aHTML) : Email`

````text
If the Email object was initialized with isHtml = true then will set the HTML content to aHTML.
````

### Email.setMessage

`Email.setMessage(aMessage) : Email`

````text
Sets the current email body message to send (raw). Please use Email.setContent to specify the mime type. For  emails initialized with isHtml = true, sets the alternative text content to show.
````

### Email.setPort

`Email.setPort(aPort)`

````text
Sets aPort to contact the SMTP server.
````

### Email.setSubject

`Email.setSubject(aSubject) : Email`

````text
Sets the email's aSubject;
````
{% endraw %}
