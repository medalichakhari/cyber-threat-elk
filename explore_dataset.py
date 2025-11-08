import pandas as pd
import os

# Find CSV files in data directory
data_dir = "./data"
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

if not csv_files:
    print("No CSV files found in ./data/")
    print("Please download and extract the dataset to the data/ folder")
    exit(1)

for i, file in enumerate(csv_files, 1):
    file_path = os.path.join(data_dir, file)
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    print(f"  {i}. {file} ({size_mb:.2f} MB)")

csv_file = csv_files[0]
file_path = os.path.join(data_dir, csv_file)

print(f"\nAnalyzing: {csv_file}")
print("=" * 70)

df = pd.read_csv(file_path, nrows=1000)  # Load first 1000 rows for quick analysis

print(f"\nDataset loaded successfully!")
print(f"   Total rows (sample): {len(df)}")
print(f"   Total columns: {len(df.columns)}")

print("-" * 70)
for col in df.columns:
    dtype = str(df[col].dtype)
    non_null = df[col].count()
    sample = df[col].iloc[0] if len(df) > 0 else "N/A"
    print(f"  • {col:25} | Type: {dtype:10} | Sample: {sample}")

print("=" * 70)
print(df.head())

print("=" * 70)
print(df.describe())

print("-" * 70)
for col in df.columns:
    unique_count = df[col].nunique()
    if unique_count < 50:  # Show unique values for categorical columns
        print(f"\n  {col}: {unique_count} unique values")
        print(f"    {df[col].value_counts().head(10).to_dict()}")