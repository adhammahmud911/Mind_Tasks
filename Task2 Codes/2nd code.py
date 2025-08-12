from itertools import product
print("enter K then M")
# Read K and M
K, M = map(int, input().split())

# Read all lists
lists = []
for _ in range(K):
    print(f"Enter the number of elements in list then the elements:")
    data = list(map(int, input().split()))
    Ni = data[0]
    elements = data[1:]
    lists.append(elements)

# Try all combinations
max_s = 0
for combo in product(*lists):
    total = sum(x**2 for x in combo) % M
    if total > max_s:
        max_s = total

print("\n The maximum possible value is:",max_s)
