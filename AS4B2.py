import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

dataset = pd.read_csv("./groceries.csv")

records = []
for i in range(0, 1000):
    records.append([str(dataset.values[i, j]) for j in range(0, 10)]) 

rules = apriori(records, min_support=0.0040, min_confidence=0.2, min_lift=3,min_length=2)

results = list(rules)


for item in results:
    pair = item.items
    items = [x for x in pair]
    print(f"Rule: {items[0]} -> {items[1]}")
    
    print(f"Support: {items}")

    for ordered_stat in item.ordered_statistics:
         print(f"Confidence: {ordered_stat.confidence}")
         print(f"Lift: {ordered_stat.lift}")
    print("========================================\n")
