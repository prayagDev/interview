nums = range(1_000_000)

# Nothing has been calculated yet.
# Only a generator object is created.
result = (
    num * num
    for num in nums
    if num % 2 == 0
)

print(result)


'''
Notice

There is no list.

Generator asked for next value

↓

Take next number from range

↓

Check if even

↓

Square it

↓

Return ONE value

↓

for loop uses it

↓

Generator forgets it

↓

Repeat

'''

# At no point are all 500,000 squares stored.

