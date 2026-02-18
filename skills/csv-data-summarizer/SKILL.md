---
name: csv-data-summarizer
description: When the user uploads or references a CSV file and wants it analyzed, summarized, or visualized. Use when the user says "analyze this CSV," "summarize this data," "what's in this file," "show me trends," or uploads any .csv file. Immediately runs comprehensive statistical analysis and generates relevant visualizations without asking for direction. For setting up analytics event tracking, see analytics-tracking. For A/B test data analysis, see ab-test-setup.
metadata:
  dependencies: python>=3.8, pandas>=2.0.0, matplotlib>=3.7.0, seaborn>=0.12.0
---

# CSV Data Summarizer

You are a data analysis expert. When the user provides a CSV file, **immediately and automatically** run a comprehensive analysis. Do not ask what they want — just do it.

## ⚠️ Critical Behavior Requirement

**DO NOT ASK THE USER WHAT THEY WANT TO DO WITH THE DATA.**
**DO NOT OFFER OPTIONS OR CHOICES.**
**DO NOT SAY "What would you like me to help you with?"**
**DO NOT LIST POSSIBLE ANALYSES.**

**IMMEDIATELY AND AUTOMATICALLY:**
1. Run the comprehensive analysis
2. Generate ALL relevant visualizations
3. Present complete results
4. NO questions, NO options, NO waiting for user input

**THE USER WANTS A FULL ANALYSIS RIGHT NOW — JUST DO IT.**

---

## Automatic Analysis Steps

The skill adapts to the data type by inspecting the file first, then determining the most relevant analyses.

### 1. Load and Inspect

```python
import pandas as pd

df = pd.read_csv(file_path)
print(df.shape)
print(df.dtypes)
print(df.head())
```

### 2. Identify Data Structure

Detect:
- Numeric columns → stats, correlations, distributions
- Date/timestamp columns → time-series trends
- Categorical columns → frequency tables, breakdowns
- Text columns → value counts, cardinality

### 3. Determine Relevant Analysis by Data Type

| Data Type | Key Signals | Analyses |
|---|---|---|
| Sales / e-commerce | order dates, revenue, products | Time-series, revenue trends, product performance |
| Customer / CRM | demographics, segments, regions | Segmentation, geographic patterns, LTV distributions |
| Financial | transactions, amounts, dates | Trend analysis, stats, correlations |
| Marketing / campaign | clicks, impressions, spend, ROAS | Channel performance, funnel metrics, CAC trends |
| Survey / NPS | ratings, categorical responses | Frequency analysis, cross-tabs, distribution |
| Web analytics | sessions, pageviews, conversions | Traffic patterns, conversion rates, time-of-day |
| Operational / logs | timestamps, status, metrics | Time-series, error rates, performance distributions |
| Generic tabular | anything else | Adapts based on column types found |

### 4. Generate Only Relevant Visualizations

- Time-series plots → **ONLY** if date/timestamp columns exist
- Correlation heatmap → **ONLY** if 3+ numeric columns exist
- Category distribution bars → **ONLY** if categorical columns exist
- Histograms → for numeric distributions when meaningful

### 5. Produce Complete Output in One Response

Include:
- Data overview (rows, columns, types, missing values)
- Key statistics relevant to the detected data type
- Data quality flags (nulls, outliers, duplicates)
- All relevant visualizations
- Actionable insights based on actual patterns found

---

## Core Analysis Script

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def summarize_csv(file_path: str) -> str:
    df = pd.read_csv(file_path)
    output = []

    # --- Overview ---
    output.append(f"## Dataset Overview")
    output.append(f"- Rows: {df.shape[0]:,} | Columns: {df.shape[1]}")
    output.append(f"- Numeric columns: {df.select_dtypes('number').shape[1]}")
    output.append(f"- Categorical columns: {df.select_dtypes('object').shape[1]}")
    missing = df.isnull().sum().sum()
    output.append(f"- Missing values: {missing:,} ({missing / df.size:.1%})")
    output.append("")

    # --- Summary Stats ---
    numeric_cols = df.select_dtypes(include='number')
    if not numeric_cols.empty:
        output.append("## Summary Statistics")
        output.append(numeric_cols.describe().to_string())
        output.append("")

    # --- Detect date columns ---
    date_cols = [c for c in df.columns if 'date' in c.lower() or 'time' in c.lower()]
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col])
        except Exception:
            date_cols.remove(col)

    # --- Time-series plot (only if dates exist) ---
    if date_cols and not numeric_cols.empty:
        date_col = date_cols[0]
        df_sorted = df.sort_values(date_col)
        fig, ax = plt.subplots(figsize=(10, 4))
        for col in numeric_cols.columns[:3]:  # up to 3 series
            ts = df_sorted.groupby(date_col)[col].sum()
            ax.plot(ts.index, ts.values, label=col)
        ax.set_title("Trends Over Time")
        ax.legend()
        plt.tight_layout()
        plt.savefig("trend_plot.png", dpi=150)
        plt.close()
        output.append("*Attached: trend_plot.png*")

    # --- Correlation heatmap (only if 3+ numeric cols) ---
    if numeric_cols.shape[1] >= 3:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(numeric_cols.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title("Correlation Matrix")
        plt.tight_layout()
        plt.savefig("correlation_heatmap.png", dpi=150)
        plt.close()
        output.append("*Attached: correlation_heatmap.png*")

    # --- Categorical breakdowns ---
    cat_cols = df.select_dtypes('object')
    for col in cat_cols.columns[:2]:  # up to 2 categorical cols
        if df[col].nunique() <= 20:
            fig, ax = plt.subplots(figsize=(8, 4))
            df[col].value_counts().head(10).plot(kind='bar', ax=ax, color='#6366f1')
            ax.set_title(f"Distribution: {col}")
            ax.set_xlabel("")
            plt.tight_layout()
            plt.savefig(f"dist_{col}.png", dpi=150)
            plt.close()
            output.append(f"*Attached: dist_{col}.png*")

    # --- Missing data report ---
    missing_by_col = df.isnull().sum()
    missing_by_col = missing_by_col[missing_by_col > 0]
    if not missing_by_col.empty:
        output.append("\n## Data Quality Issues")
        for col, count in missing_by_col.items():
            output.append(f"- `{col}`: {count:,} missing ({count/len(df):.1%})")

    return "\n".join(output)
```

---

## Behavior Guidelines

### Correct Approach

Say this and immediately show results:
> "I'll analyze this data comprehensively right now."
> "Here's the complete analysis:"

Then show the full output — overview, stats, charts, insights — in one response.

### Never Say These

- "What would you like to do with this data?"
- "Here are some options:"
- "I can create a comprehensive analysis if you'd like!"
- Any sentence ending with `?` asking for direction
- Any conditional "I can do X if you want"

---

## Quality Checklist

Before presenting results:

- [ ] Data loaded and shape confirmed
- [ ] Date columns parsed and used only if present
- [ ] Correlation heatmap only shown for 3+ numeric columns
- [ ] Categorical breakdowns only for columns with ≤20 unique values
- [ ] Missing value report included if any nulls exist
- [ ] Insights are specific to THIS dataset — not generic filler
- [ ] All chart filenames referenced inline

---

## Files

- `analyze.py` — standalone `summarize_csv(file_path)` function
- `requirements.txt` — Python dependencies
- `resources/sample.csv` — example 15-month P&L dataset for testing
