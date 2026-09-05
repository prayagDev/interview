from collections import defaultdict

text = "programming"
result = defaultdict(int)

for char in text:
    result[char] += 1

print(dict(result))