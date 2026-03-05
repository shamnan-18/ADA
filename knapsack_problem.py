from itertools import combinations

weights = [7, 3, 4, 5]
values = [42, 12, 40, 25]
capacity = 10
n = len(weights)

best_value = 0
best_subset = None

print("subsets\t\t total weight\t total value")
print("-" * 45)

for r in range(n + 1):
    for subset in combinations(range(n), r):
        total_weight = sum(weights[i] for i in subset)
        total_value = sum(values[i] for i in subset)
        if total_weight <= capacity:
            print(f"{[i for i in subset]}\t\t {total_weight}\t\t {total_value}")
            if total_value > best_value:
                best_value = total_value
                best_subset = subset

print("\nOptimal solution:")
print("items selected:", [i for i in best_subset])
print("maximum value:", best_value)