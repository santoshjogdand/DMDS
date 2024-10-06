import pandas as pd

dataset = pd.read_csv("./StudPer.csv",header=None)

# 1. Display the shape of the dataset
print("Shape of the dataset:", dataset.shape)

# 2. Display the top rows of the dataset (first 5 rows by default)
print("\nTop rows of the dataset:")
print(dataset.head())

# 3. Display a number of rows randomly (let's say 10 rows randomly)
random_rows = dataset.sample(n=10)
print("\nRandom rows from the dataset:")
print(random_rows)

# 4. Display the number of columns and the names of the columns
print("\nNumber of columns:", len(dataset.columns))
print("Names of the columns:", list(dataset.columns))
