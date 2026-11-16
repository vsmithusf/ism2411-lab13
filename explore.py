### Self-Assessment Questions ###
#1# A boolean filter uses operational logic (and, or, not) to filter each row based on whether or not they meet true-or-false conditions.
#2# Single brackets return a one-dimensional list, while double brackets return a two-dimensional data frame. This distinction matters
### when you are working with multiple variables, where double brackets would be preferred.
#3# Pandas allows you to filter and sort large sets of data quicker and more efficiently than Excel allows you to, while also giving you
### more options for filtering.


print("--- Exercise 1: Load It ---")
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print(" ")
print("--- Exercise 2: Filter by Region ---")
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print(" ")
print("--- Exercise 3: Top 5 by Revenue ---")
top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print(" ")
print("--- Exercise 4: Two-Condition Filter ---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south[0:5])

print(" ")
print("--- Exercise 5: A New Column ---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())

print(" ")
print("--- Exercise 6: Unique Values ---")
print(df['region'].unique())
print(df['region'].value_counts())

print(" ")
print("--- Exercise 7: Select Columns ---")
df_subset = df[['region', 'product', 'revenue']]
print(df_subset.shape)

print(" ")
print("--- Exercise 8: Save ---")
df.to_csv('data/explored.csv', index=False) # always use index=False