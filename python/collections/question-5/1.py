from collections import defaultdict

data = [
    ("Rahul", "Python"),
    ("Rahul", "Django"),
    ("Rahul", "Python"),
    ("Aman", "Python")
]

result = defaultdict(set)

for name, course in data:
    result[name].add(course)

print(dict(result))

