---
layout: default
title: Jakarta XML Binding migration
parent: Advanced
grand_parent: Guides
---

{% raw %}
> Source: [openaf `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/docs/jakarta-xml-binding-migration.md). See [documentation baseline](../../source-snapshot.md) for availability and verification.

# Jakarta XML Binding migration

OpenAF now bundles Jakarta XML Binding API 4.0.5 instead of JAXB API 2.3.1. Scripts and oPacks that directly reference `javax.xml.bind` must migrate those references to `jakarta.xml.bind`. The `ow.format.string.toHex` interface remains unchanged.
{% endraw %}
