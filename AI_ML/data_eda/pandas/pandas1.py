import pandas as pd

# 1. Create our dataset: Ages of 11 people in a coding class
ages = [22, 25, 19, 30, 65, 21, 28, 22, 40, 24, 35]

# 2. Convert it into a pandas DataFrame
df = pd.DataFrame({'Age': ages})

# 3. Print the sorted data so we can see the order with our own eyes
print("--- Sorted Data ---")
sorted_ages = df['Age'].sort_values(ignore_index=True).tolist()
print(sorted_ages)

# 4. Run describe() to get the Five-Number Summary
print("\n--- df.describe() Output ---")
print(df.describe())