---
layout: default
title: xml
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## xml

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/XML.java) · [Baseline](../source-snapshot.md)

### XML.XML

`XML.XML(aXML) : XML`

````text
Creates a XML object instance. You can provide a string representation of an XML to instantiate the internal representation. NOTE: This plugin uses a DOM parser (all XML will be read into memory).
````

### XML.doc

`XML.doc() : Document`

````text
Returns the org.w3c.dom.Document object with the internal representation.
````

### XML.find

`XML.find(aXPathQuery) : Node`

````text
Returns an org.w3c.dom.Node object from the XPathQuery provided.
````

### XML.findAll

`XML.findAll(aXPathQuery) : NodeList`

````text
Returns a org.w3c.dom.NodeList object given the XPathQuery provided.
````

### XML.from

`XML.from(aXPathQuery) : Object`

````text
Returns an XMLBuilder2 object from the XPathQuery provided.
````

### XML.fromNodes2XML

`XML.fromNodes2XML(nodes) : Object`

````text
Given a Node (result of XML.find) or NodeList (result of XML.findAll) will return the corresponding representation in a E4X object.
````

### XML.get

`XML.get(aXPathQuery) : String`

````text
Returns the string value for the given XPathQuery provided.
````

### XML.toNativeXML

`XML.toNativeXML() : Object`

````text
Returns an E4X representation.
````

### XML.w

`XML.w() : String`

````text
Returns the internal representation into a XML string.
````

### XML.x

`XML.x(aRoot) : Object`

Starts a XMLBuilder2 object given a root element string. This code:

```javascript
plugin("XML");
plugin("Beautifiers");
var xml = new XML();
xml.x("test")
 .e("test1").a("status", "ok").a("language", "javascript")
  .e("path").a("type", "sharepath")
   .t("\\\\machine\\share\\test1")
  .up()
 .up()
 .e("test2").a("status", "ongoing").a("language", "python")
  .e("path").a("type", "URL")
   .t("http://some.url/test2");

print(beautify.xml(xml.w()));

var nodes = xml.findAll("/test/*");
for(var i = 0; i < nodes.getLength(); i++) {
  var name = nodes.item(i).getNodeName();
   var status = nodes.item(i).getAttributes().getNamedItem("status").getNodeValue();
   //var value = notes.item(i).getTextContent();
   print("name = " + name +
      "; status = " + status + "; " +
      "; " + xml.get("//" + name + "/path/@type") +
       " = " + xml.get("//" + name + "/path"));
}
```

will generate the following output:

```text
<test>
   <test1 language="javascript" status="ok">
       <path type="sharepath">\\machine\share\test1</path>
   </test1>
   <test2 language="python" status="ongoing">
      <path type="URL">http://some.url/test2</path>
   </test2>
</test>
name = test1; status = ok; ; sharepath = \\machine\share\test1
name = test2; status = ongoing; ; URL = http://some.url/test2
```
{% endraw %}
