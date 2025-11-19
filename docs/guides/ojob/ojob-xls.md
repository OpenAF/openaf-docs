---
layout: default
title: oJob XLS
parent: oJob
grand_parent: Guides
---

# oJob XLS - Excel File Operations

The oJob XLS utilities provide easy Excel (XLSX) file creation and manipulation within oJob workflows, enabling automated report generation and data export to spreadsheets.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

oJob XLS enables:
- **Create Excel files** from data
- **Add tables** with automatic formatting
- **Use templates** for consistent styling
- **Auto-sizing and filters** for better UX
- **Custom cell styling** (colors, fonts, borders)

### Use Cases

- Generate Excel reports from database queries
- Export API data to spreadsheets
- Create formatted data tables
- Automated report generation
- Data extraction and transformation

---

## Getting Started

### Basic Excel Creation

```yaml
include:
  - oJobXLS.yaml

jobs:
  - name: Create Excel Report
    exec: |
      var data = [
        { name: "Alice", age: 30, department: "Sales" },
        { name: "Bob", age: 25, department: "IT" },
        { name: "Charlie", age: 35, department: "HR" }
      ];

      $job("oJob XLS Open File", { file: "report.xlsx" });
      $job("oJob XLS Table", { file: "report.xlsx", sheet: "Employees", data: data });
      $job("oJob XLS Close File", { file: "report.xlsx" });

      log("Report created: report.xlsx");

todo:
  - Create Excel Report
```

---

## Jobs Reference

### oJob XLS Open File

Opens or creates an Excel file for manipulation.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `file` | String | Yes | Path to the Excel file to create/write |
| `template` | String | No | Path to template Excel file to use as base |

**Example:**

```yaml
jobs:
  - name: Open New File
    to: oJob XLS Open File
    args:
      file: ./output/report.xlsx

  - name: Open from Template
    to: oJob XLS Open File
    args:
      file: ./output/branded-report.xlsx
      template: ./templates/company-template.xlsx
```

---

### oJob XLS Table

Adds a table of data to a sheet with automatic formatting.

**Arguments:**

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `file` | String | Yes | - | Excel file path |
| `sheet` | String | No | `"table"` | Sheet name or number |
| `data` | Array | Yes | `[]` | Array of objects to add as table |
| `position` | Map | No | `{row:1, column:'A'}` | Starting position for table |
| `headerStyle` | Map | No | (see below) | Header row style options |
| `lineStyle` | Map | No | (see below) | Data row style options |
| `autoResize` | Boolean | No | `true` | Auto-size columns to fit content |
| `autoFilter` | Boolean | No | `true` | Add auto-filter to header row |

**Default Header Style:**
```javascript
{
  bold: true,
  fontPoints: 10,
  wrapText: true,
  borderBottom: "thick",
  borderBottomColor: "red"
}
```

**Default Line Style:**
```javascript
{
  valign: "top",
  fontPoints: 10,
  wrapText: true
}
```

**Position Map:**
```javascript
{
  row: 1,        // Row number (1-based)
  column: 'A'    // Column letter
}
```

**Example:**

```yaml
jobs:
  - name: Add Table
    to: oJob XLS Table
    args:
      file: report.xlsx
      sheet: "Sales Data"
      data: "{{salesData}}"
      position:
        row: 2
        column: 'B'
      headerStyle:
        bold: true
        bgColor: "blue"
        fgColor: "white"
      lineStyle:
        fontPoints: 9
```

---

### oJob XLS Close File

Closes the Excel file and writes it to disk.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `file` | String | Yes | Excel file path to close |

**Example:**

```yaml
jobs:
  - name: Save and Close
    to: oJob XLS Close File
    args:
      file: report.xlsx
```

---

## Common Patterns

### Pattern 1: Database Query to Excel

```yaml
include:
  - oJobXLS.yaml
  - oJobSQL.yaml

jobs:
  - name: Query Database
    to: SQL
    args:
      DBURL: "jdbc:postgresql://localhost:5432/mydb"
      DBUser: "{{dbUser}}"
      DBPass: "{{dbPass}}"
      sql: |
        SELECT
          employee_id,
          first_name,
          last_name,
          department,
          salary,
          hire_date
        FROM employees
        WHERE active = true
        ORDER BY department, last_name

  - name: Export to Excel
    deps:
      - Query Database
    exec: |
      $job("oJob XLS Open File", { file: "employees.xlsx" });

      $job("oJob XLS Table", {
        file: "employees.xlsx",
        sheet: "Active Employees",
        data: args.output,
        headerStyle: {
          bold: true,
          bgColor: "darkblue",
          fgColor: "white",
          fontPoints: 11
        }
      });

      $job("oJob XLS Close File", { file: "employees.xlsx" });

      log("Employee report generated");

todo:
  - Query Database
  - Export to Excel
```

### Pattern 2: Multiple Sheets

```yaml
include:
  - oJobXLS.yaml

jobs:
  - name: Multi-Sheet Report
    exec: |
      // Open file
      $job("oJob XLS Open File", { file: "quarterly-report.xlsx" });

      // Sales sheet
      $job("oJob XLS Table", {
        file: "quarterly-report.xlsx",
        sheet: "Sales",
        data: args.salesData
      });

      // Expenses sheet
      $job("oJob XLS Table", {
        file: "quarterly-report.xlsx",
        sheet: "Expenses",
        data: args.expensesData
      });

      // Summary sheet
      $job("oJob XLS Table", {
        file: "quarterly-report.xlsx",
        sheet: "Summary",
        data: args.summaryData,
        headerStyle: {
          bold: true,
          bgColor: "green",
          fgColor: "white"
        }
      });

      // Close file
      $job("oJob XLS Close File", { file: "quarterly-report.xlsx" });
```

### Pattern 3: Custom Styling

```yaml
include:
  - oJobXLS.yaml

jobs:
  - name: Styled Report
    exec: |
      var data = [
        { product: "Widget A", revenue: 15000, target: 10000, variance: 5000 },
        { product: "Widget B", revenue: 8000, target: 12000, variance: -4000 },
        { product: "Widget C", revenue: 22000, target: 20000, variance: 2000 }
      ];

      $job("oJob XLS Open File", { file: "performance.xlsx" });

      $job("oJob XLS Table", {
        file: "performance.xlsx",
        sheet: "Performance",
        data: data,
        position: { row: 3, column: 'B' },
        headerStyle: {
          bold: true,
          bgColor: "navy",
          fgColor: "white",
          fontPoints: 12,
          align: "center",
          borderBottom: "thick"
        },
        lineStyle: {
          fontPoints: 10,
          align: "left",
          valign: "middle",
          wrapText: false
        },
        autoResize: true,
        autoFilter: true
      });

      $job("oJob XLS Close File", { file: "performance.xlsx" });
```

### Pattern 4: Template-Based Reports

```yaml
include:
  - oJobXLS.yaml

jobs:
  - name: Branded Report
    exec: |
      // Use company template with logo and formatting
      $job("oJob XLS Open File", {
        file: "monthly-report.xlsx",
        template: "./templates/company-report-template.xlsx"
      });

      // Add data starting after template header (row 10)
      $job("oJob XLS Table", {
        file: "monthly-report.xlsx",
        sheet: "Data",
        data: args.monthlyData,
        position: { row: 10, column: 'A' },
        headerStyle: {
          bold: true,
          bgColor: "companyBlue",  // From template colors
          fgColor: "white"
        }
      });

      $job("oJob XLS Close File", { file: "monthly-report.xlsx" });
```

### Pattern 5: API Data Export

```yaml
include:
  - oJobXLS.yaml

jobs:
  - name: Fetch API Data
    exec: |
      ow.loadObj();

      var response = $rest()
        .get("https://api.example.com/reports/sales")
        .getResponse();

      args.apiData = response.data;

  - name: Export API Data
    deps:
      - Fetch API Data
    exec: |
      // Transform API data if needed
      var transformed = args.apiData.map(item => ({
        Date: ow.format.fromDate(new Date(item.timestamp), "yyyy-MM-dd"),
        Product: item.productName,
        Quantity: item.qty,
        Revenue: item.totalRevenue,
        Region: item.region
      }));

      $job("oJob XLS Open File", { file: "api-export.xlsx" });

      $job("oJob XLS Table", {
        file: "api-export.xlsx",
        sheet: "Sales Data",
        data: transformed
      });

      $job("oJob XLS Close File", { file: "api-export.xlsx" });

todo:
  - Fetch API Data
  - Export API Data
```

### Pattern 6: Scheduled Report Generation

```yaml
include:
  - oJobXLS.yaml
  - oJobEmail.yaml

ojob:
  daemon: true

jobs:
  # Generate daily report
  - name: Daily Report
    typeArgs:
      cron: "0 9 * * *"  # 9 AM daily
    exec: |
      log("Generating daily report");

      // Collect data
      var data = collectDailyMetrics();

      // Generate filename with date
      var today = ow.format.fromDate(new Date(), "yyyy-MM-dd");
      var filename = "./reports/daily-" + today + ".xlsx";

      // Create Excel
      $job("oJob XLS Open File", { file: filename });
      $job("oJob XLS Table", {
        file: filename,
        sheet: "Metrics",
        data: data
      });
      $job("oJob XLS Close File", { file: filename });

      // Email report
      $job("Email Report", { filename: filename });

  # Email job
  - name: Email Report
    to: oJob Send email
    args:
      server: "{{emailServer}}"
      from: "reports@example.com"
      to: ["team@example.com"]
      subject: "Daily Report - {{ow.format.fromDate(new Date(), 'yyyy-MM-dd')}}"
      output: "Please find attached the daily report."
      addAttachments:
        - file: "{{filename}}"
          name: "daily-report.xlsx"

todo:
  - Daily Report
```

---

## Style Options Reference

### Available Style Properties

| Property | Type | Values | Description |
|----------|------|--------|-------------|
| `bold` | Boolean | true/false | Bold text |
| `italic` | Boolean | true/false | Italic text |
| `underline` | Boolean | true/false | Underlined text |
| `fontPoints` | Number | 8-72 | Font size in points |
| `fontName` | String | "Arial", "Calibri", etc. | Font family |
| `bgColor` | String | Color name/hex | Background color |
| `fgColor` | String | Color name/hex | Foreground (text) color |
| `align` | String | "left","center","right" | Horizontal alignment |
| `valign` | String | "top","middle","bottom" | Vertical alignment |
| `wrapText` | Boolean | true/false | Text wrapping |
| `borderTop` | String | "thin","medium","thick" | Top border style |
| `borderBottom` | String | "thin","medium","thick" | Bottom border style |
| `borderLeft` | String | "thin","medium","thick" | Left border style |
| `borderRight` | String | "thin","medium","thick" | Right border style |
| `borderTopColor` | String | Color name/hex | Top border color |
| `borderBottomColor` | String | Color name/hex | Bottom border color |
| `borderLeftColor` | String | Color name/hex | Left border color |
| `borderRightColor` | String | Color name/hex | Right border color |

### Color Examples

```yaml
headerStyle:
  bgColor: "navy"
  fgColor: "white"

lineStyle:
  bgColor: "#F0F0F0"
  fgColor: "#333333"
```

---

## Advanced Techniques

### Conditional Formatting

```yaml
jobs:
  - name: Color-Coded Report
    exec: |
      var data = [
        { product: "A", sales: 15000, target: 10000 },
        { product: "B", sales: 8000, target: 12000 },
        { product: "C", sales: 22000, target: 20000 }
      ];

      // Add status field
      data = data.map(row => {
        row.status = row.sales >= row.target ? "✓" : "✗";
        return row;
      });

      $job("oJob XLS Open File", { file: "sales.xlsx" });
      $job("oJob XLS Table", {
        file: "sales.xlsx",
        sheet: "Sales",
        data: data
      });
      $job("oJob XLS Close File", { file: "sales.xlsx" });
```

### Aggregated Data

```yaml
jobs:
  - name: Summary Report
    exec: |
      var data = args.salesData;

      // Add summary row
      var summary = {
        product: "TOTAL",
        sales: $from(data).sum("sales"),
        target: $from(data).sum("target")
      };

      data.push(summary);

      $job("oJob XLS Open File", { file: "summary.xlsx" });
      $job("oJob XLS Table", {
        file: "summary.xlsx",
        sheet: "Summary",
        data: data,
        lineStyle: {
          fontPoints: 10
        }
      });

      // Note: To style the last row differently,
      // you'd need to use the XLS plugin directly
      $job("oJob XLS Close File", { file: "summary.xlsx" });
```

### Using XLS Plugin Directly

For more advanced features, use the XLS plugin:

```yaml
jobs:
  - name: Advanced Excel
    exec: |
      plugin("XLS");
      ow.loadFormat();

      var xls = new XLS();
      var sheet = xls.getSheet("Advanced");

      // Set cell values directly
      xls.setCellValue(sheet, "A1", "Title");
      xls.setCellValue(sheet, "B1", "Value");

      // Apply custom style
      var headerStyle = ow.format.xls.getStyle(xls, {
        bold: true,
        bgColor: "blue",
        fgColor: "white"
      });
      xls.setCellStyle(sheet, "A1", headerStyle);
      xls.setCellStyle(sheet, "B1", headerStyle);

      // Add formula
      xls.setCellValue(sheet, "B5", "=SUM(B2:B4)");

      // Write file
      xls.writeFile("advanced.xlsx");
      xls.close();
```

---

## Error Handling

### Safe File Operations

```yaml
jobs:
  - name: Safe Excel Generation
    exec: |
      var filename = "report.xlsx";

      try {
        $job("oJob XLS Open File", { file: filename });

        $job("oJob XLS Table", {
          file: filename,
          sheet: "Data",
          data: args.data
        });

        $job("oJob XLS Close File", { file: filename });

        log("Report generated successfully: " + filename);

      } catch(e) {
        logErr("Failed to generate Excel: " + e.message);

        // Cleanup
        if (isDef(global.__xls) && isDef(global.__xls[filename])) {
          try {
            global.__xls[filename].close();
            delete global.__xls[filename];
          } catch(cleanup) {}
        }

        throw e;
      }
```

### Validate Data

```yaml
jobs:
  - name: Validated Export
    exec: |
      // Validate data
      _$(args.data, "data").isArray().$_();

      if (args.data.length == 0) {
        logWarn("No data to export");
        return;
      }

      // Ensure all rows have same keys
      var keys = Object.keys(args.data[0]);
      var valid = args.data.every(row =>
        Object.keys(row).length == keys.length
      );

      if (!valid) {
        throw "Data rows have inconsistent structure";
      }

      // Generate Excel
      $job("oJob XLS Open File", { file: "validated.xlsx" });
      $job("oJob XLS Table", {
        file: "validated.xlsx",
        sheet: "Data",
        data: args.data
      });
      $job("oJob XLS Close File", { file: "validated.xlsx" });
```

---

## Complete Example: Monthly Sales Report

```yaml
include:
  - oJobXLS.yaml
  - oJobSQL.yaml
  - oJobEmail.yaml

ojob:
  sequential: true

jobs:
  # Query sales data
  - name: Get Sales Data
    to: SQL
    args:
      DBURL: "{{dbUrl}}"
      DBUser: "{{dbUser}}"
      DBPass: "{{dbPass}}"
      sql: |
        SELECT
          DATE(order_date) as date,
          product_name,
          category,
          SUM(quantity) as units_sold,
          SUM(amount) as revenue,
          AVG(amount) as avg_order_value
        FROM orders
        WHERE order_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
          AND order_date < DATE_TRUNC('month', CURRENT_DATE)
        GROUP BY DATE(order_date), product_name, category
        ORDER BY date, revenue DESC

  # Query summary
  - name: Get Summary
    to: SQL
    args:
      DBURL: "{{dbUrl}}"
      DBUser: "{{dbUser}}"
      DBPass: "{{dbPass}}"
      sql: |
        SELECT
          category,
          COUNT(*) as orders,
          SUM(quantity) as total_units,
          SUM(amount) as total_revenue
        FROM orders
        WHERE order_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
          AND order_date < DATE_TRUNC('month', CURRENT_DATE)
        GROUP BY category
        ORDER BY total_revenue DESC

  # Generate Excel report
  - name: Generate Report
    deps:
      - Get Sales Data
      - Get Summary
    exec: |
      var filename = "monthly-sales-" +
        ow.format.fromDate(new Date(), "yyyy-MM") + ".xlsx";

      // Open file
      $job("oJob XLS Open File", {
        file: filename,
        template: "./templates/sales-template.xlsx"
      });

      // Sales detail sheet
      $job("oJob XLS Table", {
        file: filename,
        sheet: "Sales Detail",
        data: args.output,
        position: { row: 1, column: 'A' },
        headerStyle: {
          bold: true,
          bgColor: "darkgreen",
          fgColor: "white",
          fontPoints: 11
        },
        lineStyle: {
          fontPoints: 10,
          wrapText: false
        }
      });

      // Summary sheet
      $job("Get Summary");
      $job("oJob XLS Table", {
        file: filename,
        sheet: "Summary",
        data: args.output,
        position: { row: 1, column: 'A' },
        headerStyle: {
          bold: true,
          bgColor: "navy",
          fgColor: "white",
          fontPoints: 12
        },
        lineStyle: {
          fontPoints: 11,
          bold: false
        }
      });

      // Close file
      $job("oJob XLS Close File", { file: filename });

      args.reportFile = filename;
      log("Report generated: " + filename);

  # Email report
  - name: Email Report
    deps:
      - Generate Report
    to: oJob Send email
    args:
      server: "{{emailServer}}"
      from: "reports@example.com"
      to: ["sales-team@example.com", "management@example.com"]
      subject: "Monthly Sales Report - {{ow.format.fromDate(new Date(), 'MMMM yyyy')}}"
      output: |
        Please find attached the monthly sales report.

        Report period: {{ow.format.fromDate(new Date(), 'MMMM yyyy')}}
        Generated: {{ow.format.fromDate(new Date(), 'yyyy-MM-dd HH:mm:ss')}}
      addAttachments:
        - file: "{{reportFile}}"
          name: "{{reportFile}}"

todo:
  - Get Sales Data
  - Get Summary
  - Generate Report
  - Email Report
```

---

## Best Practices

### 1. Always Close Files

```yaml
try:
  $job("oJob XLS Open File", { file: filename });
  $job("oJob XLS Table", { file: filename, data: data });
finally:
  $job("oJob XLS Close File", { file: filename });
```

### 2. Validate Data Structure

```yaml
if (!isArray(data) || data.length == 0) {
  logWarn("No data to export");
  return;
}
```

### 3. Use Meaningful Sheet Names

```yaml
# Good
sheet: "Monthly Sales"
sheet: "Customer Data"

# Bad
sheet: "Sheet1"
sheet: "Data"
```

### 4. Enable Auto Features

```yaml
autoResize: true   # Better readability
autoFilter: true   # User-friendly
```

### 5. Consistent Styling

Create style constants:

```yaml
jobs:
  - name: Constants
    exec: |
      global.HEADER_STYLE = {
        bold: true,
        bgColor: "navy",
        fgColor: "white"
      };

      global.LINE_STYLE = {
        fontPoints: 10
      };
```

---

## See Also

- [oJob Basics](common-browse.md)
- [oJob SQL](common-browse.md#oJobSQL)
- [XLS Plugin Reference](../../reference/plugins/xls.md)
- [ow.format.xls Reference](../../reference/ow_format.md)
