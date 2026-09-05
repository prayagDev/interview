sales = [
    ("Delhi", "Laptop"),
    ("Delhi", "Mobile"),
    ("Delhi", "Laptop"),
    ("Mumbai", "Laptop"),
    ("Mumbai", "Mobile"),
    ("Mumbai", "Mobile")
]

from collections import defaultdict, Counter

result = defaultdict(Counter)

for location, device in sales:
    result[location][device] += 1

print(result)

formatted_result = {city: dict(counts) for city, counts in result.items()}
print(formatted_result)