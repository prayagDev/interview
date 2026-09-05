from collections import defaultdict

employees = [
    ("Engineering", "Rahul"),
    ("HR", "Aman"),
    ("Engineering", "Zoya"),
    ("HR", "Priya"),
    ("Engineering", "Aman"),
]

# Step 1: Group names by department using defaultdict
grouped = defaultdict(list)
for dept, name in employees:
    grouped[dept].append(name)

# Step 2: Sort names alphabetically for each department
result = {dept: sorted(names) for dept, names in grouped.items()}

print(result)
