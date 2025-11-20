---
layout: default
title: Modifying XML using E4X
parent: Medium
grand_parent: Guides
---

# Modifying XML using E4X

OpenAf uses the Java Mozilla Rhino javascript engine and one of the features that, despite being obsolete, has still been kept is E4X.

E4X simply allows for easy interaction and also modification of XML content in Javascript.

Let's start by the XML example used in "Accessing XML using E4X":

````xml
<shopcart>
  <!-- Client id -->
  <client type="personal" id="12345">
    <name>Joe Smith</name>
  </client>

  <!-- Store id -->
  <store>
    <id>12345</id>
    <type>diy</type>
  </store>

  <!-- Items on the shopcart -->
  <items>
    <item id="123">
       <qty>1</qty>
       <name>Item 1</name>
    </item>
    <item id="456">
       <qty>10</qty>
       <name>Item 2</name>
    </item>
  </items>
</shopcart>
````

Then you can load it to a _xml_ javascript variable through various ways:

````javascript
var xml = io.readFileXML("myxml.xml");
var xml = new XMLList(myXMLString);
var xml = <shopcart><!-- Client id --><client type="personal" id="12345">...
````

## Modifying data using the xml variable in javascript

Any element that you can access directly, you can change it:

````javascript
> xml.client.name.toString()
"Joe Smith"
> xml.client.name = "Scott Tiger"
"Scott Tiger"
> xml.client.name.toString()
"Scott Tiger"
````

Changing attributes:

````javascript
> xml.client.@id.toString()
"12345"
> xml.client.@id = "67890"
"67890"
> xml.client.@id.toString()
"67890"
````



And any comments are kept:

````javascript
> xml.toString()
<shopcart>
  <!-- Client id -->
  <client id="12345" type="personal">
    <name>Scott Tiger</name>
  </client>
  <!-- Store id -->
  <store>
    <id>12345</id>
...    
````

### Adding and removing children elements

To add you can simply think like an array:

````javascript
> xml.items.item[2] = <item id="789"><qty>2</qty><name>Item 3</name></item>
> xml.items.item.length()
3
````

And to remove a children element you can use _delete_:

````javascript
> delete xml.items.item[2]
> xml.items.item.length()
2
````

There are more methods to add or remove elements, like `appendChild(child)`, `prependChild(child)`, `insertChildAfter()`, and `insertChildBefore()`.

## XML Object methods

The E4X specification defines a rich set of methods to interact with XML objects. Here are some of the most common ones, grouped by modification and inspection

### Modification methods

| Method | Description |
|--------|-------------|
| `appendChild(child)` | Adds the `child` XML object at the end of the element's children. |
| `prependChild(child)` | Inserts a `child` XML object at the beginning of the element's children. |
| `insertChildAfter(childRef, childNew)` | Inserts `childNew` after `childRef`. |
| `insertChildBefore(childRef, childNew)` | Inserts `childNew` before `childRef`. |
| `replace(propertyName, value)` | Replaces the XML properties that match `propertyName` with `value`. |
| `setChildren(value)` | Replaces all children of the XML object with `value`. |
| `addNamespace(namespace)` | Adds a namespace to the XML object. |
| `removeNamespace(namespace)` | Removes a namespace from the XML object. |
| `setLocalName(name)` | Changes the local name of the XML object. |
| `setName(name)` | Changes the qualified name of the XML object. |
| `setNamespace(ns)` | Changes the namespace of the XML object. |

### Inspection methods

| Method | Description |
|--------|-------------|
| `attribute(attributeName)` | Returns the attribute that matches `attributeName`. |
| `attributes()` | Returns all attributes of the XML object. |
| `child(propertyName)` | Returns the children that match `propertyName`. |
| `children()` | Returns all children of the XML object. |
| `comments()` | Returns all comments in the XML object. |
| `copy()` | Returns a deep copy of the XML object. |
| `descendants(name)` | Returns all descendants of the XML object (optionally with a given `name`). |
| `elements(name)` | Returns the children of the XML object that are elements (optionally with a given `name`). |
| `hasComplexContent()` | Returns `true` if the XML object has child elements. |
| `hasSimpleContent()` | Returns `true` if the XML object has no child elements. |
| `inScopeNamespaces()` | Returns all in-scope namespaces. |
| `localName()` | Returns the local name of the XML object. |
| `name()` | Returns the qualified name of the XML object. |
| `namespace()` | Returns the namespace of the XML object. |
| `nodeKind()` | Returns the kind of the XML object (e.g. "element", "text", "comment"). |
| `parent()` | Returns the parent of the XML object. |
| `processingInstructions()` | Returns all processing instructions. |
| `text()` | Returns the text content of the XML object. |

For a complete list of methods and properties please refer to the [ECMA-357 specification](https://www.ecma-international.org/publications-and-standards/standards/ecma-357/).
