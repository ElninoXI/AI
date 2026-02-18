"""
CSV Data Summarizer - Core analysis function.
Usage: summarize_csv("path/to/data.csv")
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def summarize_csv(file_path: str) -> str:
    """
    Analyze a CSV file and return a comprehensive text summary.
    Also saves visualizations to the current directory.
    """
    df = pd.read_csv(file_path)
    output = []

    # --- Overview ---
    output.append("## Dataset Overview")
    output.append(f"- Rows: {df.shape[0]:,} | Columns: {df.shape[1]}")
    numeric_cols = df.select_dtypes(include="number")
    cat_cols = df.select_dtypes(include="object")
    output.append(f"- Numeric columns ({numeric_cols.shape[1]}): {', '.join(numeric_cols.columns.tolist())}")
    output.append(f"- Categorical columns ({cat_cols.shape[1]}): {', '.join(cat_cols.columns.tolist())}")
    missing_total = df.isnull().sum().sum()
    output.append(f"- Missing values: {missing_total:,} ({missing_total / df.size:.1%} of all cells)")
    output.append("")

    # --- Summary Stats ---
    if not numeric_cols.empty:
        output.append("## Summary Statistics")
        output.append(numeric_cols.describe().round(2).to_string())
        output.append("")

    # --- Detect and parse date columns ---
    date_cols = []
    for col in df.columns:
        if any(kw in col.lower() for kw in ("date", "time", "timestamp", "month", "year", "week")):
            try:
                df[col] = pd.to_datetime(df[col])
                date_cols.append(col)
            except Exception:
                pass

    # --- Time-series plot ---
    if date_cols and not numeric_cols.empty:
        date_col = date_cols[0]
        df_sorted = df.sort_values(date_col)
        fig, ax = plt.subplots(figsize=(10, 4))
        for col in numeric_cols.columns[:3]:
            ts = df_sorted.groupby(date_col)[col].sum()
            ax.plot(ts.index, ts.values, marker="o", markersize=3, label=col)
        ax.set_title("Trends Over Time", fontsize=13, fontweight="bold")
        ax.set_xlabel(date_col)
        ax.legend()
        plt.tight_layout()
        plt.savefig("trend_plot.png", dpi=150)
        plt.close()
        output.append("*Visualization saved: trend_plot.png*")

    # --- Correlation heatmap ---
    if numeric_cols.shape[1] >= 3:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            numeric_cols.corr(),
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
            ax=ax,
            linewidths=0.5,
        )
        ax.set_title("Correlation Matrix", fontsize=13, fontweight="bold")
        plt.tight_layout()
        plt.savefig("correlation_heatmap.png", dpi=150)
        plt.close()
        output.append("*Visualization saved: correlation_heatmap.png*")

    # --- Categorical distributions ---
    for col in cat_cols.columns[:2]:
        if 2 <= df[col].nunique() <= 20:
            fig, ax = plt.subplots(figsize=(8, 4))
            df[col].value_counts().head(10).plot(kind="bar", ax=ax, color="#6366f1", edgecolor="white")
            ax.set_title(f"Distribution: {col}", fontsize=13, fontweight="bold")
            ax.set_xlabel("")
            ax.tick_params(axis="x", rotation=30)
            plt.tight_layout()
            fname = f"dist_{col.lower().replace(' ', '_')}.png"
            plt.savefig(fname, dpi=150)
            plt.close()
            output.append(f"*Visualization saved: {fname}*")

    output.append("")

    # --- Missing data report ---
    missing_by_col = df.isnull().sum()
    missing_by_col = missing_by_col[missing_by_col > 0]
    if not missing_by_col.empty:
        output.append("## Data Quality Issues")
        for col, count in missing_by_col.sort_values(ascending=False).items():
            output.append(f"- `{col}`: {count:,} missing ({count / len(df):.1%})")
        output.append("")

    # --- Duplicate check ---
    dupes = df.duplicated().sum()
    if dupes > 0:
        output.append(f"⚠️  {dupes:,} duplicate rows detected.")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python analyze.py <path_to_csv>")
        sys.exit(1)
    print(summarize_csv(sys.argv[1]))
