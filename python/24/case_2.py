nums = range(1_000_000)

# Looks different...
# But internally Python is doing almost the same thing
result = [
    num * num           # Square
    for num in nums     # Iterate one number at a time
    if num % 2 == 0     # Keep only even
]

# Entire list already exists
print(len(result))

'''
Trade-off:

✔ Cleaner
✔ Usually slightly faster than manual loop
❌ Still stores every result

'''

