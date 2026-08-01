# range() itself is lazy (doesn't create 1 million numbers)
nums = range(1_000_000)

# Empty list created in memory
result = []

# for loop internally creates an iterator over nums
for num in nums:

    # Process one number at a time
    if num % 2 == 0:

        # Square it
        square = num * num

        # IMPORTANT:
        # This value is stored permanently inside result
        result.append(square)

# After loop completes,
# result contains ALL squared even numbers
print(len(result))


'''
Memory
range
   │
iterator
   │
   ▼
result list

[0,4,16,36,64,100,....]

Trade-off:

✔ Easy
✔ Fast
❌ Stores ~500,000 values in RAM
'''

