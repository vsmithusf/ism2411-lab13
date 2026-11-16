print("--- Exercise 1: Load It ---")
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--- Exercise 2: Filter by Region ---")
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("--- Exercise 3: Top 5 by Revenue ---")
top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print("--- Exercise 4: Two-Condition Filter ---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print("--- Exercise 5: A New Column ---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())

print("--- Exercise 6: Unique Values ---")

print("--- Exercise 7: Select Columns ---")

print("--- Exercise 8: Save ---")
