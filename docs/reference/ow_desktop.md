---
layout: default
title: ow.desktop
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.desktop

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.desktop.js) · [Baseline](../source-snapshot.md)

### ow.desktop.info

`ow.desktop.info() : Map`

````text
Returns session state, selected provider and actual capabilities. Does not start a toolkit.
````

### ow.desktop.registerProvider

`ow.desktop.registerProvider(aProvider)`

````text
Registers a provider implementing SPI version 1 before the desktop session starts. Providers expose describe, probe, start, request and stop. Used by optional oPacks and contract tests.
````

### ow.desktop.shutdown

`ow.desktop.shutdown() : oPromise`

````text
Stops only the desktop session and its owned helper/server. Idempotent.
````

### ow.desktop.start

`ow.desktop.start() : oPromise`

````text
Initializes the selected runtime and resolves to info(), including actual capabilities, without creating a window.
````

### ow.desktop.wait

`ow.desktop.wait(aTimeoutMs)`

````text
Keeps a standalone script alive until windows close, then shuts down desktop resources. An optional deadline raises TIMEOUT after cleanup. Do not call from a desktop callback.
````

### ow.desktop.window

`ow.desktop.window(aOptions) : Object`

````text
Creates a provider-neutral handle. Exactly one of html, url, file or a declarative view is required. Commands return oPromises; on/off subscribe to ready, message, closed and error events.
````
{% endraw %}
