from collections import defaultdict

def main(data):
    result = defaultdict(list)
    for name, marks in data:
        result[marks].append(name)
    return result

if __name__ == "__main__":
    data = [
        ("Rahul", 90),
        ("Aman", 80),
        ("Riya", 90),
        ("Priya", 80),
        ("Rohit", 70)
    ]
    result = main(data)
    print(result)
    print()
    print(dict(result))

