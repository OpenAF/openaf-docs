---
layout: default
title: ow.ai
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.ai

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.ai.js) · [Baseline](../source-snapshot.md)

### $gpt

`$gpt(aModel) : $gpt`

Creates a GPT AI model from `aModel` (e.g. type "openai", "gemini", "ollama" or "anthropic").

`aModel` can be a map with the following properties:

- `type`: the type of the model (e.g. "openai", "ollama", "anthropic")
- `options`: a map with the options for the model (e.g. { key: "your-api-key", model: "gpt-3.5-turbo", temperature: 0.7, url: "https://api.openai.com/" })
- `conversation`: an array of messages to start the conversation (e.g. [{ role: "system", content: "You are a helpful assistant." }, { role: "user", content: "Hello!" }])
- `tools`: a map with the tools to use in the conversation (e.g. { "tool1": { type: "function", function: { name: "tool1", description: "A tool that does something", parameters: { type: "object", properties: { param1: { type: "string" } } } }, fn: function(args) { return args.param1; } } })
- `timeout`: the timeout for the requests in milliseconds (defaults to 15 minutes)
- `noSystem`: if true, it will not output the system messages (defaults to true)
- `instructions`: a string or an array of strings with the instructions for the model (e.g. "json", "boolean", "sql", "js", "path")
- `headers`: a map with the headers to use in the requests (e.g. { "Content-Type": "application/json" })
- `params`: a map with the parameters to use in the requests (e.g. { "max_tokens": 1000, "top_p": 1, "frequency_penalty": 0, "presence_penalty": 0 })
- `promptCaching`: when true adds Anthropic cache_control markers; no prompt-caching beta header is required (defaults to false)

For type "openai", options can also include:

- `decisionApi`: native decision contract ("openai" default, "openrouter", or "microsoft"). Microsoft requires mode "foundry" or "azure-foundry", API v1 and an explicit deployment name in model.
- `decisionUrl`: optional absolute HTTP(S) native decision endpoint override.
- `mode`: transport mode ("openai", "azure-openai-v1", "azure-openai-legacy" or "foundry").
- `apiVersion`: OpenAI-compatible API version path segment, or Azure legacy api-version query parameter. In Foundry mode, "v1" uses the /openai/v1 path; dated versions use the /models route with api-version. Defaults to "v1".
- `deployment`: Azure OpenAI legacy deployment name; defaults to model when omitted.
- `authType`: generated authentication header style ("bearer", "api-key" or "none"). Defaults to "bearer" for OpenAI mode and "api-key" for Azure/Foundry modes.

OpenAI-compatible examples:

- { type: "openai", key: "sk-...", url: "https://api.openai.com/v1", model: "gpt-4o-mini" }
- { type: "openai", key: "...", url: "https://RESOURCE.openai.azure.com", mode: "azure-openai-v1", model: "DEPLOYMENT" }
- { type: "openai", key: "...", url: "https://RESOURCE.openai.azure.com", mode: "azure-openai-legacy", deployment: "DEPLOYMENT", apiVersion: "2024-10-21" }
- { type: "openai", key: "...", url: "https://RESOURCE.services.ai.azure.com", mode: "foundry", model: "DEPLOYMENT" }
- { type: "openai", key: "...", url: "https://RESOURCE.services.ai.azure.com/models", mode: "foundry", apiVersion: "2024-05-01-preview", model: "DEPLOYMENT" }

If `aModel` is not provided, it will try to get the model from the environment variable "OAF_MODEL" with the map in JSON or SLON format.

The returned object also exposes helper methods to inspect vendor usage information: `getLastStats`/`lastStats` (map with the latest statistics), `promptWithStats`,
`promptJSONWithStats` and `rawPromptWithStats` (returning `{ response, stats }`). OpenAI compatible models can expose cached prompt tokens via `stats.tokens.cached`.

### $gpt.close

`$gpt.close()`

````text
Closes the current GPT model.
````

### $gpt.decide

`$gpt.decide(aState, aQuestions, aOptions) : Map`

````text
Returns a stateless versioned decision envelope. Also exposed through $llm. See ow.ai.gpt.decide and docs/llm-decisions.md.
````

### $gpt.decideWithStats

`$gpt.decideWithStats(aState, aQuestions, aOptions) : Map`

````text
Returns { response, stats } from one stateless decision execution.
````

### $gpt.exportConversation

`$gpt.exportConversation() : Array`

````text
Exports the current conversation in a standard portable format that can be imported into a different provider via importConversation().
````

### $gpt.getCapabilities

`$gpt.getCapabilities() : Map`

````text
Reports decision adapter support and runtime availability without a network request.
````

### $gpt.getEmbeddings

`$gpt.getEmbeddings(aInput, aDimensions, aEmbeddingModel) : Object`

````text
Gets text embeddings for aInput (string or array of strings) using aEmbeddingModel (defaults to provider-specific default). If aDimensions is specified, requests embeddings with that many dimensions (provider support varies). Returns the raw embedding response from the provider.
````

### $gpt.getEmbeddingsWithStats

`$gpt.getEmbeddingsWithStats(aInput, aDimensions, aEmbeddingModel) : Map`

````text
Gets text embeddings for aInput (string or array of strings) using aEmbeddingModel and returns both the response and usage statistics. If aDimensions is specified, requests embeddings with that many dimensions (provider support varies). Returns a map with { response, stats }.
````

### $gpt.getLastStats

`$gpt.getLastStats() : Map`

````text
Returns the latest usage statistics reported by the underlying LLM vendor for the last prompt request.
````

### $gpt.getModelInfo

`$gpt.getModelInfo(aModelId) : Map`

````text
Returns the model information for aModelId (defaults to the current configured model when omitted).
````

### $gpt.importConversation

`$gpt.importConversation(aExport) : $gpt`

````text
Imports a portable conversation previously exported via exportConversation() into this provider instance.
````

### $gpt.iniPrompt

`$gpt.iniPrompt(aPrompt, aRole, aModel, aTemperature) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) after cleaning the current conversation.
````

### $gpt.jsonSchemaPrompt

`$gpt.jsonSchemaPrompt(aPrompt, aResponseSchema, aModel, aTemperature, tools) : Object`

Executes a prompt using OpenAI's JSON Schema response format, enforcing structured output validated against `aResponseSchema`.

`aResponseSchema` should be a map with:

- `name` (string)
- `description` (string)
- `schema` (JSON Schema object)
- `strict` (boolean, defaults to true)

Gemini uses its provider-specific GenerateContent schema hook and supported schema subset; explicit nonempty `tools` are rejected.

Returns the parsed JSON response matching the provided schema.

Only supported by the `openai` provider.

### $gpt.jsonSchemaPromptWithStats

`$gpt.jsonSchemaPromptWithStats(aPrompt, aResponseSchema, aModel, aTemperature, tools) : Map`

````text
Executes jsonSchemaPrompt and returns the parsed response together with any reported statistics ({ response, stats }).
aResponseSchema should be a map with: name (string), description (string), schema (JSON Schema object), strict (boolean, defaults to true). Gemini uses its provider-specific GenerateContent schema hook and supported schema subset; explicit nonempty tools are rejected.
````

### $gpt.lastStats

`$gpt.lastStats() : Map`

````text
Alias for $gpt.getLastStats.
````

### $gpt.prompt

`$gpt.prompt(aPrompt, aRole, aModel, aTemperature, tools) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor).
````

### $gpt.promptBool

`$gpt.promptBool(aPrompt, aRole, aModel, aTemperature, tools) : boolean`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a boolean.
````

### $gpt.promptImage

`$gpt.promptImage(aPrompt, aImage, aDetailLevel, aRole, aModel, aTemperature, jsonFlag) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aImage (a file path or a base64 string representation), aRole (defaults to "user") and aModel (defaults to the one provided on the constructor). Images are prepared with ow.ai.prepareImage; detail semantics are unchanged. Constructor options imageMaxSide, imageMaxBytes, imageMaxPixels, imageFormat, imageQuality and imageBackground override preparation defaults; imageResize:false preserves original bytes. For the anthropic provider aImage can also be an array, and items can be maps { file | base64 | url, mediaType } to attach PDFs and text files (sent as document blocks); aDetailLevel is ignored.
````

### $gpt.promptImgGen

`$gpt.promptImgGen(aPrompt, aModel, aPath) : Array`

````text
Tries to prompt aPrompt and aModel (defaults to the one provided on the constructor) to generate one or more images and aPath to which the number of the image and ".png" will be saved to. Returns an array of the image files generated.
````

### $gpt.promptJSON

`$gpt.promptJSON(aPrompt, aModel, aTemperature)`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a Javascript function.
````

### $gpt.promptJSONWithStats

`$gpt.promptJSONWithStats(aPrompt, aModel, aTemperature)`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a map with the parsed JSON response and statistics ({ response, stats }).
````

### $gpt.promptJSONWithStatsRaw

`$gpt.promptJSONWithStatsRaw(aPrompt, aModel, aTemperature)`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a map with the raw response, parsed JSON response, and statistics ({ response, raw, stats }).
````

### $gpt.promptMD

`$gpt.promptMD(aPrompt, aRole, aModel, aTemperature, tools) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a markdown string.
````

### $gpt.promptPath

`$gpt.promptPath(aPrompt, aJSONSchemaDef, aModel, aTemperature)`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a JMESPath query.
````

### $gpt.promptSQL

`$gpt.promptSQL(aPrompt, aTableDefs, aDBName, aModel, aTemperature, tools)`

````text
Tries to prompt aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor) returning a SQL query.
````

### $gpt.promptStream

`$gpt.promptStream(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : String`

````text
Executes a streaming prompt, calling aOnDelta for each streamed chunk, and returns the aggregated response.
````

### $gpt.promptStreamJSON

`$gpt.promptStreamJSON(aPrompt, aRole, aModel, aTemperature, tools, aOnDelta) : Object`

````text
Executes a streaming JSON prompt and returns the parsed JSON response.
````

### $gpt.promptStreamJSONWithStats

`$gpt.promptStreamJSONWithStats(aPrompt, aRole, aModel, aTemperature, tools, aOnDelta) : Map`

````text
Executes a streaming JSON prompt and returns the parsed response with statistics ({ response, stats }).
````

### $gpt.promptStreamJSONWithStatsRaw

`$gpt.promptStreamJSONWithStatsRaw(aPrompt, aRole, aModel, aTemperature, tools, aOnDelta) : Map`

````text
Executes a streaming JSON prompt and returns the raw response, parsed response, and statistics ({ response, raw, stats }).
````

### $gpt.promptStreamWithStats

`$gpt.promptStreamWithStats(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : Map`

````text
Executes a streaming prompt and returns a map with the aggregated response and statistics ({ response, stats }).
````

### $gpt.promptWithStats

`$gpt.promptWithStats(aPrompt, aRole, aModel, aTemperature, tools) : Map`

````text
Executes prompt and returns a map with the response and the reported statistics ({ response, stats }).
````

### $gpt.rawDecide

`$gpt.rawDecide(aState, aQuestions, aOptions) : Map`

````text
Returns execution metadata and the raw provider payload from one stateless request.
````

### $gpt.rawPromptStream

`$gpt.rawPromptStream(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : Map`

````text
Executes a streaming prompt and returns the raw streaming payloads together with the aggregated response ({ content, events }).
````

### $gpt.rawPromptStreamWithStats

`$gpt.rawPromptStreamWithStats(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : Map`

````text
Executes a streaming prompt and returns the raw streaming payloads, aggregated response, and statistics ({ response, stats }).
````

### $gpt.rawPromptWithStats

`$gpt.rawPromptWithStats(aPrompt, aModel, aTemperature, aJsonFlag, tools) : Map`

````text
Executes the underlying rawPrompt call and returns the raw response together with the reported statistics ({ response, stats }).
````

### $gpt.setDebugCh

`$gpt.setDebugCh(aChName) : $gpt`

````text
Sets the debug channel name to aChName. When defined, creates an OpenAF channel and logs all requests and responses. Call with undefined to disable debug logging.
````

### $gpt.sysPrompt

`$gpt.sysPrompt(aPrompt, aModel, aTemperature) : String`

````text
Adds a prompt system aPrompt (a string or an array of strings) and aModel (defaults to the one provided on the constructor).
````

### $gpt.withA2aAgents

`$gpt.withA2aAgents(aA2aClient, aAgentIds) : ow.ai.gpt`

Automatically adds A2A agents from an MCP/A2A client to the current GPT instance as tools.
The `aA2aClient` should be an initialized `$mcp` client that supports agents/* methods.
If `aAgentIds` is provided (array of strings), only those specific agents will be added. Otherwise, all available agents are added.
Each A2A agent becomes a GPT tool where the tool call sends a message to the agent and returns its response.

Example:

```javascript
var a2aClient = $mcp({type: "remote", url: "http://localhost:8080/a2a"});
a2aClient.initialize();
var gpt = $gpt({type: "openai", options: {key: "your-key"}});
gpt.withA2aAgents(a2aClient); // Adds all A2A agents as tools
// or gpt.withA2aAgents(a2aClient, ["weather-agent", "translator-agent"]); // Adds only specific agents

var response = gpt.prompt("What's the weather in Lisbon?"); // GPT can call the weather-agent
```

### $gpt.withContext

`$gpt.withContext(anObject, aContext) : ow.ai.gpt`

````text
Adds a context to the current conversation.
````

### $gpt.withJSONAssert

`$gpt.withJSONAssert(aPath, anAssert) : ow.ai.gpt`

````text
Adds a JSON path aPath to be asserted with anAssert (e.g. isArray or isMap).
````

### $gpt.withMcpTools

`$gpt.withMcpTools(aMcpClient, aToolNames) : ow.ai.gpt`

Automatically adds MCP tools from an MCP client to the current GPT instance. The `aMcpClient` should be an initialized `$mcp` client.
If `aToolNames` is provided (array of strings), only those specific tools will be added. Otherwise, all available tools are added.
Each MCP tool will be converted to a GPT-compatible tool using the MCP tool's JSON schema.

Example:

```javascript
var mcpClient = $mcp({cmd: "npx @modelcontextprotocol/server-filesystem /tmp"});
mcpClient.initialize();
var gpt = $gpt({type: "openai", options: {key: "your-key"}});
gpt.withMcpTools(mcpClient); // Adds all MCP tools
// or gpt.withMcpTools(mcpClient, ["read_file", "write_file"]); // Adds only specific tools

var response = gpt.prompt("Read the file /tmp/example.txt");
```

### $gpt.withSQLTables

`$gpt.withSQLTables(aDBName, aTablesDefs) : ow.ai.gpt`

````text
Adds aDBName with aTableDefs to be used with promptSQL.
````

### $gpt.withTool

`$gpt.withTool(aName, aDesc, aParams, aFn) : ow.ai.gpt`

````text
Sets a tool with aName, aDesc (description), aParams (a json schema) and aFn (a javascript function tha receives a map according with the provided json schema and returns a map)
````

### ow.ai.agent

`ow.ai.agent(aOptions) : Map`

Creates a GPT-backed agent suitable for A2A (Agent-to-Agent) messaging.
Returns a map with 'meta' (agent metadata) and 'handler' (message handler function) ready for registration with `ow.server.a2a.registerAgent()`.

`aOptions` should contain:

- `id` (string, required) : Unique agent identifier
- `name` (string) : Display name (defaults to id)
- `title` (string) : Human-readable title (defaults to id)
- `version` (string) : Version string (defaults to "1.0.0")
- `tags` (array) : Array of categorization tags
- `capabilities` (map) : Map of agent capabilities (defaults to {messaging: true})
- `gpt` (required) : Either a `$gpt` instance or a config map for `$gpt` (e.g., {type: "openai", options: {key: "..."}})
- `systemPrompt` (string) : System message to guide the agent's behavior
- `tools` (array) : Array of tool names or definitions to add to the GPT instance

Example:

```javascript
var weatherAgent = ow.ai.agent({
  id: "weather-agent",
  name: "Weather Agent",
  gpt: {type: "openai", options: {key: "sk-..."}},
  systemPrompt: "You provide weather information concisely.",
  capabilities: {messaging: true, weatherData: true}
});

global.__a2a__ = new ow.server.a2a();
global.__a2a__.registerAgent(weatherAgent.meta, weatherAgent.handler);
```

### ow.ai.cluster

`ow.ai.cluster(args) : Object`

Wraps access to clustering of data. The result will be an object with a classify method that will
return the clustering result given the provided data. Args expects different arguments depending on type of
clustering:

- `args.type` (String) "kmeans" (default)
- `args.numberOfClusters` (Number) number of clusters to use (default to 5)
- `classify(normalizedData)` (Map) returns a map of centroids and cluster assignments

### ow.ai.decisionTree

`ow.ai.decisionTree(aMap) : Object`

Provides a wrapper to access the existing decision tree algorithms included:

ID3:

- `type`: `'id3'`
- `trainingSet` (array of maps) The training data
- `categoryAttr` (key name) The map key to build the decision tree on
- `ignoredAttributes` (array of keys) The list of keys to be ignored in each map

RandomForest:

- `type`: `'randomforest'`
- `trainingSet` (array of maps) The training data
- `categoryAttr` (key name) The map key to build the decision tree on
- `ignoredAttributes` (array of keys) The list of keys to be ignored in each map
- `treesNumber` (number) The number of decision trees to use

C45:

- `type`: `'c45'`
- `data` (array of arrays) The training data
- `features` (arrays of keys) The keys name by order of each array data value
- `featureTypes` (arrays of types) Categorization of each attribute between 'category' and 'number'
- `target` (key) The target key name (the last of each array data value)

### ow.ai.gpt

`ow.ai.gpt(aType, aOptions) : ow.ai.gpt`

Creates a GPT AI model of `aType` (e.g. "openai", "gemini", "ollama" or "anthropic") with `aOptions`.

Common `aOptions` properties include:

- `key`: provider API key when required.
- `model`: default model name or deployment name.
- `url`: provider base URL. For OpenAI defaults to "https://api.openai.com".
- `temperature`: default model temperature.
- `timeout`: request timeout in milliseconds (defaults to 15 minutes).
- `headers`: extra request headers. These override generated headers with the same names.
- `params`: extra request body parameters merged into prompt, image and embedding calls.
- `noSystem`: when true, system messages are converted to developer messages where supported (defaults to true).
- `schemaTransport`: explicit schema-hook transport, "responses" or "chat"; no automatic fallback. Tool-free calls default to Responses. Native-tool calls default to Responses on the official OpenAI endpoint and Chat Completions on compatible endpoints.
- `noResponseFormat`: when true, disables OpenAI-compatible JSON response_format injection.
- `promptCaching`: when true adds Anthropic cache_control markers; no prompt-caching beta header is required (defaults to false).

OpenAI-compatible transport options:

- `apiVersion`: API version/path segment for OpenAI-compatible routes (defaults to "v1"). In Azure legacy mode this becomes the api-version query parameter. In Foundry mode, "v1" uses the /openai/v1 path; dated versions use the /models route with api-version.
- `mode`: transport mode. Supported values are "openai" (default), "azure-openai-v1", "azure-openai-legacy" and "foundry". Aliases: "azure-v1", "azure-legacy" and "azure-foundry".
- `deployment`: deployment name for "azure-openai-legacy" mode. If omitted, the selected model name is used.
- `decisionApi`: native decision contract ("openai" default, "openrouter", or "microsoft"). Microsoft requires Foundry mode, API v1 and an explicit model deployment name.
- `decisionUrl`: optional absolute HTTP(S) native decision endpoint override.
- `authType`: authentication header style. Supported values are "bearer" (OpenAI default), "api-key" (Azure/Foundry default) and "none".

Examples:

- `OpenAI`: new `ow.ai.gpt("openai", { key: "sk-...", url: "https://api.openai.com/v1", model: "gpt-4o-mini" })`
- Azure OpenAI v1: new `ow.ai.gpt("openai", { key: "...", url: "https://RESOURCE.openai.azure.com", mode: "azure-openai-v1", model: "DEPLOYMENT" })`
- Azure OpenAI legacy: new `ow.ai.gpt("openai", { key: "...", url: "https://RESOURCE.openai.azure.com", mode: "azure-openai-legacy", deployment: "DEPLOYMENT", apiVersion: "2024-10-21" })`
- Azure AI Foundry v1: new `ow.ai.gpt("openai", { key: "...", url: "https://RESOURCE.services.ai.azure.com", mode: "foundry", model: "DEPLOYMENT" })`
- Azure AI Foundry dated API: new `ow.ai.gpt("openai", { key: "...", url: "https://RESOURCE.services.ai.azure.com/models", mode: "foundry", apiVersion: "2024-05-01-preview", model: "DEPLOYMENT" })`

Usage stats note: `getLastStats()` now includes OpenAI cached prompt tokens (`tokens.cached`) when reported by compatible models.

### ow.ai.gpt.addDeveloperPrompt

`ow.ai.gpt.addDeveloperPrompt(aPrompt) : ow.ai.gpt`

````text
Adds aPrompt (a string or an array of strings) with aRole (defaults to "developer") to the current conversation.
````

### ow.ai.gpt.addPrompt

`ow.ai.gpt.addPrompt(aPrompt, aRole) : ow.ai.gpt`

````text
Adds aPrompt (a string or an array of strings) with aRole (defaults to "user") to the current conversation.
````

### ow.ai.gpt.addSystemPrompt

`ow.ai.gpt.addSystemPrompt(aPrompt) : ow.ai.gpt`

````text
Adds aPrompt (a string or an array of strings) with aRole (defaults to "user") to the current conversation. For Gemini, large system instructions may be implicitly cached by the provider. For Anthropic, explicit cache markers are sent when `promptCaching` is enabled.
````

### ow.ai.gpt.addUserPrompt

`ow.ai.gpt.addUserPrompt(aPrompt) : ow.ai.gpt`

````text
Adds aPrompt (a string or an array of strings) with aRole (defaults to "user") to the current conversation.
````

### ow.ai.gpt.booleanPrompt

`ow.ai.gpt.booleanPrompt(aPrompt, aModel, aTemperature, tools) : boolean`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.gpt.cleanPrompt

`ow.ai.gpt.cleanPrompt() : ow.ai.gpt`

````text
Cleans the current conversation.
````

### ow.ai.gpt.codePrompt

`ow.ai.gpt.codePrompt(aPrompt, aModel, aTemperature, aCommentChars) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.gpt.decide

`ow.ai.gpt.decide(aState, aQuestions, aOptions) : Map`

````text
Evaluates text/JSON state with named choice, boolean and ordinal score questions. Returns contractVersion 1. Options: strategy (auto/native/structured), model, requireProbabilities, providerOptions, images (Ollama raw base64 or OpenAI inline image data URLs; native only). Stateless: ignores conversation and tools. Native probabilities are provider information, not calibrated correctness. Structured probability fields are null.
````

### ow.ai.gpt.decideWithStats

`ow.ai.gpt.decideWithStats(aState, aQuestions, aOptions) : Map`

````text
Returns { response, stats } from one execution with request-scoped usage. Missing usage remains absent.
````

### ow.ai.gpt.exportConversation

`ow.ai.gpt.exportConversation() : Array`

````text
Exports the current conversation as a portable, provider-neutral format array. Each entry contains: role ("system"|"user"|"assistant"), content (string|null), and optionally toolCalls and toolResults arrays. The exported format can be safely imported into a different provider via importConversation().
````

### ow.ai.gpt.getCapabilities

`ow.ai.gpt.getCapabilities() : Map`

````text
Returns implemented decision strategies, verified contracts and model availability (usually unknown). Does not contact the provider. Legacy adapters without hooks report unsupported decision strategies.
````

### ow.ai.gpt.getConversation

`ow.ai.gpt.getConversation() : Array`

````text
Returns the current conversation.
````

### ow.ai.gpt.getLastStats

`ow.ai.gpt.getLastStats() : Map`

````text
Returns the latest usage statistics reported by the underlying GPT model for the most recent prompt request (including provider-specific fields such as OpenAI cached prompt tokens and Anthropic cache read/creation tokens when available).
````

### ow.ai.gpt.importConversation

`ow.ai.gpt.importConversation(aExport) : ow.ai.gpt`

````text
Imports a portable conversation previously exported via exportConversation() into this provider, converting it to the provider's native internal format. Supports text turns and tool call/result turns.
````

### ow.ai.gpt.jsonPrompt

`ow.ai.gpt.jsonPrompt(aPrompt, aModel, aTemperature, tools) : Object`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.gpt.jsonPromptWithStats

`ow.ai.gpt.jsonPromptWithStats(aPrompt, aModel, aTemperature, tools) : Map`

````text
Executes jsonPrompt and returns the parsed response together with any reported statistics ({ response, stats }).
````

### ow.ai.gpt.jsonPromptWithStatsRaw

`ow.ai.gpt.jsonPromptWithStatsRaw(aPrompt, aModel, aTemperature, tools) : Map`

````text
Executes jsonPrompt and returns the raw response, parsed response, and statistics ({ response, raw, stats }).
````

### ow.ai.gpt.jsonSchemaPrompt

`ow.ai.gpt.jsonSchemaPrompt(aPrompt, aResponseSchema, aModel, aTemperature, tools) : Object`

Executes a prompt using OpenAI's JSON Schema response format, enforcing structured output validated against `aResponseSchema`.

`aResponseSchema` should be a map with:

- `name` (string)
- `description` (string)
- `schema` (JSON Schema object)
- `strict` (boolean, defaults to true)

Gemini uses its provider-specific GenerateContent schema hook and supported schema subset; explicit nonempty `tools` are rejected.

Returns the parsed JSON response matching the provided schema.

Only supported by the `openai` provider. Throws if the underlying provider does not implement `rawResponse`.

### ow.ai.gpt.jsonSchemaPromptWithStats

`ow.ai.gpt.jsonSchemaPromptWithStats(aPrompt, aResponseSchema, aModel, aTemperature, tools) : Map`

````text
Executes jsonSchemaPrompt and returns the parsed response together with any reported statistics ({ response, stats }).
aResponseSchema should be a map with: name (string), description (string), schema (JSON Schema object), strict (boolean, defaults to true). Gemini uses its provider-specific GenerateContent schema hook and supported schema subset; explicit nonempty tools are rejected.
````

### ow.ai.gpt.parseCode

`ow.ai.gpt.parseCode(anAnswer) : String`

````text
Tries to parse anAnswer and return the code between \``` and \```.
````

### ow.ai.gpt.pathPrompt

`ow.ai.gpt.pathPrompt(aPrompt, aJSONSchemaDef, aModel, aTemperature, tools) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.gpt.prompt

`ow.ai.gpt.prompt(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.gpt.promptImage

`ow.ai.gpt.promptImage(aPrompt, aImage, aDetailLevel, aRole, aModel, aTemperature, jsonFlag) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aImage (a file path or a base64 string representation), aRole (defaults to "user") and aModel (defaults to the one provided on the constructor). Images are prepared with ow.ai.prepareImage; detail semantics are unchanged. Constructor options imageMaxSide, imageMaxBytes, imageMaxPixels, imageFormat, imageQuality and imageBackground override preparation defaults; imageResize:false preserves original bytes. For the anthropic provider aImage can also be an array, and items can be maps { file | base64 | url, mediaType } to attach PDFs and text files (sent as document blocks); aDetailLevel is ignored.
````

### ow.ai.gpt.promptImgGen

`ow.ai.gpt.promptImgGen(aPrompt, aModel, anOutputPathPrefix) : Array`

````text
Tries to prompt aPrompt (a string or an array of strings), aModel (defaults to the one provided on the constructor) to generate one or more images and anOutputPathPrefix to which the number of the image and ".png" will be appended. Returns an array of the files generated.
````

### ow.ai.gpt.promptStream

`ow.ai.gpt.promptStream(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : String`

````text
Executes a streaming prompt, calling aOnDelta for each streamed chunk, and returns the aggregated response.
````

### ow.ai.gpt.promptStreamJSON

`ow.ai.gpt.promptStreamJSON(aPrompt, aRole, aModel, aTemperature, tools, aOnDelta) : Object`

````text
Executes a streaming JSON prompt and returns the parsed JSON response.
````

### ow.ai.gpt.promptStreamJSONWithStats

`ow.ai.gpt.promptStreamJSONWithStats(aPrompt, aRole, aModel, aTemperature, tools, aOnDelta) : Map`

````text
Executes a streaming JSON prompt and returns the parsed response with statistics ({ response, stats }).
````

### ow.ai.gpt.promptStreamJSONWithStatsRaw

`ow.ai.gpt.promptStreamJSONWithStatsRaw(aPrompt, aRole, aModel, aTemperature, tools, aOnDelta) : Map`

````text
Executes a streaming JSON prompt and returns the raw response, parsed response, and statistics ({ response, raw, stats }).
````

### ow.ai.gpt.promptStreamWithStats

`ow.ai.gpt.promptStreamWithStats(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : Map`

````text
Executes a streaming prompt and returns a map with the aggregated response and statistics ({ response, stats }).
````

### ow.ai.gpt.promptWithStats

`ow.ai.gpt.promptWithStats(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools) : Map`

````text
Executes prompt and returns a map with the model response and any reported statistics ({ response, stats }).
````

### ow.ai.gpt.prototype.getEmbeddings

`ow.ai.gpt.prototype.getEmbeddings(aInput, aDimensions, aEmbeddingModel) : Object`

````text
Gets text embeddings for aInput (string or array of strings) using aEmbeddingModel (defaults to provider-specific default). If aDimensions is specified, requests embeddings with that many dimensions (provider support varies). Returns the raw embedding response from the provider.
````

### ow.ai.gpt.prototype.getModelInfo

`ow.ai.gpt.prototype.getModelInfo(aModelId) : Map`

````text
Returns the model information for aModelId (defaults to the current configured model when omitted).
````

### ow.ai.gpt.prototype.getModelName

`ow.ai.gpt.prototype.getModelName() : String`

````text
Returns the default model name configured for this GPT instance.
````

### ow.ai.gpt.prototype.getModels

`ow.ai.gpt.prototype.getModels() : Array`

````text
Returns the available models from the GPT AI service.
````

### ow.ai.gpt.prototype.getType

`ow.ai.gpt.prototype.getType() : String`

````text
Returns the GPT provider type used to create this instance.
````

### ow.ai.gpt.rawDecide

`ow.ai.gpt.rawDecide(aState, aQuestions, aOptions) : Map`

````text
Returns { contractVersion, provider, model, strategy, raw } from one execution. Malformed answer content can be inspected, except requireProbabilities still validates coverage and probability semantics. Transport/API errors always throw.
````

### ow.ai.gpt.rawImgGen

`ow.ai.gpt.rawImgGen(aPrompt, aModel) : Map`

````text
Tries to generate an image based on aPrompt (a string or an array of strings) with aModel (defaults to the one provided on the constructor). Returns the raw result.
````

### ow.ai.gpt.rawPrompt

`ow.ai.gpt.rawPrompt(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.gpt.rawPromptStream

`ow.ai.gpt.rawPromptStream(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : Map`

````text
Executes a streaming prompt and returns the raw streaming payloads together with the aggregated response ({ content, events }).
````

### ow.ai.gpt.rawPromptStreamWithStats

`ow.ai.gpt.rawPromptStreamWithStats(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools, aOnDelta) : Map`

````text
Executes a streaming prompt and returns the raw streaming payloads, aggregated response, and statistics ({ response, stats }).
````

### ow.ai.gpt.rawPromptWithStats

`ow.ai.gpt.rawPromptWithStats(aPrompt, aRole, aModel, aTemperature, aJsonFlag, tools) : Map`

````text
Executes rawPrompt and returns the raw response together with any reported statistics ({ response, stats }).
````

### ow.ai.gpt.setConversation

`ow.ai.gpt.setConversation(aConversation) : ow.ai.gpt`

````text
Sets the current conversation to aConversation.
````

### ow.ai.gpt.setDebugCh

`ow.ai.gpt.setDebugCh(aChName) : ow.ai.gpt`

````text
Sets the debug channel name to aChName. When defined, creates an OpenAF channel and logs all requests and responses. Call with undefined to disable debug logging.
````

### ow.ai.gpt.setInstructions

`ow.ai.gpt.setInstructions(aType) : ow.ai.gpt`

````text
Sets the instructions for the current conversation. aType can be a string (e.g. json, boolean, sql, js and path) or an array of strings.
````

### ow.ai.gpt.setTool

`ow.ai.gpt.setTool(aName, aDesc, aParams, aFn) : ow.ai.gpt`

````text
Sets a tool with aName, aDesc (description), aParams (a json schema) and aFn (a javascript function tha receives a map according with the provided json schema and returns a map)
````

### ow.ai.gpt.sqlPrompt

`ow.ai.gpt.sqlPrompt(aPrompt, aTableDefs, aDBName, aModel, aTemperature, tools) : String`

````text
Tries to prompt aPrompt (a string or an array of strings) with aRole (defaults to "user") and aModel (defaults to the one provided on the constructor).
````

### ow.ai.network

`ow.ai.network(aMap) : ow.ai.network`

````text
Creates a neural network given the parameters in aMap. aMap should contain a "type" parameter to indicate the type of network (synaptic: perceptron, lstm, liquid or hopfield; brainjs: neuralnetwork, rnntimestep, lstmtimestep, grutimestep, rnn, lstm or gru).  Then aMap should contain a "args" parameter to provide each network inialization parameters. Please see "help ow.ai.network.[type of network]" for more details about each one.
````

### ow.ai.network.feedfoward

`ow.ai.network.feedfoward(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#neural-network-types)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.forecast

`ow.ai.network.forecast(aInput, aCount) : Array`

````text

````

### ow.ai.network.fromJson

`ow.ai.network.fromJson(aMap)`

````text
Tries to rebuild the network from aMap returned previously by a toJson function.
````

### ow.ai.network.get

`ow.ai.network.get(inputArray) : Array`

````text
Given an inputArray of decimal values, normalize between 0 and 1, will activate the current network and  return an output array of decimal values between 0 and 1.
````

### ow.ai.network.getBrainJSObject

`ow.ai.network.getBrainJSObject() : Object`

````text
Returns the current BrainJS object.
````

### ow.ai.network.getSynapticObject

`ow.ai.network.getSynapticObject() : Object`

````text
Returns the current Synaptic object.
````

### ow.ai.network.gru

`ow.ai.network.gru(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnn-lstm-and-gru)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.grutimestep

`ow.ai.network.grutimestep(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnntimestep-lstmtimestep-and-grutimestep)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.hopfield

`ow.ai.network.hopfield(args) : ow.ai.network`

````text
Hopfield serves as a content-addressable memory remembering patterns and when feed with new patterns the network returns the most similar one from the patterns it was trained to remember. You need to provide then number of input patterns args = [ 10 ].
````

### ow.ai.network.liquid

`ow.ai.network.liquid(args) : ow.ai.network`

````text
Liquid state machines are neural networks where neurons are randomly connected to each other. The recurrent nature of the connections turns the time varying input into a spatio-temporal pattern of activations in the network nodes. You need to provide args = [number of inputs, size of pool of neurons, number of outputs, number of random connections, number of random gates] (e.g. 2, 20, 1, 30, 10).
````

### ow.ai.network.lstm

`ow.ai.network.lstm(args) : ow.ai.network`

LSTM (Long short-term memory) are well-suited to learn from experience to classify, process and predict time series when
there are very long time lags of unknown size between important events. There is a minimum of 3 layers (input, memory block (input, memory cell, forget gate, output gate), output).
`args = [2, 6, 1]` means 2 input, 6 memory blocks, 1 output; `args = [2, 4, 4, 4, 1]` means 2 input neurons, 3 memory blocks and 1 output.

### ow.ai.network.lstmtimestep

`ow.ai.network.lstmtimestep(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnntimestep-lstmtimestep-and-grutimestep)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.neuralnetwork

`ow.ai.network.neuralnetwork(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-neuralnetwork)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.perceptron

`ow.ai.network.perceptron(args) : ow.ai.network`

````text
Perceptron or feed-forward neural networks. There is a minimum of 3 layers (input, hidden and output) and a any nmumber of hidden layers. args = [2, 3, 1] means 2 input neurons, 3 hidden neurons and 1 output neuron; args = [2, 10, 10, 10, 10, 1] means 2 input neurons, 4 layers of 10 neurons and 1 output neuron.
````

### ow.ai.network.put

`ow.ai.network.put(inputArray, outputArray, learningRate)`

````text
Given an inputArray of decimal values, normalize between 0 and 1, will activate the current network and then the outputArray of decimal values, normalize between 0 and 1, with an optionial learningRate (defaults to 0.3).
````

### ow.ai.network.readFile

`ow.ai.network.readFile(aFile)`

````text
Rebuilds a network from a map stored in aFile previously with ow.ai.network.writeFile.
````

### ow.ai.network.recurrent

`ow.ai.network.recurrent(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#neural-network-types)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.rnn

`ow.ai.network.rnn(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnn-lstm-and-gru)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.rnntimestep

`ow.ai.network.rnntimestep(args) : ow.ai.network`

- [Examples](https://github.com/BrainJS/brain.js?tab=readme-ov-file#examples)
- [Data format](https://github.com/BrainJS/brain.js?tab=readme-ov-file#for-training-with-rnntimestep-lstmtimestep-and-grutimestep)
- [Train](https://github.com/BrainJS/brain.js?tab=readme-ov-file#training-options)

### ow.ai.network.toJson

`ow.ai.network.toJson() : Map`

````text
Returns a map representation of the current network to be later rebuilt with the fromJson function.
````

### ow.ai.network.train

`ow.ai.network.train(trainingData, trainArgs)`

Trains the current network with the `trainingData` provided. `trainingData` should be an array of maps. Each
map entry should have a input and output keys. Each input and output entries should be an array for the
entry values and output values normalized to a decimal number between 0 and 1. Example:

```javascript
[{input: [0,0], output: [0]}, {input: [0,1], output: [1]}, {input: [1,0], output: [1]}, {input: [1,1], output :[0]}]
```

### ow.ai.network.writeFile

`ow.ai.network.writeFile(aFile)`

````text
Writes a compressed file with the map representation of the current network.
````

### ow.ai.normalize.denormalizeWithSchema

`ow.ai.normalize.denormalizeWithSchema(aMapOfNormalizedData, aMapSchema, convertBools) : Map`

````text
Tries to denormalize aMapOfNormalizedData (result from ow.ai.normalize.withSchema) according with aMapSchema provided.
````

### ow.ai.normalize.intArray

`ow.ai.normalize.intArray(anArray) : Array`

````text
Returns anArray where all numbers have been rounded to an integer value.
````

### ow.ai.normalize.quantitize

`ow.ai.normalize.quantitize(anArray, aLevels) : Array`

````text
Given anArray of numbers tries to quantitize returning an array of values between 0 and aLevels. If aLevels is not provided it will default to 10.
````

### ow.ai.normalize.scaleArray

`ow.ai.normalize.scaleArray(anArray, aMax, aMin) : Array`

````text
Given anArray of numbers tries to normalize returning an array of values between 0 and 1. If aMax or aMin are not provided they will be infered from the provided anArray.
````

### ow.ai.normalize.softMax

`ow.ai.normalize.softMax(anArray, aTemperature) : Array`

````text
Given anArray of numbers tries to apply a Softmax function returning an array of values between 0 and 1. If aTemperature is provided it will be used to control the smoothness of the output.
````

### ow.ai.normalize.toFeaturesArray

`ow.ai.normalize.toFeaturesArray(anArrayOfObjects, ignoredAttrs) : Map`

````text
Tries to convert anArrayOfObjects into an array of array of values where each value is positioned in the resulting array by the corresponding key sorted. The result will be a map with the resulting array in 'data' (with the features values ignoring any key on ignoredAttrs), the 'ignoredAttrs' and keys with all the 'keys' identified.
````

### ow.ai.normalize.withSchema

`ow.ai.normalize.withSchema(aSimpleMapOfData, aMapSchema, convertBools) : Array`

Tries to normalize and return `aSimpleMapOfData` normalized according with `aMapSchema` provided. Each element of `aMapSchema`
should be a map describing how to normalize `aSimpleMapOfData`. Example:

```javascript
var ar = [
   {name:'workout', duration:'120', enjoy: true, time:1455063275, tags:['gym', 'weights'], crucial: false },
   {name:'lunch', duration:'45', enjoy: false, time:1455063275, tags:['salad', 'wine'], crucial: true },
   {name:'sleep', duration:'420', enjoy: true, time:1455063275, tags:['bed', 'romance'], crucial: true}
];

var sar = {
   name    : { col: 0, oneOf: [ 'workout', 'lunch', 'sleep' ] },
   duration: { col: 1, min: 0, max: 1000 },
   enjoy   : { col: 2 },
   tags    : { col: 3, anyOf: [ 'gym', 'weights', 'salad', 'wine', 'bed', 'romance' ] },
   crucial : { col: 4, scaleOf: [
     { val: true,  weight: 0.85 },
     { val: false, weight: 0.15 }
   ]},
};

$from(ar).sort("time").select((r) => { return normalize(r, sar); });
```

### ow.ai.regression

`ow.ai.regression() : Regression`

Returns a Regression with the following functions:

- `linear(data, options)`: Map
- `power(data, options)`: Map
- `exponential(data, options)`: Map
- `logarithmic(data, options)`: Map
- `polynomial(data, options)`: Map

- `data`: an array of arrays of x, y values ([[0,1],[1,3],[2,5]])
- `options`: map to determine the order and precision ({ order: 2, precision: 5})

### ow.ai.valuesArray

`ow.ai.valuesArray(entriesspan) : Map`

Creates a valuesArray object with the following functions:

- `getValues()`: Array
- `push(value)`: void
- `deviation()`: Number
- `variance()`: Number
- `movingAverage()`: Number

- `entriesspan`: number of entries to keep
{% endraw %}
