import pandas as pd
import re

# Load the dataset
file_path = 'bank-marketing.csv' # Update this path
df = pd.read_csv(file_path)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values. Here we're dropping rows with any missing values
# You might choose to fill these instead, depending on your dataset and needs
df = df.dropna()

# Normalize text data: convert to lowercase and remove special characters
# Adjust the column names according to your dataset
text_columns = ['job'] # Update with your actual text columns
for column in text_columns:
    # Convert to lowercase
    df[column] = df[column].str.lower()
    # Remove special characters
    df[column] = df[column].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

# Assume df has numeric columns 'price' and 'age'. Update these to your actual numeric columns
numeric_columns = ['age']  # Update with your actual numeric columns

# Handle missing values. Here we're filling missing values with the mean of the column
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Save the cleaned dataset to a new CSV file
cleaned_file_path = 'cleaned_bank-marketing.csv' # Update this path
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned dataset saved to {cleaned_file_path}")
