# Large Language Model (LLM) Configuration

OpenAF provides first-class support for Local Language Model (LLM) prompts via the `$llm` function in JavaScript jobs and the `oafp` CLI. You can configure which model to use by setting environment variables at runtime.

## Environment Variables

### OAF_MODEL

Used by the `$llm` function and OpenAF JavaScript APIs to select and configure a GPT model. If no explicit model is passed to `$llm()`, OpenAF will look at `OAF_MODEL` as a JSON or SLON string.

- Type: string (JSON/SLON) or simple `<type>` name
- Default key: `OAF_MODEL`

Examples:

```bash
# Full JSON configuration (SLON is also supported)
export OAF_MODEL='{ \
  type: "openai", \
  options: { 
    key: "YOUR_OPENAI_API_KEY", 
    model: "gpt-4", 
    temperature: 0.7 
  } 
}'

# Inline shorthand (must parse as a map)
export OAF_MODEL='{"type":"openai","options":{"key":"$OPENAI_KEY","model":"gpt-3.5-turbo"}}'
```

With `OAF_MODEL` set, you can use `$llm()` without arguments:

```javascript
// Inside an oJob or script
var response = $llm().prompt("Summarize the following text...");
print(response);
```  

You can still override at call time:

```javascript
var response = $llm({ type: "ollama", options: { model: "local-llama" } })
  .prompt("Analyze this data...");
```

### OAFP_MODEL

Used by the `oafp` command-line tool to drive prompts from your shell or pipelines. Set `OAFP_MODEL` in the same format as `OAF_MODEL`.

Examples:

```bash
# Use OpenAI via CLI
export OAFP_MODEL='(type: openai, options: (key: "$OPENAI_KEY", model: gpt-3.5-turbo, temperature: 0.5))'

# Use Gemini via CLI
export OAFP_MODEL='(type: gemini, options: (model: gpt-4o))'
```

Then run:

```bash
# Single prompt
oafp in=llm data="Translate this to French: Hello, world!"

# Prompt from stdin
printf "Write a poem about ${TOPIC}" | oafp in=llm
```

## Tips

- **Environment isolation**: Set these variables in your CI/CD or container environment to avoid hard-coding secrets.
- **SLON support**: OpenAF will parse SLON (Single Line Object Notation) if you prefer a more compact syntax.
- **Multiple providers**: You can switch providers by changing `type` (e.g. `openai`, `gemini`, `ollama`, `anthropic`).

## Reference Table: OAF_MODEL / OAFP_MODEL Fields

| Field         | Type     | Required | Description                                                                 | Provider Notes                                  |
|-------------- |----------|----------|-----------------------------------------------------------------------------|-------------------------------------------------|
| type          | string   | Yes      | Provider type (e.g. `openai`, `gemini`, `ollama`, `anthropic`, etc.)        | Must match supported provider                   |
| options       | map      | Yes      | Provider-specific options (see below)                                       | Structure varies by provider                    |
| conversation  | array    | No       | Initial conversation history (messages)                                     | OpenAI, Gemini, Anthropic, Ollama               |
| tools         | map      | No       | Tool definitions for function calling                                       | OpenAI, Gemini, Anthropic                       |
| timeout       | integer  | No       | Request timeout in milliseconds                                             | All                                            |
| noSystem      | boolean  | No       | If true, suppress system messages in output                                 | All                                            |
| instructions  | string/array | No   | Instructions for the model (e.g. `json`, `boolean`, `sql`, etc.)            | All                                            |
| headers       | map      | No       | Custom HTTP headers                                                         | All                                            |
| params        | map      | No       | Additional provider-specific parameters (e.g. `max_tokens`, `top_p`)        | OpenAI, Gemini, Anthropic, Ollama               |

**Provider-specific `options` fields:**

| Provider   | Option      | Type     | Required | Description                                  |
|------------|-------------|----------|----------|----------------------------------------------|
| openai     | key         | string   | Yes      | API key                                      |
| openai     | model       | string   | Yes      | Model name (e.g. `gpt-3.5-turbo`)            |
| openai     | temperature | float    | No       | Sampling temperature                         |
| openai     | url         | string   | No       | API endpoint (default: OpenAI)               |
| gemini     | key         | string   | No       | API key (if required)                        |
| gemini     | model       | string   | Yes      | Model name (e.g. `gemini-pro`)               |
| ollama     | model       | string   | Yes      | Model name (e.g. `llama2`)                   |
| ollama     | url         | string   | No       | Ollama server URL                            |
| anthropic  | key         | string   | Yes      | API key                                      |
| anthropic  | model       | string   | Yes      | Model name (e.g. `claude-3-opus-20240229`)   |
| ...        | ...         | ...      | ...      | ...                                          |

See provider documentation for more options.

## Advanced Usage Examples

### Using $llm with JSON Context

```javascript
// Pass a JSON context to the prompt
var context = {
  user: "Alice",
  data: [1, 2, 3, 4],
  task: "Summarize the numbers above."
};
var response = $llm().prompt(
  `Given the following context, provide a summary.\nContext: ${JSON.stringify(context)}`
);
print(response);
```

### Using $llm with Image Input

```javascript
// Prompt with an image (file path or base64)
var response = $llm().promptImage(
  "Describe the contents of this image.",
  "/path/to/image.png"
);
print(response);
```

### Using oafp CLI with JSON Context

```bash
# Pass JSON context as input
oafp in=llm data='{"context": {"user": "Bob", "numbers": [5,6,7]}, "prompt": "Summarize the numbers for the user."}'
```

### Using oafp CLI with Image Input

```bash
# Prompt with an image (path or base64)
oafp in=llm data='{"prompt": "What is in this image?", "image": "/path/to/image.jpg"}'
```

---

## Further Reading

- [oJob LLM Integration](../ojob.md#job-llm)
- [OpenWrap AI API Reference](../api/openaf.md#owai-gpt)
