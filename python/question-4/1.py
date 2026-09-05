from collections import Counter

text = "programming"
result = Counter(text)

# Output as a standard dictionary
print(dict(result))

data = ['apple', 'banana', 'cherry', 'apple']
print(dict(Counter(data)))