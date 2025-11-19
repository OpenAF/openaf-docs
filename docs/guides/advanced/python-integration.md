---
layout: default
title: Python Integration
parent: Advanced
grand_parent: Guides
---

# Python Integration with OpenAF

OpenAF provides seamless integration with Python, allowing you to execute Python code from within OpenAF scripts and oJobs, and vice versa. This enables you to leverage Python libraries and tools alongside OpenAF's automation capabilities.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

OpenAF's Python integration enables:
- **Execute Python code** from OpenAF/JavaScript
- **Call Python functions** with parameter passing
- **Use Python libraries** (NumPy, Pandas, scikit-learn, etc.)
- **Bidirectional data exchange** between JavaScript and Python
- **oJob Python execution** with language integration

### Use Cases

- Data science and machine learning workflows
- Use Python libraries for specialized tasks
- Integrate existing Python scripts into OpenAF automation
- Leverage Python's scientific computing ecosystem
- Cross-language data processing pipelines

---

## Prerequisites

### Install Python

Ensure Python 3.x is installed and accessible:

```bash
python3 --version
# or
python --version
```

### Install Required Packages

For basic integration, Python 3.x is sufficient. For advanced features, install:

```bash
pip install numpy pandas
```

---

## Basic Python Execution

### Execute Python Code

```javascript
// Simple Python execution
var result = af.runFromExternalClass("python", `
print("Hello from Python!")
print(2 + 2)
`);

print(result);
```

### Execute Python with Return Value

```javascript
// Python code that returns JSON
var pythonCode = `
import json

data = {
    "message": "Hello from Python",
    "value": 42,
    "items": [1, 2, 3, 4, 5]
}

print(json.dumps(data))
`;

var output = af.runFromExternalClass("python", pythonCode);
var result = jsonParse(output);

print("Message: " + result.message);
print("Value: " + result.value);
print("Items: " + result.items);
```

---

## Using ow.python Module

### Load the Module

```javascript
ow.loadPython();
```

### Execute Python Scripts

```javascript
ow.loadPython();

// Execute Python code
var result = ow.python.exec(`
def calculate(x, y):
    return x ** y

result = calculate(2, 10)
print(result)
`);

print("Result: " + result);
```

### Python with Arguments

```javascript
ow.loadPython();

var x = 5;
var y = 3;

var pythonCode = `
import sys
import json

# Read arguments
args = json.loads(sys.argv[1])
x = args['x']
y = args['y']

# Calculate
result = x + y

# Return as JSON
print(json.dumps({'sum': result}))
`;

var result = ow.python.exec(pythonCode, {
    args: { x: x, y: y }
});

var data = jsonParse(result);
print("Sum: " + data.sum);
```

---

## Data Exchange Patterns

### JavaScript to Python

```javascript
ow.loadPython();

// Prepare data in JavaScript
var data = {
    numbers: [1, 2, 3, 4, 5],
    operation: "sum"
};

// Pass to Python
var pythonCode = `
import sys
import json

data = json.loads(sys.argv[1])
numbers = data['numbers']
operation = data['operation']

if operation == 'sum':
    result = sum(numbers)
elif operation == 'product':
    result = 1
    for n in numbers:
        result *= n
else:
    result = None

print(json.dumps({'result': result}))
`;

var output = ow.python.exec(pythonCode, {
    args: data
});

var result = jsonParse(output);
print("Result: " + result.result);
```

### Python to JavaScript

```javascript
ow.loadPython();

var pythonCode = `
import json

# Python data structure
data = {
    'users': [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ],
    'total': 3
}

# Return as JSON
print(json.dumps(data))
`;

var output = ow.python.exec(pythonCode);
var data = jsonParse(output);

// Use in JavaScript
data.users.forEach(user => {
    print(user.name + " is " + user.age + " years old");
});
```

---

## oJob Python Integration

### Execute Python in oJob

```yaml
jobs:
  - name: Python Job
    lang: python
    exec: |
      # Python code in oJob
      import json

      # Access args from oJob
      name = "{{name}}"
      age = {{age}}

      # Python logic
      message = f"Hello {name}, you are {age} years old"

      # Return data (will be in args for next job)
      result = {
          "message": message,
          "valid": age >= 18
      }

      print(json.dumps(result))

  - name: Process Result
    deps:
      - Python Job
    exec: |
      // JavaScript job processing Python result
      log("Python said: " + args.message);
      log("Valid: " + args.valid);

todo:
  - name: Python Job
    args:
      name: Alice
      age: 25
  - Process Result
```

### Python with File Processing

```yaml
jobs:
  - name: Process CSV with Python
    lang: python
    exec: |
      import pandas as pd
      import json

      # Read CSV
      df = pd.read_csv('{{csvFile}}')

      # Process data
      summary = {
          'total_rows': len(df),
          'columns': list(df.columns),
          'numeric_summary': df.describe().to_dict()
      }

      # Return result
      print(json.dumps(summary))

  - name: Display Results
    deps:
      - Process CSV with Python
    exec: |
      log("Total rows: " + args.total_rows);
      log("Columns: " + args.columns);

todo:
  - name: Process CSV with Python
    args:
      csvFile: ./data/sales.csv
  - Display Results
```

---

## Common Patterns

### Pattern 1: Data Analysis with Pandas

```yaml
include:
  - oJobBasics.yaml

jobs:
  - name: Analyze Sales Data
    lang: python
    exec: |
      import pandas as pd
      import json

      # Load data
      df = pd.read_csv('sales.csv')

      # Analysis
      total_sales = float(df['amount'].sum())
      avg_sales = float(df['amount'].mean())
      top_products = df.groupby('product')['amount'].sum().nlargest(5).to_dict()

      # Return analysis
      result = {
          'total_sales': total_sales,
          'average_sale': avg_sales,
          'top_products': top_products
      }

      print(json.dumps(result))

  - name: Generate Report
    deps:
      - Analyze Sales Data
    exec: |
      log("Sales Analysis Report");
      log("===================");
      log("Total Sales: $" + args.total_sales);
      log("Average Sale: $" + args.average_sale);
      log("Top Products:");

      Object.keys(args.top_products).forEach(product => {
        log("  " + product + ": $" + args.top_products[product]);
      });

todo:
  - Analyze Sales Data
  - Generate Report
```

### Pattern 2: Machine Learning Predictions

```yaml
jobs:
  - name: Train Model
    lang: python
    exec: |
      from sklearn.linear_model import LinearRegression
      import numpy as np
      import pickle
      import json

      # Training data
      X = np.array([[1], [2], [3], [4], [5]])
      y = np.array([2, 4, 6, 8, 10])

      # Train model
      model = LinearRegression()
      model.fit(X, y)

      # Save model
      with open('model.pkl', 'wb') as f:
          pickle.dump(model, f)

      print(json.dumps({'status': 'trained', 'score': model.score(X, y)}))

  - name: Make Predictions
    deps:
      - Train Model
    lang: python
    exec: |
      import pickle
      import numpy as np
      import json

      # Load model
      with open('model.pkl', 'rb') as f:
          model = pickle.load(f)

      # Make predictions
      X_new = np.array([[6], [7], [8]])
      predictions = model.predict(X_new).tolist()

      result = {
          'predictions': predictions
      }

      print(json.dumps(result))

  - name: Display Predictions
    deps:
      - Make Predictions
    exec: |
      log("Predictions:");
      args.predictions.forEach((pred, idx) => {
        log("  Input " + (idx + 6) + ": " + pred);
      });

todo:
  - Train Model
  - Make Predictions
  - Display Predictions
```

### Pattern 3: Image Processing

```yaml
jobs:
  - name: Process Image
    lang: python
    exec: |
      from PIL import Image
      import json

      # Open image
      img = Image.open('{{inputImage}}')

      # Get info
      info = {
          'width': img.width,
          'height': img.height,
          'format': img.format,
          'mode': img.mode
      }

      # Resize
      img_resized = img.resize((800, 600))
      img_resized.save('{{outputImage}}')

      print(json.dumps(info))

todo:
  - name: Process Image
    args:
      inputImage: ./photos/original.jpg
      outputImage: ./photos/resized.jpg
```

### Pattern 4: Web Scraping

```yaml
jobs:
  - name: Scrape Website
    lang: python
    exec: |
      import requests
      from bs4 import BeautifulSoup
      import json

      # Fetch page
      response = requests.get('{{url}}')
      soup = BeautifulSoup(response.content, 'html.parser')

      # Extract data
      titles = [h2.text.strip() for h2 in soup.find_all('h2')]

      result = {
          'url': '{{url}}',
          'titles': titles,
          'count': len(titles)
      }

      print(json.dumps(result))

  - name: Process Scraped Data
    deps:
      - Scrape Website
    exec: |
      log("Found " + args.count + " titles from " + args.url);
      args.titles.forEach(title => log("  - " + title));

todo:
  - name: Scrape Website
    args:
      url: https://example.com
  - Process Scraped Data
```

### Pattern 5: API Integration

```yaml
jobs:
  - name: Call Python API
    lang: python
    exec: |
      import requests
      import json

      # API call
      response = requests.post('{{apiUrl}}', json={{requestData}})

      # Parse response
      data = response.json()

      # Return
      print(json.dumps(data))

todo:
  - name: Call Python API
    args:
      apiUrl: https://api.example.com/predict
      requestData:
        features: [1.2, 3.4, 5.6]
        model: v2
```

---

## Advanced Techniques

### Streaming Data Processing

```javascript
ow.loadPython();

// Process large dataset in chunks
var pythonCode = `
import pandas as pd
import json

# Read in chunks
chunk_size = 1000
chunks = pd.read_csv('large_file.csv', chunksize=chunk_size)

results = []
for chunk in chunks:
    # Process chunk
    chunk_sum = chunk['value'].sum()
    results.append(chunk_sum)

total = sum(results)
print(json.dumps({'total': total, 'chunks': len(results)}))
`;

var result = ow.python.exec(pythonCode);
var data = jsonParse(result);
log("Processed " + data.chunks + " chunks, total: " + data.total);
```

### Virtual Environment Support

```javascript
// Use specific Python virtual environment
var pythonCode = `
import sys
sys.path.insert(0, '/path/to/venv/lib/python3.9/site-packages')

import custom_library
# Use library
`;

var result = af.runFromExternalClass("python", pythonCode);
```

### Error Handling

```yaml
jobs:
  - name: Safe Python Execution
    exec: |
      try {
        var pythonCode = `
import sys
import json

try:
    # Risky operation
    result = 10 / 0
    print(json.dumps({'result': result}))
except Exception as e:
    print(json.dumps({'error': str(e)}))
`;

        var output = af.runFromExternalClass("python", pythonCode);
        var result = jsonParse(output);

        if (isDef(result.error)) {
          logErr("Python error: " + result.error);
          throw result.error;
        }

        log("Result: " + result.result);

      } catch(e) {
        logErr("Execution failed: " + e.message);
      }
```

---

## Environment Variables

### Pass Environment to Python

```yaml
jobs:
  - name: Python with Env
    lang: python
    exec: |
      import os
      import json

      # Access environment variables
      api_key = os.getenv('API_KEY', 'default_key')
      debug = os.getenv('DEBUG', 'false').lower() == 'true'

      result = {
          'api_key_set': api_key != 'default_key',
          'debug': debug
      }

      print(json.dumps(result))

todo:
  - Python with Env
```

Run with:
```bash
API_KEY=mykey123 DEBUG=true ojob myjob.yaml
```

---

## Performance Considerations

### Minimize Python Calls

```javascript
// Bad - multiple Python calls
for (var i = 0; i < 100; i++) {
  var result = af.runFromExternalClass("python", `print(${i} * 2)`);
}

// Good - single Python call
var pythonCode = `
results = [i * 2 for i in range(100)]
import json
print(json.dumps(results))
`;
var results = jsonParse(af.runFromExternalClass("python", pythonCode));
```

### Batch Processing

```yaml
jobs:
  - name: Batch Process
    lang: python
    exec: |
      import json

      # Process all items at once
      items = {{items}}

      results = []
      for item in items:
          result = process_item(item)
          results.append(result)

      print(json.dumps(results))

todo:
  - name: Batch Process
    args:
      items: [1, 2, 3, 4, 5]
```

---

## Complete Example: Data Pipeline

```yaml
include:
  - oJobBasics.yaml

jobs:
  # Extract data
  - name: Extract Data
    exec: |
      ow.loadObj();

      var data = $rest()
        .get("https://api.example.com/data")
        .getResponse().data;

      // Save for Python processing
      io.writeFileJSON("./temp/data.json", data);

  # Transform with Python
  - name: Transform Data
    deps:
      - Extract Data
    lang: python
    exec: |
      import pandas as pd
      import json

      # Load data
      with open('./temp/data.json') as f:
          data = json.load(f)

      # Convert to DataFrame
      df = pd.DataFrame(data)

      # Transform
      df['processed'] = df['value'] * 2
      df['category'] = df['value'].apply(lambda x: 'high' if x > 100 else 'low')

      # Aggregate
      summary = df.groupby('category').agg({
          'value': ['sum', 'mean', 'count']
      }).to_dict()

      # Save results
      result_data = df.to_dict('records')

      with open('./temp/transformed.json', 'w') as f:
          json.dump(result_data, f)

      print(json.dumps({
          'rows': len(df),
          'summary': summary
      }))

  # Load to database
  - name: Load Data
    deps:
      - Transform Data
    exec: |
      var data = io.readFileJSON("./temp/transformed.json");

      log("Loading " + data.length + " rows");

      // Load to database
      data.forEach(row => {
        // Insert into database
        insertRow(row);
      });

      log("Data loaded successfully");

  # Cleanup
  - name: Cleanup
    deps:
      - Load Data
    exec: |
      io.rm("./temp/data.json");
      io.rm("./temp/transformed.json");

todo:
  - Extract Data
  - Transform Data
  - Load Data
  - Cleanup
```

---

## Troubleshooting

### Python Not Found

**Error:** `python: command not found`

**Solutions:**
1. Install Python 3
2. Add Python to PATH
3. Use full Python path:

```javascript
var result = af.runFromExternalClass("/usr/bin/python3", code);
```

### Module Import Errors

**Error:** `ModuleNotFoundError: No module named 'pandas'`

**Solutions:**
```bash
# Install module
pip install pandas

# Or use specific Python
pip3 install pandas
```

### JSON Parsing Errors

**Problem:** Invalid JSON from Python

**Solution:** Always use `json.dumps()` in Python:

```python
import json

result = {"key": "value"}
print(json.dumps(result))  # Correct

# NOT: print(result)  # Wrong - won't parse as JSON
```

### Character Encoding Issues

```python
# Use UTF-8 encoding
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

---

## Best Practices

### 1. Always Use JSON for Data Exchange

```python
import json
result = {"data": [1, 2, 3]}
print(json.dumps(result))
```

### 2. Handle Errors in Python

```python
import json
import sys

try:
    # Your code
    result = process_data()
    print(json.dumps({'success': True, 'data': result}))
except Exception as e:
    print(json.dumps({'success': False, 'error': str(e)}))
    sys.exit(1)
```

### 3. Use Type Hints in Python

```python
from typing import List, Dict

def process_items(items: List[int]) -> Dict[str, int]:
    return {'sum': sum(items)}
```

### 4. Validate Inputs

```python
import json
import sys

data = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}

if 'required_field' not in data:
    print(json.dumps({'error': 'Missing required field'}))
    sys.exit(1)
```

### 5. Clean Up Resources

```python
import json

try:
    with open('file.txt', 'r') as f:
        data = f.read()

    result = process(data)
    print(json.dumps(result))
finally:
    # Cleanup if needed
    pass
```

---

## See Also

- [oJob Reference](../../concepts/oJob.html)
- [ow.python Reference](../../reference/ow_python.md)
- [Language Integration](../ojob/language-access.md)
- [Python Official Documentation](https://docs.python.org/)
